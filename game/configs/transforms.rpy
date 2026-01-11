transform bandit_c_left:
    xalign -0.2
    yalign 1.0

transform fel_table_pos:
    xpos 0

transform fel_board_pos:
    xpos -100
#common
transform c_left:
    xalign 0.1
    yalign 1.0

transform c_right:
    xalign 0.95
    yalign 1.0

transform face_left:
    xzoom -1.0

transform face_right:
    xzoom 1.0

# для сцен с 5 персонажами
transform penta_left:
    xalign 0
    yalign 1.0

transform penta_left_center:
    xalign 0.25
    yalign 1.0

transform penta_center:
    xalign 0.5
    yalign 1.0

transform penta_right_center:
    xalign 0.75
    yalign 1.0

transform penta_right:
    xalign 1.0
    yalign 1.0

# для сцен с 4 персонажами
transform quad_left:
    xalign 0
    yalign 1.0

transform quad_left_center:
    xalign 0.33
    yalign 1.0

transform quad_right_center:
    xalign 0.66
    yalign 1.0

transform quad_right:
    xalign 1.0
    yalign 1.0

# для сцен с 3 персонажами
transform trio_left:
    xalign 0.1
    yalign 1.0

transform trio_center:
    xalign 0.5
    yalign 1.0

transform trio_right:
    xalign 0.95
    yalign 1.0

transform size_change(x=0.5, z=0.5):
    xzoom x
    yzoom z

transform delay_appear(delay = 1.0, time = 0.5):
    alpha 0
    pause delay
    linear time alpha 1.0

transform delay_hide(delay = 1.0, time = 0.5):
    alpha 1.0
    pause delay
    linear time alpha 0.0

transform zoom_appear(start = 0, end = 1.0, time = 0.5):
    zoom start
    linear time zoom end

# Уход персонажа за левый край экрана
transform exit_left(time=2.0):
    parallel:
        ease time xpos -1000
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

# Уход персонажа за правый край экрана
transform exit_right(time=4.0):
    parallel:
        ease time xpos 3000
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

# Вход персонажа слева
# transform enter_left(time=2.0, from_right=False):
#     xpos (2000 if from_right else -1000)
#     parallel:
#         ease time xalign 0.2
#     parallel:
#         block:
#             ease 0.2 yoffset 20
#             ease 0.2 yoffset 0
#             repeat (int(time * 2.5))

transform enter_c_left(time=2.0, from_right=False):
    xpos (2000 if from_right else -1000)
    parallel:
        ease time xalign 0.1
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform enter_c_right(time=2.0, from_left=False, xalign=0.95):
    xpos (-1000 if from_left else 2000)
    parallel:
        ease time xalign xalign
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform enter_scene(time=2.0, from_left=False, xalign=0.95, y=1.0):
    xpos (-1000 if from_left else 2000)
    yalign y
    parallel:
        ease time xalign xalign
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform move_on_scene(time=2.0, xalign=0.95):
#    xpos (x)
#    ypos (y)
    parallel:
        ease time xalign xalign
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform move_on_scene_slow(time=6.0, xalign=2.0):
    parallel:
        ease time xalign xalign
    parallel:
        block:
            ease 0.4 yoffset 20
            ease 0.4 yoffset 0
            repeat (int(time * 5.0))

#как листочек типа падает
transform fall_like_leaf(time=5.0, yalign=25.0):
    parallel:
        ease time yalign yalign
    parallel:
        block:
            ease 0.9 xoffset 50
            ease 0.9 xoffset 0
            repeat (int(time * 0.5))

transform move_vertically(time=1.0, x=0.5, yalign1=0, yalign2=1.0):
        xalign x
        yalign yalign1
        ease time yalign yalign2

transform collapse:
    ease 0.5 yalign 2.0

transform move_on_scene_repeat(easey=0, offsety=0):
    parallel:
        block:
            ease easey yoffset offsety
            ease easey yoffset 0
            repeat

transform step_up(steps=1, step_time=0.3, step_size=10):
    yoffset 0
    ease step_time yoffset step_size
    ease step_time yoffset 0
    repeat steps

transform move_step(xoffset=-100, time=0.3, steps = 1):
    parallel:
        xoffset 0
        linear time xoffset xoffset
    parallel:
        yoffset 0
        ease time yoffset 10
        ease time yoffset 0
        repeat steps

transform background_step(start=-1920, offset=100, time=0.5, yoffset=0):
    parallel:
        xpos start
        linear time xpos (start + offset)
    parallel:
        yoffset 0
        ease time yoffset yoffset
        ease time yoffset 0

# Вход персонажа справа
# transform enter_right(time=2.0, xalign = 0.8):
#     xpos 1920 + 1000
#     parallel:
#         ease time xalign xalign
#     parallel:
#         block:
#             ease 0.2 yoffset 20
#             ease 0.2 yoffset 0
#             repeat (int(time * 2.5))

