## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"
        style "say_window"
                
        fixed:
            xfill True
            yfit True

            vbox:
                spacing 6
                frame:
                    style "say_textframe"
                    text what id "what"

            if who:
                window:
                    style "namebox"
                    text who id "who"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0 zoom 0.9

    # if not (config.developer):
    #     key "mouseup_4" action ShowMenu("history")
    #     key "K_PAGEUP" action ShowMenu("history")


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style say_window:
    subpixel True
    xalign 0.5
    xsize 1280
    align (0.5, 0.98)
    xpadding 10
    ypadding 10
    background Frame(textbox_style, Borders(0,0, 0, 0), tile=False) #textbox_style
    yminimum 240
    xfill False
    yfill False

style namebox:
    subpixel True
    xpos -0.008
    xanchor 0.0
    xminimum 740
    ypos -0.072
    ysize 68
    background Frame("gui/namebox.png", Borders(80, 0, 690, 0), tile=False) #gui/namebox.png
    left_padding 60
    right_padding 490
    #padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign -0.5
    color gui.text_color
    outlines [(2, "000000AA", 0, 0)]

style say_dialogue:
    properties gui.text_properties("dialogue")
    adjust_spacing True
    outlines [(2, "000000AA", 0, 0)]
    
style say_textframe:
    background None
    xfill True
    padding (150, 30, 140, 30)