## Экран главного меню
transform menu_move_back(from_game_menu=False):
    xoffset (-390 if from_game_menu else 0)
    alpha (0.0 if not from_game_menu else 1.0)
    pause 0.3
    parallel:
        ease 0.5 xoffset 0
    parallel:
        ease 0.5 alpha 1.0

screen main_menu(from_game_menu=False):
    tag menu

    $ elements_apperar_time = 2.0 if not from_game_menu else 1.0

    add "bg_black"


    textbutton "Игра создана в рамках Капелла Jam 3 2026":
        at jam_logo_transform, delay_appear(1, elements_apperar_time)
        pos (0.5, 0.87)
        text_size 40
        text_align 0.5
        action OpenURL(URL_JAM)
        hover_mouse "inspect"

    style_prefix "main_menu"

    vbox at delay_appear(1, elements_apperar_time):
        spacing 10
        align (0.92, 0.75)
    
        textbutton _("Начать") action Start():
            text_size 90

        textbutton _("Загрузить") action ShowMenu("load"):
            text_size 55
            
        
        textbutton _("Достижения") action ShowMenu("achievements_screen"):
            text_size 55

        textbutton _("Настройки") action ShowMenu("preferences"):
            text_size 55

        textbutton _("Об игре") action [ShowMenu("about")]:
            text_size 55

        if renpy.variant("pc"):
            textbutton _("Выход") action Quit(confirm=not main_menu):
                text_size 50

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
