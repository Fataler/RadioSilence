init -2 python:
    renpy.register_shader(
        "fx.vhs_crt_frame",
        variables=r"""
            uniform float u_time;

            uniform vec4  u_vhs_window;

            uniform float u_vhs_corner;
            uniform float u_vhs_edge_soft;

            uniform vec4  u_vhs_frame_color;   // rgb
            uniform float u_vhs_frame_noise;   // 0..1

            uniform float u_vhs_curvature;     // 0..0.25
            uniform float u_vhs_chroma;        // 0..0.01 (UV смещение)
            uniform float u_vhs_jitter;        // 0..0.01 (UV)
            uniform float u_vhs_warp;          // 0..0.01 (UV)
            uniform float u_vhs_scan;          // 0..1
            uniform float u_vhs_noise;         // 0..1
            uniform float u_vhs_vignette;      // 0..1
            uniform float u_vhs_roll;          // 0..1
            uniform float u_vhs_roll_speed;    // 0..2

            uniform float u_vhs_brightness;    // -0.2..0.2
            uniform float u_vhs_contrast;      // 0.7..1.4
        """,
        fragment_functions=r"""
            float vhs_hash(vec2 p) {
                p = fract(p * vec2(123.34, 456.21));
                p += dot(p, p + 45.32);
                return fract(p.x * p.y);
            }

            float vhs_noise(vec2 p) {
                vec2 i = floor(p);
                vec2 f = fract(p);
                float a = vhs_hash(i);
                float b = vhs_hash(i + vec2(1.0, 0.0));
                float c = vhs_hash(i + vec2(0.0, 1.0));
                float d = vhs_hash(i + vec2(1.0, 1.0));
                vec2 u = f * f * (3.0 - 2.0 * f);
                return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
            }

            float vhs_round_rect_mask(vec2 uv, vec4 rect, float radius, float soft) {
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
            float inw = vhs_round_rect_mask(uv, u_vhs_window, u_vhs_corner, u_vhs_edge_soft);

            float fn = vhs_noise(uv * 420.0 + vec2(u_time * 0.3, u_time * 0.17));
            vec3 frame = u_vhs_frame_color.rgb + (fn - 0.5) * u_vhs_frame_noise;

            vec2 w0 = u_vhs_window.xy;
            vec2 wh = u_vhs_window.zw - w0;
            vec2 cuv = (uv - w0) / wh;
            vec2 p = cuv * 2.0 - 1.0;

            float r2 = dot(p, p);
            p *= (1.0 + u_vhs_curvature * r2);

            float j = (vhs_noise(vec2(u_time * 28.0, gl_FragCoord.y * 0.05)) - 0.5) * u_vhs_jitter;
            p.x += j + sin(gl_FragCoord.y * 0.015 + u_time * 6.0) * u_vhs_warp;

            vec2 suv = clamp(w0 + (p * 0.5 + 0.5) * wh, w0, u_vhs_window.zw);

            float rr = texture2D(tex0, suv + vec2(u_vhs_chroma, 0.0), u_lod_bias).r;
            vec4 col = texture2D(tex0, suv, u_lod_bias);
            float bb = texture2D(tex0, suv - vec2(u_vhs_chroma, 0.0), u_lod_bias).b;

            vec3 rgb = vec3(rr, col.g, bb);
            rgb = (rgb - 0.5) * u_vhs_contrast + (0.5 + u_vhs_brightness);

            float sl = 0.5 + 0.5 * sin(gl_FragCoord.y * 3.1415927);
            float gr = 0.5 + 0.5 * sin(gl_FragCoord.x * 3.1415927);
            rgb *= 1.0 - u_vhs_scan * (0.10 * sl + 0.03 * gr);

            float n = vhs_noise(gl_FragCoord.xy * 0.25 + vec2(u_time * 60.0, u_time * 13.0));
            rgb += (n - 0.5) * (u_vhs_noise * 0.08);

            float t = fract(u_time * u_vhs_roll_speed + cuv.y);
            float band = smoothstep(0.48, 0.50, t) - smoothstep(0.50, 0.52, t);
            rgb += band * (u_vhs_roll * 0.15);

            float vig = smoothstep(0.0, 1.0, 1.0 - r2);
            rgb *= mix(1.0 - u_vhs_vignette, 1.0, vig);

            gl_FragColor = vec4(mix(frame, rgb, inw), col.a);
        """
    )

transform vhs_crt_frame(
    window=(0.08, 0.08, 0.92, 0.80),
    corner=0.018,
    edge_soft=0.003,

    frame_color=(0.0, 0.0, 0.0, 1.0),
    frame_noise=0.02,

    curvature=0.10,
    chroma=0.0025,
    jitter=0.0020,
    warp=0.0015,
    scan=0.85,
    noise=0.80,
    vignette=0.35,
    roll=0.55,
    roll_speed=0.40,

    brightness=0.02,
    contrast=1.05
):
    mesh True
    shader "fx.vhs_crt_frame"

    u_vhs_window window
    u_vhs_corner corner
    u_vhs_edge_soft edge_soft

    u_vhs_frame_color frame_color
    u_vhs_frame_noise frame_noise

    u_vhs_curvature curvature
    u_vhs_chroma chroma
    u_vhs_jitter jitter
    u_vhs_warp warp
    u_vhs_scan scan
    u_vhs_noise noise
    u_vhs_vignette vignette
    u_vhs_roll roll
    u_vhs_roll_speed roll_speed

    u_vhs_brightness brightness
    u_vhs_contrast contrast

    pause 1.0/30
    repeat

default vhs_demo_content = "bg_monitors_block"

screen vhs_demo(content=vhs_demo_content):
    default last_content = None
    default glitch = False

    if last_content != content:
        $ last_content = content
        $ glitch = True
        timer 0.20 action SetScreenVariable("glitch", False)

    fixed:
        at vhs_crt_frame()

        add content
        text "PLAY" xpos 0.12 ypos 0.10 color "#9aff9a" size 28
        text "SP 00:12:34" xpos 0.12 ypos 0.14 color "#9aff9a" size 22

        if glitch:
            add Solid("#b9b9b9") at glitch_flash

transform glitch_flash:
    alpha 0.0
    linear 0.02 alpha 0.35
    linear 0.08 alpha 0.0

label vhs_test():

    show screen vhs_demo(content="bg_monitors_block")
    "Демо изображение 1"

    show screen vhs_demo(content="bg_generator")
    "Демо изображение 2"

    show screen vhs_demo(content="bg_room_viktor_default")
    "Демо изображение 3"

    hide screen vhs_demo
    return

