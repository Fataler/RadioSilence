define mv_bands_default = 100
define mv_window_ms = 20
define mv_min_freq = 44
define mv_max_freq = 22000
define mv_smoothing = 0.4
define mv_gamma = 0.3

init python:
    import math
    import wave
    from array import array

    mv_wav_cache = {}
    mv_blackman_cache = {}

    def mv_hex_to_rgb(s):
        s = s.lstrip('#')
        return (int(s[0:2],16), int(s[2:4],16), int(s[4:6],16))

    def mv_rgb_to_hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    def mv_grad_color(i, n):
        pts = [(0.0, mv_hex_to_rgb("#fffb00")), (0.5, mv_hex_to_rgb("#ff005d")), (1.0, mv_hex_to_rgb("#ff0000"))]
        x = 0.0 if n<=1 else i/float(n-1)
        t0,c0 = pts[0]
        for t1,c1 in pts[1:]:
            if x <= t1:
                k = 0.0 if t1==t0 else (x-t0)/(t1-t0)
                r = int(c0[0] + (c1[0]-c0[0])*k)
                g = int(c0[1] + (c1[1]-c0[1])*k)
                b = int(c0[2] + (c1[2]-c0[2])*k)
                return mv_rgb_to_hex(r,g,b)
            t0,c0 = t1,c1
        r,g,b = pts[-1][1]
        return mv_rgb_to_hex(r,g,b)

    def mv_blackman(n):
        w = mv_blackman_cache.get(n)
        if w is not None:
            return w
        a0 = 0.42
        a1 = 0.5
        a2 = 0.08
        w = [a0 - a1*math.cos(2.0*math.pi*k/(n-1)) + a2*math.cos(4.0*math.pi*k/(n-1)) for k in range(n)]
        mv_blackman_cache[n] = w
        return w

    def mv_logspace(a, b, n):
        if n <= 1:
            return [b]
        out = []
        la = math.log(a)
        lb = math.log(b)
        for i in range(n):
            t = i/float(n-1)
            out.append(math.exp(la*(1.0-t) + lb*t))
        return out

    def mv_load_wav(audio_path):
        info = mv_wav_cache.get(audio_path)
        if info is not None:
            return info
        try:
            f = renpy.loader.load(audio_path)
        except Exception:
            return None
        try:
            wf = wave.open(f,'rb')
        except Exception:
            return None
        try:
            channels = wf.getnchannels()
            sampwidth = wf.getsampwidth()
            framerate = wf.getframerate()
            nframes = wf.getnframes()
            data = wf.readframes(nframes)
        finally:
            try:
                wf.close()
            except Exception:
                pass
        info = {
            'channels': channels,
            'sampwidth': sampwidth,
            'framerate': framerate,
            'nframes': nframes,
            'data': data
        }
        mv_wav_cache[audio_path] = info
        return info

    def mv_try_map_to_wav(audio_id):
        if not isinstance(audio_id, str):
            return None
        if audio_id.endswith('.wav'):
            return audio_id
        base = None
        if audio_id.endswith('.mp3'):
            base = audio_id[:-4]
        elif audio_id.endswith('.ogg'):
            base = audio_id[:-4]
        if base:
            candidate = base + '.wav'
            try:
                f = renpy.loader.load(candidate)
                f.close()
                return candidate
            except Exception:
                return None
        return None

    def mv_read_window(info, time_sec, window_samples):
        ch = info['channels']
        sw = info['sampwidth']
        sr = info['framerate']
        data = info['data']
        frame0 = int(time_sec*sr) - window_samples//2
        if frame0 < 0:
            frame0 = 0
        if frame0 + window_samples > info['nframes']:
            frame0 = max(0, info['nframes'] - window_samples)
        bytes_per_frame = ch*sw
        start = frame0*bytes_per_frame
        end = start + window_samples*bytes_per_frame
        if start >= len(data):
            return ([], [])
        chunk = data[start:end]
        if sw == 2:
            arr = array('h')
            arr.frombytes(chunk)
            left = []
            right = []
            if ch == 1:
                for v in arr:
                    left.append(v/32768.0)
                    right.append(v/32768.0)
            else:
                for i in range(0, len(arr)-1, ch):
                    l = arr[i]/32768.0
                    r = arr[i+1]/32768.0
                    left.append(l)
                    right.append(r)
        else:
            arr = array('B')
            arr.frombytes(chunk)
            left = []
            right = []
            if ch == 1:
                for v in arr:
                    s = (v-128)/127.0
                    left.append(s)
                    right.append(s)
            else:
                for i in range(0, len(arr)-1, ch):
                    l = (arr[i]-128)/127.0
                    r = (arr[i+1]-128)/127.0
                    left.append(l)
                    right.append(r)
        n = min(len(left), window_samples)
        return (left[:n], right[:n])

    def mv_goertzel_power(seq, freq_hz, sr):
        n = len(seq)
        if n <= 0:
            return 0.0
        w = 2.0*math.pi*freq_hz/sr
        c = 2.0*math.cos(w)
        s_prev = 0.0
        s_prev2 = 0.0
        win = mv_blackman(n)
        for i in range(n):
            s = seq[i]*win[i] + c*s_prev - s_prev2
            s_prev2 = s_prev
            s_prev = s
        power = s_prev2*s_prev2 + s_prev*s_prev - c*s_prev*s_prev2
        return max(0.0, power)

    def mv_compute_bands_lr(info, time_sec, bands, min_f, max_f, window_ms):
        sr = info['framerate']
        win_samples = max(64, int(sr*window_ms/1000.0))
        lch, rch = mv_read_window(info, time_sec, win_samples)
        n = min(len(lch), len(rch))
        if n <= 0:
            return ([0.0]*bands, [0.0]*bands)
        lch = lch[:n]
        rch = rch[:n]
        freqs = mv_logspace(min_f, max_f, bands)
        out_l = []
        out_r = []
        for f in freqs:
            pl = mv_goertzel_power(lch, f, sr)
            pr = mv_goertzel_power(rch, f, sr)
            out_l.append(pl)
            out_r.append(pr)
        return (out_l, out_r)

