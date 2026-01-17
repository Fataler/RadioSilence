# Музыка
define music_main_theme = "audio/bg/foot290_02-iliaque-singularite.mp3"
define music_experimental_android_work_06 = "audio/bg/foot280_02-ish10_yow1r0-experimental_android_work_06.mp3"
define music_overthrive_uncharted_realms = "audio/bg/foot291_05-overthrive-uncharted_realms.mp3"

# Игра

# Интерфейс
define sfx_ui_achieve = "audio/sfx/UI 01 Achive.ogg"
define sfx_ui_click = "audio/sfx/UI 02 Click.ogg"
define sfx_ui_over = "audio/sfx/UI 03 Over.ogg"

# каналы
init python:
    renpy.music.register_channel("ui", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx3", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("music2", mixer="music", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
