################################################################################
## Экран паузы
################################################################################

image pause_buttons_hover = "gui/menu/pause/game_menu_hover.png"
image pause_buttons_normal = "gui/menu/pause/game_menu_normal.png"

init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu(from_game_menu=False):
    on "show" action Function(pause_sfx, True)
    on "hide" action Function(pause_sfx, False)

    tag menu

    add "bg_black"
    add "menu_bg"

    imagemap:
        idle "pause_buttons_normal"
        hover "pause_buttons_hover"

        hotspot (1088, 443, 432, 374) action ShowMenu("preferences")
        hotspot (711, 322, 328, 470) action ShowMenu("history")
        hotspot (478, 268, 227, 240) action Return()
        hotspot (82, 388, 278, 175) action ShowMenu("save")
        hotspot (295, 550, 293, 136) action ShowMenu("load")
        hotspot (82, 690, 457, 355) action MainMenu()

    add "menu_setka"

style pause_menu_button is main_menu_button:
    xalign 0.5
    yalign 0.5

style pause_menu_button_text is main_menu_button_text:
    xalign 0.5
    yalign 0.5
    size 55

transform pause_menu_board_drop(start_pos = -900):
    ypos start_pos
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform pause_menu_board_hide(height = -900):
    ypos 0
    easeout 0.15 ypos -50
    easein 0.2 ypos 0
    easeout 0.5 ypos height

transform pause_menu_items_appear:
    alpha 0.0
    pause 0.5
    easein 0.3 alpha 1.0