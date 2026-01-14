
init -2 python:
    renpy.register_shader(
        "fx.radio_crt",
        variables=r"""
            uniform float u_time;
            uniform vec4  u_radio_window;
            uniform float u_radio_corner;
            uniform float u_radio_edge_soft;

            uniform float u_radio_curvature;
            uniform float u_radio_chroma;
            uniform float u_radio_jitter;
            uniform float u_radio_warp;
            uniform float u_radio_scan;
            uniform float u_radio_noise;
            uniform float u_radio_vignette;
            
            uniform float u_radio_brightness;
            uniform float u_radio_contrast;
            uniform vec3  u_radio_tint;
            uniform float u_radio_desat;
        """,
        fragment_functions=r"""
            float radio_hash(vec2 p) {
                p = fract(p * vec2(123.34, 456.21));
                p += dot(p, p + 45.32);
                return fract(p.x * p.y);
            }

            float radio_noise(vec2 p) {
                vec2 i = floor(p);
                vec2 f = fract(p);
                float a = radio_hash(i);
                float b = radio_hash(i + vec2(1.0, 0.0));
                float c = radio_hash(i + vec2(0.0, 1.0));
                float d = radio_hash(i + vec2(1.0, 1.0));
                vec2 u = f * f * (3.0 - 2.0 * f);
                return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
            }

            float radio_mask(vec2 uv, vec4 rect, float radius, float soft) {
                vec2 center = (rect.xy + rect.zw) * 0.5;
                vec2 halfsz = (rect.zw - rect.xy) * 0.5;
                vec2 p = uv - center;
                vec2 q = abs(p) - (halfsz - vec2(radius));
                float dist = length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - radius;
                return 1.0 - smoothstep(0.0, soft, dist);
            }
        """,
        fragment_450=r"""
            vec2 uv = v_tex_coord.xy;
            float inw = radio_mask(uv, u_radio_window, u_radio_corner, u_radio_edge_soft);

            vec2 w0 = u_radio_window.xy;
            vec2 wh = u_radio_window.zw - w0;
            vec2 p = ((uv - w0) / wh) * 2.0 - 1.0;

            float r2 = dot(p, p);
            p *= (1.0 + u_radio_curvature * r2);

            float j = (radio_noise(vec2(u_time * 20.0, gl_FragCoord.y * 0.1)) - 0.5) * u_radio_jitter;
            p.x += j + sin(gl_FragCoord.y * 0.02 + u_time * 5.0) * u_radio_warp;

            vec2 suv = clamp(w0 + (p * 0.5 + 0.5) * wh, w0, u_radio_window.zw);
            vec2 co = vec2(u_radio_chroma, 0.0);

            float rr = texture2D(tex0, suv + co, u_lod_bias).r;
            vec4 col = texture2D(tex0, suv, u_lod_bias);
            float bb = texture2D(tex0, suv - co, u_lod_bias).b;

            vec3 rgb = vec3(rr, col.g, bb);

            float gray = dot(rgb, vec3(0.299, 0.587, 0.114));
            rgb = mix(rgb, vec3(gray), u_radio_desat) * u_radio_tint;
            rgb = (rgb - 0.5) * u_radio_contrast + (0.5 + u_radio_brightness);

            float sl = 0.5 + 0.5 * sin(gl_FragCoord.y * 1.5);
            rgb *= 1.0 - u_radio_scan * (0.15 * sl);

            float n = radio_noise(gl_FragCoord.xy * 0.5 + vec2(u_time * 50.0, u_time * 17.0));
            rgb += (n - 0.5) * (u_radio_noise * 0.1);

            float vig = smoothstep(0.0, 1.0, 1.0 - r2 * 0.8);
            rgb *= mix(1.0 - u_radio_vignette, 1.0, vig);

            gl_FragColor = vec4(rgb, col.a) * inw;
        """
    )

transform radio_crt_effect(
    window=(0.0, 0.0, 1.0, 1.0),
    corner=0.05,
    edge_soft=0.01,
    curvature=0.08,
    chroma=0.003,
    jitter=0.003,
    warp=0.002,
    scan=0.7,
    noise=0.6,
    vignette=0.8,
    brightness=0.05,
    contrast=1.2,
    tint=(0.5, 1.0, 0.5),
    desat=1.0
):
    mesh True
    shader "fx.radio_crt"
    u_radio_window window
    u_radio_corner corner
    u_radio_edge_soft edge_soft
    u_radio_curvature curvature
    u_radio_chroma chroma
    u_radio_jitter jitter
    u_radio_warp warp
    u_radio_scan scan
    u_radio_noise noise
    u_radio_vignette vignette
    u_radio_brightness brightness
    u_radio_contrast contrast
    u_radio_tint tint
    u_radio_desat desat
    pause 1.0/30
    repeat