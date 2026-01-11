################################################################################
## Экран паузы
################################################################################

init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu(from_game_menu=False):
    on "show" action Function(pause_sfx, True)
    on "hide" action Function(pause_sfx, False)

    tag menu

    $ elements_apperar_time = 2.0 if not from_game_menu else 1.0
    
    add "bg_black"

    frame:
        style_prefix "pause_menu"
        background None #"#00000080"
        xanchor 0.5
        xpos 0.83

        # Кнопки меню
        vbox at pause_menu_items_appear:
            spacing 30
            xalign 0.5
            yalign 0.5
            yfit True
            first_spacing 150

            text "ПАУЗА" size 120 xalign 0.5 color gui.accent_color style "pause_menu_button_text"
            
            textbutton _("Сохранить") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("save")]
            textbutton _("Загрузить") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("load")]
            textbutton _("История") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("history")]
            textbutton _("Настройки") action [SetVariable("came_from_pause_menu", True), Hide("pause_menu"), ShowMenu("preferences")]
            textbutton _("Главное меню") action MainMenu()
            textbutton _("Вернуться") action Return()

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