default _show_hud = False
default _jump_filter = ""

init -999 python:
    def _open_jump():
        renpy.call_in_new_context("_debug_jump_show")

    def _on_filter_change(txt):
        store._jump_filter = txt
        renpy.restart_interaction()

label _debug_jump_show:
    call screen debug_jump
    return

screen debug_jump():
    modal True
    tag debug_jump
    add Solid("#0008")

    $ labels_all = [l for l in renpy.get_all_labels() if not l.startswith("_")]
    $ labels_vis = sorted((l for l in labels_all if _jump_filter.lower() in l.lower()), key=str.lower)

    frame align (0.5, 0.5) padding (18, 18) xmaximum 800 ymaximum 600 background Frame("gui/frame.png", 18, 18):
        vbox spacing 12:
            hbox spacing 8:
                text "Куда прыгнуть?" style "debug_text"
                text "(%d)" % len(labels_all) size 18
            hbox spacing 8:
                text "Фильтр:" style "debug_text"
                input value VariableInputValue("_jump_filter") length 32 changed _on_filter_change
            viewport draggable True mousewheel True:
                vbox spacing 4:
                    textbutton "— Отмена —" action Return()
                    for lb in labels_vis:
                        textbutton lb action [Return(), Jump(lb)]