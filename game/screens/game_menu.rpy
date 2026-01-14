## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None или один из "viewport" или "vpgrid". Этот
## экран предназначен для использования с одним или несколькими дочерними
## элементами, которые трансклюдируются (помещаются) внутрь него.

transform menu_move:
    pause 0.3
    parallel:
        ease 0.5 xoffset -390

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    
    style_prefix "game_menu"

    frame:
        top_margin 15
        xsize 1390
        style "game_menu_outer_frame"

        hbox:

            frame at vhs_crt_frame(
                        window=(0.00, 0.00, 1.00, 1.0),
                        corner=0.018,
                        edge_soft=0.003,

                        frame_color=(0.0, 0.0, 0.0, 1.0),
                        frame_noise=0.01,

                        curvature=0.025,
                        chroma=0.0005,
                        jitter=0.0008,
                        warp=0.0002,
                        scan=0.85,
                        noise=0.50,
                        vignette=0.45,
                        roll=0.45,
                        roll_speed=0.30,

                        brightness=0.02,
                        contrast=1.05
                        ):
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:
                    transclude

    imagebutton:
        idle "knopka_nazad"
        hover At("knopka_nazad", set_bright_hovered(0.1))
        action (ShowMenu(MAIN_MENU_SCREEN, from_game_menu=True) if main_menu else Return())
        align (0.95, 0.95)
        focus_mask True

    if main_menu:
        key "game_menu" action ShowMenu(MAIN_MENU_SCREEN, from_game_menu=True)
    else:
        key "game_menu" action Return()


style game_menu_outer_frame is empty:
    #background "#90909085"
    #xpos 0.15
    yoffset 0
    
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

# style return_button is gui_button
# style return_button_text is main_menu_button_text

style game_menu_content_frame:
    #background "#90909085"
    margin (10, 10, 10, 0)
    xoffset 418
    yoffset 80
    xsize 1100
    ysize 830

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 190

style game_menu_label_text:
    size gui.title_text_size
    color gui.interface_text_color
    yalign 0.5

style return_button:
    anchor (1.0, 0.5)
    xpos gui.navigation_xpos
    hover_color gui.hover_color
    yalign 1.0
    yoffset -45