transform jump(times = 1, height = 100, speed = 0.3):
    yoffset 0
    linear speed yoffset height
    repeat times

transform step_right(steps=1, step_time=0.3, step_size=50):
    parallel:
        xoffset 0
        linear steps * step_time xoffset steps * step_size
    parallel:
        yoffset 0
        ease step_time/2 yoffset 10
        ease step_time/2 yoffset 0
        repeat steps

transform step_left(steps=1, step_time=0.3, step_size=50):
    parallel:
        xoffset 0
        linear steps * step_time xoffset steps * -step_size
    parallel:
        yoffset 0
        ease step_time/2 yoffset 10
        ease step_time/2 yoffset 0
        repeat steps

transform panic_run(times=4, run_time=0.5, distance=150):
    parallel:
        xoffset 0
        xzoom 1
        linear run_time xoffset distance
        xzoom -1
        linear run_time xoffset -distance
        repeat times
    parallel:
        yoffset 0
        ease run_time/2 yoffset 10
        ease run_time/2 yoffset 0
        repeat (times * 2)

transform flip:
    xzoom -1

transform flip_back:
    xzoom 1

transform put_down(speed=0.2, offset=-10):
    parallel:
        linear speed xoffset offset
        linear speed xoffset 0
    parallel:
        linear speed yoffset 50
        linear speed yoffset 0

transform punch_h(duration=0.1, strength=10):
    xoffset 0
    ease duration/4 xoffset strength
    ease duration/4 xoffset -strength
    ease duration/4 xoffset strength/2
    ease duration/4 xoffset 0

transform hide_after_pause(time = 1, alpha_time = 0.1):
    pause time
    linear alpha_time alpha 0.0

transform giggle(height=5, shake=3, repeats=3, speed=0.15):
    parallel:
        ease speed yoffset height
        ease speed yoffset 0
        repeat repeats
    parallel:
        ease speed*0.7 xoffset shake
        ease speed*0.7 xoffset -shake
        repeat (repeats + 1)

transform fear(height=10, shake=5, repeats=2, fade=0.2):
    parallel:
        ease 0.2 yoffset height
        ease 0.2 yoffset 0
        repeat repeats
    parallel:
        ease 0.15 xoffset shake
        ease 0.15 xoffset -shake
        repeat (repeats + 1)

transform joy(height=10, shake=3, repeats=2, speed=0.15):
    parallel:
        ease speed yoffset height
        ease speed yoffset 0
        repeat repeats
    parallel:
        ease speed*0.7 xoffset shake
        ease speed*0.7 xoffset -shake
        repeat repeats

transform scared(height=30, speed=0.15):
    yoffset 0
    ease speed yoffset height*0.7
    ease speed*1.5 yoffset 0
    ease speed*0.5 yoffset height*0.3
    ease speed yoffset 0

transform angry(height=8, shake=5, repeats=3, speed=0.1):
    parallel:
        ease speed yoffset height
        ease speed yoffset 0
        repeat repeats
    parallel:
        ease speed*0.5 xoffset -shake
        ease speed*0.5 xoffset shake
        repeat (repeats * 2)

transform flipping(repeats=3, pause_time=0.9, flip_time=0.3):
    xzoom 1.0
    block:
        pause pause_time
        xzoom -1.0
        pause pause_time
        xzoom 1.0
        repeat repeats

transform y_offset_appear(start=0, end=100, time=0.5):
    yoffset start
    alpha 0
    linear time yoffset end alpha 1.0

transform y_offset_hide(start=0, end=100, time=0.5):
    yoffset start
    alpha 1.0
    linear time yoffset end alpha 0.0

transform x_offset_appear(start=0, end=100, time=0.5):
    xoffset start
    alpha 0
    easein_quad time xoffset end alpha 1.0

transform x_offset_hide(start=0, end=100, time=0.5):
    xoffset start
    alpha 1.0
    easein_quad time xoffset end alpha 0.0

transform take_in(start=0, end=100, time=0.5):
    xoffset start
    yoffset start
    alpha 0
    parallel:
        easein_quad time/2 xoffset end/2 yoffset end/2
        easein_quad time/2 xoffset end yoffset end
    parallel:
        easein_quad time/2 alpha 1.0

transform take_out(start=0, end=100, time=0.5):
    xoffset start
    yoffset start
    alpha 1.0
    parallel:
        easein_quad time/2 xoffset -end/2 yoffset end/2
        easein_quad time/2 xoffset -end yoffset end
    parallel:
        easein_quad time alpha 0

transform txt_up(start=-0.9, end=2.4, time=40.0):
    yalign start
    linear time yalign end

#тряска медленная
transform shaky(time=3.0):
    block:
        ease 0.9 xoffset 30
        ease 0.9 xoffset 0
        repeat (int(time * 0.5))

