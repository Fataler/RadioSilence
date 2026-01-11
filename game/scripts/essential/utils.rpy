#region robot say
init -1 python:
    import random

    robot_char = Character("")
    
    def make_robot_bits(txt):
        # symbols = "0123456789ABCDEF"
        symbols = "01"
        
        # matrix_colors = ["#00ff00", "#00cc00", "#00ff41", "#00cc33"]
        
        robot_bits = ""
        for char in txt:
            if char != " ":
                symbol = random.choice(symbols)
                color = "#ffffff"
                robot_bits += "{color=" + color + "}" + symbol + "{/color}"
            else:
                robot_bits += char
        return robot_bits

    def robot_say(what, **kwargs):
        bits = make_robot_bits(str(what))
        
        robot_char("{font=gui/fonts/DejaVuSansMono.ttf}{cps=200}" + bits + "{/font}", interact=False)
        
        renpy.pause(0.3, hard=True)
        
        return robot_char("{font=gui/fonts/DejaVuSansMono.ttf}{cps=999}" + str(what) + "{/font}", interact=True)

# трансформ для моргания
transform parametric_blink(open_img, closed_img, min_wait=2.0, max_wait=4.0, blink_speed=0.15, double_blink_chance=0.03):
    open_img
    block:
        choice:
            pause min_wait
        choice:
            pause (min_wait + max_wait) / 2
        choice:
            pause max_wait
        closed_img
        pause 0.1
        open_img
        repeat
#endregion

#region eye_effect
#with eye_on
init python:
    eye_on = ImageDissolve("gui/masks/eye_mask.png", 0.3, 10, reverse=False)
    #eye_off = ImageDissolve("gui/masks/eye_mask.png", 0.3, 10, reverse=True)
    def eye_off(duration=0.3):
        return ImageDissolve("gui/masks/eye_mask.png", duration, 10, reverse=True)
#endregion

# region glitch text
# button:
#     xalign 0.5
#     xsize 750
#     ysize 50
#     background None
#     action NullAction()
#     idle_child Text("Секретное достижение", style="achievement_description")
#     hover_child DynamicDisplayable(glitch_text_func, "Секретное достижение")
init :
    image check = "gui/check.png"
    image check_bg = "gui/check_bg.png"

    python:
        import random

        def glitch_text_func(st, at, original_text="Секретное достижение"):
            chars = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯабвгдежзиклмнопрстуфхцчшщыэюя0123456789"
            noise = "█▓▒░◣◢◥◤▌▐┇┋╳/\\|#@*~"

            burst = (int(st * 12) % 16) < 3 or random.random() < 0.06

            if burst:
                p_replace = 0.55
                p_drop = 0.10
                p_dup = 0.08
                p_upper = 0.15
                jitter = 2
                alpha_shift = 0.55
                frame_time = 0.08
            else:
                p_replace = 0.12
                p_drop = 0.02
                p_dup = 0.03
                p_upper = 0.05
                jitter = 1
                alpha_shift = 0.35
                frame_time = 0.16

            out = []
            for ch in original_text:
                if ch == " ":
                    out.append(ch)
                    continue

                r = random.random()
                if r < p_drop:
                    continue
                elif r < p_drop + p_dup:
                    out.append(ch)
                    out.append(ch)
                    continue
                elif r < p_drop + p_dup + p_replace:
                    out.append(random.choice(chars + noise))
                else:
                    if random.random() < p_upper:
                        out.append(ch.upper())
                    else:
                        out.append(ch)

            glitched = "".join(out)

            base = Text(glitched, style="achievement_description")
            red = Text(glitched, style="achievement_description", color="#ff3b3b")
            cyan = Text(glitched, style="achievement_description", color="#3bf7ff")

            dx1 = random.randint(-jitter, jitter)
            dy1 = random.randint(-jitter, jitter)
            dx2 = random.randint(-jitter, jitter)
            dy2 = random.randint(-jitter, jitter)

            red_t = renpy.display.transform.Transform(red, xoffset=dx1, yoffset=dy1, alpha=alpha_shift)
            cyan_t = renpy.display.transform.Transform(cyan, xoffset=dx2, yoffset=dy2, alpha=alpha_shift)
            base_t = renpy.display.transform.Transform(base)

            container = renpy.display.layout.Fixed()
            container.add(red_t)
            container.add(cyan_t)
            container.add(base_t)
            return container, frame_time
#endregion

#region автомультики

# init python:
#     define_numbered_animation("scene_good_ending_mayak_mult", "CG/CG_lighthouse", 1, 13, mayak_speed)

init -1 python:
    def define_numbered_animation(image_name, folder, start, end, delay, ext=".png", padding=0):
        frames = []
        for i in range(start, end):
            n = str(i).zfill(padding)
            frames.extend([f"{folder}/{n}{ext}", delay])
        renpy.image(image_name, Animation(*frames))
#endregion
#region pause_sfx
init -1 python:
    def pause_sfx(enable):
        for ch in ("sfx", "sfx2", "sfx3", "sound"):
            renpy.music.set_pause(enable, channel=ch)
#endregion