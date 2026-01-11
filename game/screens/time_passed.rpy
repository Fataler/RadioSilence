## Экран "Прошло времени" #####################################################
##
## Ипользуется для перебивки между сценами.
##

define run_time = 5
define blue_color = Color("#393185")

# image time_animation:
#     "images/Prochee/p1.png"
#     pause 0.2
#     "images/Prochee/p2.png"
#     pause 0.2
#     repeat

# image time_animation_colored = Transform("time_animation", matrixcolor=TintMatrix(blue_color)) 

layeredimage time_passed_img:
    always:
        "bg_menu_main"

    always:
        "time_animation_colored"

transform show_screen_transform(show_time=0.5, hide_time=0.5):
    on show:
        parallel:
            alpha 0.0
            linear show_time alpha 1.0
    on hide:
        linear hide_time alpha 0.0

transform loading_move:
    xzoom -1.0
    parallel:
        xpos -128 yalign 0.95
        linear run_time xpos 1920+128
    parallel:
        block:
            ease 1 yoffset 20
            ease 1 yoffset 0
            repeat

# init python:
#     loading_frames = []
#     for j in range(3):  # по вертикали
#         for i in range(4):  # по горизонтали
#             loading_frames.append(
#                 Transform(
#                     "gui/loading.png",
#                     crop=(697 * i, 800 * j, 697, 800)
#                 )
#             )

# image loading_animation:
#     size (128, 128)
#     block:
#         loading_frames[0]
#         0.1
#         loading_frames[1]
#         0.1
#         loading_frames[2]
#         0.1
#         loading_frames[3]
#         0.1
#         loading_frames[4]
#         0.1
#         loading_frames[5]
#         0.1
#         loading_frames[6]
#         0.1
#         loading_frames[7]
#         0.1
#         loading_frames[8]
#         0.1
#         loading_frames[9]
#         0.1
#         loading_frames[10]
#         0.1
#         loading_frames[11]
#         0.1
#         repeat

screen time_passed(text="Прошло времени..."):
    modal True
    
    fixed:
        xfill True
        yfill True
        at show_screen_transform
        
        add "time_passed_img"
        
        vbox:
            align (0.5, 0.5)
            spacing 50
            
            text text:
                size 80
                color blue_color
                text_align 0.5
                at transform:
                    alpha 0.0
                    pause 1.0
                    ease 2.0 alpha 1.0

    timer run_time action Return()

label time_passed_label(message = "Некоторое время спустя"):
    window hide
    stop music
    stop sound
    call screen time_passed(message)
    scene bg_black
    pause 1
    stop sound
    window show
return