#тряска быстрая
transform shaky_fast(time=15.0):
    block:
        ease 0.05 xoffset 10
        ease 0.05 xoffset 0
        repeat (int(time * 0.5))

#плавно присел
transform down_little:
    xalign 0.5
    yalign 1.0
    linear 0.6 yoffset 50  

#и встал
transform up_little:
    xalign 0.5
    yalign 1.0
    linear 1.0 yoffset 50

transform move_down:
    #xalign 0.5
    #yalign 1.0
    linear 0.5 yoffset 50 

transform hover_shake_x(dx=4, speed=0.05):
    on hover:
        block:
            linear speed xoffset dx
            linear speed xoffset -dx
            repeat
    on idle:
        ease speed xoffset 0

transform hover_shake_y(dy=4, speed=0.05):
    on hover:
        block:
            linear speed yoffset dy
            linear speed yoffset -dy
            repeat
    on idle:
        ease speed yoffset 0

transform hue_cycle(time=10.0):
    matrixcolor HueMatrix(0)
    linear time matrixcolor HueMatrix(360)
    repeat

transform screen_fade_effect(time=0.5):
    on show:
        alpha 0
        linear time alpha 1.0
    on hide:
        alpha 1.0
        linear time alpha 0.0

transform screen_fade_effect_in_out(time=0.5, start_alpha=0.0, end_alpha=1.0, initial_alpha=0.0):
    on show:
        alpha initial_alpha
        block:
            linear time alpha end_alpha
            linear time alpha start_alpha
            repeat
    on hide:
        alpha end_alpha
        linear time alpha initial_alpha

transform fade_in_out(fade_time=2.0, max_alpha=1.0, min_alpha=0.0, delay=0.0):
    alpha 0
    pause delay
    block:
        linear fade_time alpha max_alpha
        linear fade_time alpha min_alpha
        repeat

#blend - max, min, add, multiply
transform fade_in_out_blend(fade_time=2.0, max_alpha=1.0, min_alpha=0.0, from_zero = True, blend_type = "max"):
    blend blend_type
    alpha (0 if from_zero else min_alpha)
    block:
        linear fade_time alpha max_alpha
        linear fade_time alpha min_alpha
        repeat

transform light_hurt:
    alpha 0
    linear 1.0 alpha 0.9
    pause 0.5
    linear 1.0 alpha 0.4

transform alpha_mask(a=0.4):
    alpha a

transform alpha_mask_fade(a=0.4, time=1.0, initial_alpha=0.0):
    alpha initial_alpha
    linear time alpha a

transform alpha_mask_fade_inverse(a=0.4, time=1.0):
    alpha a
    linear time alpha 0

transform alpha_mask_fade_inverse1(a=0.4, time=1.0):
    alpha 1.0
    linear time alpha a

transform screen_shake(dx=10, dy=0, t=0.05):
    xoffset 0 yoffset 0
    linear t xoffset dx yoffset dy
    linear t xoffset -dx yoffset -dy
    linear t xoffset 0 yoffset 0

transform screen_step(dx=10, dy=5, t=0.2):
    xoffset 0 yoffset 0
    linear t xoffset dx yoffset dy
    linear t xoffset -dx yoffset dy
    linear t xoffset 0 yoffset 0

transform screen_step_zoom(dx=10, dy=5, t=0.2, period=1.85, zoom_str=0.025, zoom1=1.0):
    anchor (1.0, 0.5)
    align (0.8, 0.5)
    parallel:
        zoom zoom1
        linear period/2 zoom (zoom1 + zoom_str)
    parallel:
        xoffset 0 yoffset 0
        linear t xoffset dx yoffset dy
        linear t xoffset -dx yoffset dy
        linear t xoffset 0 yoffset 0

transform space_drift(speed=8.0, intensity=0.3, pulse_speed=3.0):
    subpixel True
    parallel:
        block:
            linear speed*0.5 xoffset (intensity*2)
            linear speed*0.5 xoffset (-intensity*2)
            linear speed*0.5 xoffset intensity
            linear speed*0.5 xoffset (-intensity)
            repeat

    parallel:
        block:
            linear speed*0.7 yoffset (intensity*1.5)
            linear speed*0.7 yoffset (-intensity*1.5)
            linear speed*0.7 yoffset (intensity*0.8)
            linear speed*0.7 yoffset (-intensity*0.8)
            repeat

    parallel:
        block:
            linear (pulse_speed*0.4) zoom 1.002
            linear (pulse_speed*0.3) zoom 0.998
            linear (pulse_speed*0.3) zoom 1.001
            repeat

    
transform space_door_open(speed=1):
    xalign 0.5
    yalign 0.5
    zoom 1.0
    
    linear 1 zoom 0.95
    pause 1
    linear speed * 3 xoffset 600

transform fade_on_show(t=1.0):
    on show:
        alpha 0.0
        linear t alpha 1.0
    on hide:
        alpha 1.0
        linear t alpha 0.0