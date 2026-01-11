init python:
    def cutscene_callback(event, interact=True, **kwargs):
        if event == "end" and interact:
            renpy.hide_screen("say_window")

style cutscene_say_window is say_window
style cutscene_dialogue is say_dialogue

style cutscene_say_window:
    background None#"#ff0000"
    xalign 0.5
    yalign gui.textbox_yalign
    xsize 1820
    yminimum 180
    xfill False
    yfill False
    xpadding 40
    ypadding 10

style cutscene_dialogue:
    properties gui.text_properties("dialogue")
    size 50
    xalign 0.5
    text_align 0.5
    outlines [(3, "#000000CC", 0, 0)]
    xmaximum 1700 
    color "#ffffff"

define cutscene = Character(
    None,
    what_style="cutscene_dialogue",
    window_style="cutscene_say_window",
    callback=cutscene_callback
)


