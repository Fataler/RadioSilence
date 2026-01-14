################################################################################
## Сплешскрин
################################################################################
init -2 python:
    renpy.music.register_channel("video", loop=False, stop_on_mute=True, tight=False, movie=True)
    renpy.music.register_channel("video_ch", "video", loop=False, stop_on_mute=True, tight=False, movie=True)

default show_main_menu_fade = False

init:
    image logo_jam = Movie(channel='video_ch', play="video/jam4.ogv", loops=0, stop_music=True)

screen logo_jam():
    add "logo_jam"
        
label splashscreen:

    $ quick_menu = False

    if not splash_enabled:
        return

    if not renpy.variant("pc"):
        return

    scene black
    with Dissolve(1.0)

    stop music
    scene bg_white

    $ renpy.music.set_volume(0.5, channel='video_ch')  

    show screen logo_jam

    if persistent.first_start:
        $renpy.pause(4.85, hard=True)
    else:
        $renpy.pause(4.85)

    $renpy.music.stop(channel='video_ch', fadeout=None)
    hide screen logo_jam
    
    if persistent.first_start:
        $persistent.first_start = False
    
    $ show_main_menu_fade = True
    return