## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    fixed:
        at screen_fade_effect(0.5)

        style_prefix "choice"

        vbox:
            for i in items:            
                textbutton i.caption:
                    action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound sfx_ui_over
    activate_sound sfx_ui_click

style choice_button_text is default:
    properties gui.text_properties("choice_button")