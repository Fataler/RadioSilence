transform headache_pulse(period=1.85, zoom_str=0.01, shift=1):
    anchor (0.5, 0.5)   
    align (0.5, 0.5)
    parallel:
        zoom 1.0
        linear period/2 zoom (1.0 + zoom_str)
        linear period/2 zoom 1.0
        repeat
    parallel:
        xoffset 0 yoffset 0
        linear 0.04 xoffset shift
        linear 0.04 xoffset -shift
        linear 0.04 xoffset 0
        pause 1.0
        repeat

transform pulse_alpha(period=0.925, a1=0.15, a2=0.5):
    alpha a1
    linear period/2 alpha a2
    linear period/2 alpha a1
    repeat

label scene_pulse:
    show layer master at headache_pulse

    show pulse_mask at pulse_alpha:
        xalign 0.5 yalign 0.5
    return