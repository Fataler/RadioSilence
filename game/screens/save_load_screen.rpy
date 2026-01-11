## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

define save_type = _("Сохранить")
define load_type = _("Загрузить")

screen save():

    tag menu

    use file_slots(save_type)


screen load():

    tag menu

    use file_slots(load_type)


screen file_slots(title):
    on "show" action FilePage(1)

    default page_name_value = FilePageNameInputValue(pattern=_("Сохранения"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"), default=False)

    use game_menu(title):

        fixed:

            ## Это гарантирует, что ввод будет принимать enter перед остальными
            ## кнопками.
            order_reverse True

            ## Номер страницы, который может быть изменён посредством клика на
            ## кнопку.
            label title style "page_label"

            ## Таблица слотов.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пусто")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Кнопки для доступа к другим страницам.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    # textbutton _("<=") action FilePagePrevious()
                    # key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave and title == load_type:
                        textbutton _("{#auto_page}Авто") action FilePage("auto")

                    if config.has_quicksave and title == load_type:
                        textbutton _("{#quick_page}Быстрые") action FilePage("quick")

                    ## range(1, 2) задаёт диапазон значений от 1 до 2.
                    if title == load_type:
                        for page in range(1, max_save_pages + 1):
                            textbutton "Основные" action FilePage(page)

                    # textbutton _("=>") action FilePageNext(max = max_save_pages)
                    # key "save_page_next" action FilePageNext(max = max_save_pages)

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Загрузить Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Скачать Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label:
    xalign 0.5
style page_label_text is gui_label_text:
    xalign 0.5

style page_button is gui_button
style page_button_text is gui_button_text:
    size 40

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:
    size 30
    #color gui.text_color
    #hover_color "#FFF"

style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")
    yoffset 20

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675