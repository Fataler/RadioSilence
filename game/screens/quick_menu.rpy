## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

image pause_button :
    "gui/Pause_baget.png"
    alpha 0.8

screen quick_menu():

    ## Гарантирует, что оно появляется поверх других экранов.
    zorder 100

    if quick_menu :
        imagebutton:
            idle "pause_button"
            hover At("pause_button", set_bright_hovered(0.1))
            action ShowMenu("pause_menu")
            anchor (1.0, 1.0)
            pos (1.0, 1.0)
        # hbox:
        #     style_prefix "quick"

        #     xalign 0.5
        #     yalign 1.0

        #     #textbutton _("Назад") action Rollback()
        #     textbutton _("История") action ShowMenu('history')
        #     textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
        #     textbutton _("Авто") action Preference("auto-forward", "toggle")
        #     textbutton _("Сохранить") action ShowMenu('save')
        #     textbutton _("Пауза") action ShowMenu('pause_menu')
        #     #textbutton _("Б.Сохр") action QuickSave()
        #     #textbutton _("Б.Загр") action QuickLoad()
        #     #textbutton _("Опции") action ShowMenu('preferences')


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")