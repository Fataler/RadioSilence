## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    predict False

    use game_menu(_("История"), scroll=("viewport"), yinitial=1.0, spacing=gui.history_spacing):
        style_prefix "history"

        for h in _history_list:
            window:
                has vbox
                spacing 10

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                $ what = what.replace("…", "...")
                $ what = what.replace("—", "-")
                $ what = what.replace("–", "-") 
                $ what = what.replace("№", "#")
                text what:
                    style "history_text"
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")

## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    #xfill True
    ysize None
    padding (10, 20)

style history_name:
    xpos 0
    xsize 200
    xalign 0

style history_text:
    xpos 70
    xsize 850
    size 40

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    size 40

style history_label:
    xfill True

style history_label_text:
    xalign 0.5