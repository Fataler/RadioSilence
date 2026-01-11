## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():
    
    add "menu_drop" at menu_board_drop:
        xpos 150
        
    vbox at menu_items_appear:
        style_prefix "navigation"

        spacing gui.navigation_spacing
        
        if main_menu:
            textbutton _("Начать") action Start()
        else:
            textbutton _("История") action ShowMenu("history")
            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")
        
        textbutton _("Достижения") action ShowMenu("achievements_screen")

        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("Завершить повтор") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about") #Function(unlock_achievement, THANK_YOU),

        if renpy.variant("pc"):
            textbutton _("Выход") action Quit(confirm=not main_menu)

style navigation_vbox :
    area (0, 300, 700, 100)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    xminimum 400
    xalign 0.5

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    color gui.text_color
    hover_color gui.accent_color
    size 70
    xalign 0.5

transform menu_board_drop:
    ypos -900
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.2 ypos 0

transform menu_board_up:
    ypos 0
    parallel:
        linear 0.3 ypos -50
        linear 0.2 ypos 0
        linear 0.5 ypos -900

transform menu_items_appear:
    alpha 0.0
    pause 0.7
    easein 0.3 alpha 1.0

transform menu_items_disappear:
    alpha 1.0
    linear 0.3 alpha 0.0