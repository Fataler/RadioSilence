## Экран главного меню
image menu_ogurchik = "gui/menu/ogurchik.png"
image menu_setka_image = At("gui/menu/setka.png", Transform(size=(1920, 1080), alpha=0.7))
image menu_bg = "gui/menu/menu_bg.png"
image menu_logo = "gui/menu/Logo.png"
image menu_hover = "gui/menu/menu_hover.png"
image menu_normal = "gui/menu/menu_normal.png"

image menu_setka:
    "menu_setka_image"
    radio_scan_effect("menu_ogurchik", brightness=2.00, width=0.08, speed=0.3)

screen main_menu(from_game_menu=False):
    tag menu

    $ elements_apperar_time = 2.0 if not from_game_menu else 1.0

    add "bg_black"
    add "menu_bg"

    imagemap:
        idle "menu_normal"
        hover "menu_hover"

        hotspot (473, 261, 232, 247) action Start()
        hotspot (715, 386, 300, 365) action ShowMenu("about")
        hotspot (1047, 463, 461, 327) action ShowMenu("preferences")
        hotspot (285, 521, 288, 162) action ShowMenu("load")
        hotspot (112, 707, 408, 373) action Quit(confirm=not main_menu)

    style_prefix "main_menu"
    
    add "menu_setka"
    add "menu_logo"

    if show_main_menu_fade:
        add "bg_black" at menu_alpha_out(1)
        timer 1 action SetVariable("show_main_menu_fade", False)

style main_menu_button:
    properties gui.button_properties("main_menu")

style main_menu_button_text is gui_button_text

style main_menu_button_text:
    properties gui.text_properties("main_menu")
    color gui.interface_text_color
    hover_color gui.hover_color
    text_align 0.0
    xalign 0.0
    font gui.interface_text_font
    outlines [(2, "000000AA", 0, 0)]

style main_menu_vbox is vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    properties gui.text_properties("version")

transform hover_scale:
    anchor (0.5, 0.5)
    rotate 0
    on idle:    
        parallel:
            linear 0.1 xzoom 1.0 yzoom 1.0
    on hover:
        parallel:
            linear 0.1 xzoom 1.1 yzoom 1.1

transform menu_alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform alpha_in(time=0.5):
    alpha 0
    linear time alpha 1

transform alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform jam_logo_transform:
    on hover:
        matrixcolor HueMatrix(0)
        linear 5 matrixcolor HueMatrix(360)
        repeat