screen music_visualizer(
    channel="music",
    bands=mv_bands_default,
    width=None,
    height=360,
    bar_w=9,
    gap=6,
    base=10,
    max_h=220,
    glow_px=6,
    min_freq=mv_min_freq,
    max_freq=mv_max_freq,
    window_ms=mv_window_ms,
    smoothing=mv_smoothing,
    gamma=mv_gamma,
    yalign_val=0.5
):
    default viewport_w = width if width is not None else config.screen_width
    default tick = 0
    default last_pos = 0.0
    default bands_smooth = [0.0]*bands
    default norm_level = 0.01
    timer 0.016 repeat True action SetScreenVariable("tick", tick + 1)

    $ total_w = bands*bar_w + (bands-1)*gap
    $ x0 = (viewport_w - total_w) / 2.0

    $ audio_id = renpy.music.get_playing(channel)
    if isinstance(audio_id,(list,tuple)) and audio_id:
        $ audio_id = audio_id[0]
    $ wav_id = mv_try_map_to_wav(audio_id)
    $ pos = renpy.music.get_pos(channel)
    if pos is not None:
        $ last_pos = float(pos)
    $ t = last_pos

    $ amps = [0.0]*bands
    if wav_id:
        $ info = mv_load_wav(wav_id)
        if info:
            $ lvals, rvals = mv_compute_bands_lr(info, t, bands, min_freq, max_freq, window_ms)
            $ cur_max = 0.0001
            for i in range(bands):
                $ v = 0.6*((1.0 - (i/float(bands-1))) * lvals[i] + (i/float(bands-1)) * rvals[i]) + 0.4*((lvals[i]+rvals[i])*0.5)
                $ amps[i] = v
                if v > cur_max:
                    $ cur_max = v
            $ norm_level = max(norm_level*0.95, cur_max)
            for i in range(bands):
                $ a = min(1.0, max(0.0, amps[i] / (norm_level if norm_level>1e-6 else 1e-6)))
                $ bands_smooth[i] = smoothing*bands_smooth[i] + (1.0-smoothing)*a
    else:
        for i in range(bands):
            $ p = i/float(bands-1)
            $ a = 0.5*(math.sin((t*3.0)+p*4.0)*0.5+0.5)*(1.0-p*0.6)
            $ bands_smooth[i] = smoothing*bands_smooth[i] + (1.0-smoothing)*a

    fixed:
        xysize (viewport_w, height)
        align (0.5, yalign_val)
        for i in range(bands):
            $ a = max(0.0, min(1.0, bands_smooth[i]))
            $ a = a**gamma
            $ h = max(1, int(base + max_h*a))
            $ col = mv_grad_color(i, bands)
            $ x = int(x0 + i*(bar_w + gap))
            $ y = int((height - h)/2)
            if glow_px > 0:
                add Solid(col + "40") xysize (bar_w + glow_px, h) xpos (x - glow_px // 2) ypos y
            add Solid(col) xysize (bar_w, h) xpos x ypos y

label music_visualizer_demo:
    scene black
    # play music music_space_ambient_3
    show screen music_visualizer(channel="music")
    "Music visualizer"
    hide screen music_visualizer
    return


