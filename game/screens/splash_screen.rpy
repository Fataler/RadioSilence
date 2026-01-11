################################################################################
## Сплешскрин
################################################################################
default show_main_menu_fade = False
default splash_duration = 5.0
default debug_splash = False

image disclamer_fon = "gui/splash/disclamer_fon.png"
image disclamer_text:
    "gui/splash/disclamer_text.png"
    align (0.5, 0.5)

image splash_dowen:
    "gui/splash/splash_dowen.png"
    align (0.5, 0.5)

image splash_fon = "gui/splash/splash_fon.png"
image splash_jam:
    "gui/splash/splash_jam.png"
    align (0.5, 0.5)

image splash_sweet:
    "gui/splash/splash_sweet.png"
    align (0.5, 0.5)
        
label splashscreen:

    if not splash_enabled:
        return
    
    scene black
    with Dissolve(1.0)
    play ui sfx_disclamer

    if (persistent.first_start or debug_splash):
        call screen splash_first()

    stop music

    show screen splash_second
    play ui sfx_intro
    $ renpy.pause(8.0, hard=True)
    hide screen splash_second
    with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)

    if persistent.first_start:
        $ persistent.first_start = False
    
    $ show_main_menu_fade = True
    return

screen splash_first():
    style_prefix "splash_screen"

    add "disclamer_fon" at delay_appear(0, 1)

    add "disclamer_text" at delay_appear(1, 1)
    
    vbox:
        at delay_appear(5, 1)
        textbutton "Продолжить" at hover_shake_y(dy=3, speed=0.5):
            text_size 60
            action Return()
        textbutton "Выход" at hover_shake_x(dx=3, speed=0.5):
            text_size 40
            action Quit(confirm=False)

screen splash_second():
    add "splash_fon" at delay_appear(0, 1)
    add "splash_jam" at delay_appear(3.5, 2):
        pos (0.5, 0.7)
    add "splash_dowen" at delay_appear(2.5, 2):
        pos (0.5, 0.6)

    add "splash_sweet" at delay_appear(1, 2):
        pos (0.5, 0.25)

style splash_screen_button is main_menu_button:
    hover_color "#ff0400"
    outlines [(2, "000000AA", 0, 0)]
    xalign 0.5
    yalign 0.5
    subpixel True

style splash_screen_textbutton_text is gui_text:
    text_align 0.5
    xalign 0.5

style splash_screen_vbox is vbox:
    align (0.5, 0.95)
    spacing 15