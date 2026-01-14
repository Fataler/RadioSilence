init -2 python:
    renpy.register_shader(
        "fx.fog_overlay",
        variables=r"""
            uniform float u_time;

            uniform float u_fog_density;   // плотность
            uniform float u_fog_scale;     // шум
            uniform float u_fog_speed;     // скорость
            uniform vec4  u_fog_color;     // цвет (rgba)
            uniform float u_fog_y0;        // где начинается усиление по Y (0..1)
            uniform float u_fog_y1;        // где заканчивается усиление по Y (0..1)
        """,
        fragment_functions=r"""
            float fog_hash(vec2 p) {
                p = fract(p * vec2(123.34, 456.21));
                p += dot(p, p + 45.32);
                return fract(p.x * p.y);
            }

            float fog_noise(vec2 p) {
                vec2 i = floor(p);
                vec2 f = fract(p);

                float a = fog_hash(i);
                float b = fog_hash(i + vec2(1.0, 0.0));
                float c = fog_hash(i + vec2(0.0, 1.0));
                float d = fog_hash(i + vec2(1.0, 1.0));

                vec2 u = f * f * (3.0 - 2.0 * f);
                return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
            }

            float fog_fbm(vec2 p) {
                float v = 0.0;
                float a = 0.5;
                for (int i = 0; i < 5; i++) {
                    v += a * fog_noise(p);
                    p *= 2.0;
                    a *= 0.5;
                }
                return v; // ~0..1
            }
        """,
        fragment_450=r"""
            vec2 uv = v_tex_coord.xy;

            vec2 p = uv * u_fog_scale + vec2(u_time * u_fog_speed, u_time * u_fog_speed * 0.31);
            float n = fog_fbm(p);

            float vertical = smoothstep(u_fog_y0, u_fog_y1, uv.y);

            float A = clamp(n * u_fog_density * vertical, 0.0, 1.0) * u_fog_color.a;

            gl_FragColor = vec4(u_fog_color.rgb * A, A);
        """
    )

transform fog_overlay(
    density=1.65,
    scale=5.0,
    speed=0.08,
    color=(0.90, 0.92, 1.00, 0.75),
    y0=0.40,
    y1=1.00
):
    mesh True
    shader "fx.fog_overlay"

    u_fog_density density
    u_fog_scale   scale
    u_fog_speed   speed
    u_fog_color   color
    u_fog_y0      y0
    u_fog_y1      y1

    pause 1.0/30
    repeat

screen fog_layer():
    layer "master"
    zorder 100
    add Solid("#ffffff") at fog_overlay()


label test_fog:

    show screen fog_layer

    show tuman_bg
    with dissolve

    "Тест1"

    show bg_dinner_block
    with dissolve

    "Тест2"
    return
