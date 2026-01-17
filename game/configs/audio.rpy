# Музыка
define music_main_theme = "audio/bg/foot290_02-iliaque-singularite.mp3"
define music_experimental_android_work_06 = "audio/bg/foot280_02-ish10_yow1r0-experimental_android_work_06.mp3"
define music_overthrive_uncharted_realms = "audio/bg/foot291_05-overthrive-uncharted_realms.mp3"
define music_ashes = "audio/bg/foot284_04-deep_intruder-ashes.mp3"
define music_p5 = "audio/bg/foot167_06-zmg-p5.mp3"
define music_23_peak = "audio/bg/foot037_01-qx55-23_peak.mp3"
define music_casasoso = "audio/bg/foot037_08-qx55-casasoso.mp3"
define music_atmosphere = "audio/bg/foot040_01-wshgaukd-atmosphere.mp3"
define music_after_all = "audio/bg/foot037_11-qx55-after_all.mp3"

# Игра

# Интерфейс
define sfx_ui_click = "audio/sfx/switch.wav"#"audio/sfx/shelk_knock.ogg"
define sfx_ui_over = "audio/sfx/UI 03 Over.ogg"
define sfx_ui_shelk = "audio/sfx/switch.wav"

# каналы
init python:
    renpy.music.register_channel("ui", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx3", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("music2", mixer="music", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
