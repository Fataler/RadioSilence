init -999 python:
    renpy.register_shader("fx.radio_divide", variables="""
        uniform float u_time;
        uniform sampler2D tex0;
        uniform sampler2D u_tex1;
        uniform float u_brightness;
        uniform float u_line_width;
        uniform float u_speed;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, vertex_200="""
        v_coords = a_tex_coord;
    """, fragment_300="""
        vec4 base = texture2D(tex0, v_coords);
        
        float x = (v_coords.x - mod(u_time * u_speed, 1.4) + 0.2) / u_line_width;
        
        float mask = step(0.0, x) * step(x, 1.0);
        
        vec4 blend = texture2D(u_tex1, vec2(clamp(x, 0.0, 1.0), v_coords.y));
        
        vec3 res = (base.rgb / max(blend.rgb, 0.75)) * u_brightness;
        
        base.rgb = mix(base.rgb, res, blend.a * mask);
        
        gl_FragColor = base;
    """)

# Компактный ATL-трансформ
transform radio_scan_effect(line="menu_ogurchik", brightness=1.05, width=0.12, speed=0.4):
    shader "fx.radio_divide"
    u_tex1 renpy.displayable(line)
    u_brightness brightness
    u_line_width width
    u_speed speed
    mesh True
    pause 0.01
    repeat
