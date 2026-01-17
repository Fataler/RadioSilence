## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

image nastroiki_bg = "gui/settings/nastroiki0.jpg"
image muzyka_100 = "gui/settings/muzyka-100.png"
image muzyka_80 = "gui/settings/muzyka-80.png"
image muzyka_65 = "gui/settings/muzyka-65.png"
image muzyka_50 = "gui/settings/muzyka-50.png"
image muzyka_40 = "gui/settings/muzyka-40.png"
image muzyka_25 = "gui/settings/muzyka-25.png"
image muzyka_0 = "gui/settings/muzyka-0.png"
image zvuki_100 = "gui/settings/zvuki-100.png"
image zvuki_80 = "gui/settings/zvuki-80.png"
image zvuki_65 = "gui/settings/zvuki-65.png"
image zvuki_50 = "gui/settings/zvuki-50.png"
image zvuki_40 = "gui/settings/zvuki-40.png"
image zvuki_25 = "gui/settings/zvuki-25.png"
image zvuki_0 = "gui/settings/zvuki-0.png"
image skorost_teksta_100 = "gui/settings/skorost-teksta-100.png"
image skorost_teksta_80 = "gui/settings/skorost-teksta-80.png"
image skorost_teksta_65 = "gui/settings/skorost-teksta-65.png"
image skorost_teksta_50 = "gui/settings/skorost-teksta-50.png"
image skorost_teksta_40 = "gui/settings/skorost-teksta-40.png"
image skorost_teksta_25 = "gui/settings/skorost-teksta-25.png"
image skorost_teksta_0 = "gui/settings/skorost-teksta-0.png"
image skorost_chteniya_100 = "gui/settings/skorost-achteniya-100.png"
image skorost_chteniya_80 = "gui/settings/skorost-achteniya-80.png"
image skorost_chteniya_65 = "gui/settings/skorost-achteniya-65.png"
image skorost_chteniya_50 = "gui/settings/skorost-achteniya-50.png"
image skorost_chteniya_40 = "gui/settings/skorost-achteniya-40.png"
image skorost_chteniya_25 = "gui/settings/skorost-achteniya-25.png"
image skorost_chteniya_0 = "gui/settings/skorost-achteniya-0.png"
image kontrast_vykl = "gui/settings/kontrast-vykl.png"
image kontrast_vkl = "gui/settings/kontrast-vkl.png"
image shrift_kastomn = "gui/settings/shrift-kastomn.png"
image shrift_orig = "gui/settings/shrift-orig.png"
image bezzvuka_vykl = "gui/settings/bezzvuka-vykl.png"
image bezzvuka_vkl = "gui/settings/bezzvuka-vkl.png"
image propusk_teksta_ves_tekst = "gui/settings/propusk-teksta-ves-tekst.png"
image propusk_teksta_prochit = "gui/settings/propusk-teksta-prochit.png"
image rezhim_ekrana_polnyi = "gui/settings/rezhim-ekrana-polnyi.png"
image rezhim_ekrana_okno = "gui/settings/rezhim-ekrana-okno.png"
image knopka_nazad = "gui/settings/knopka-nazad.png"

init -5 python:
    music_values = [
        {"value": 0.0, "image": "muzyka_0"},
        {"value": 0.25, "image": "muzyka_25"},
        {"value": 0.4, "image": "muzyka_40"},
        {"value": 0.5, "image": "muzyka_50"},
        {"value": 0.65, "image": "muzyka_65"},
        {"value": 0.8, "image": "muzyka_80"},
        {"value": 1.0, "image": "muzyka_100"},
    ]

    sound_values = [
        {"value": 0.0, "image": "zvuki_0"},
        {"value": 0.25, "image": "zvuki_25"},
        {"value": 0.4, "image": "zvuki_40"},
        {"value": 0.5, "image": "zvuki_50"},
        {"value": 0.65, "image": "zvuki_65"},
        {"value": 0.8, "image": "zvuki_80"},
        {"value": 1.0, "image": "zvuki_100"},
    ]

    text_speed_values = [
        {"value": 0.1, "image": "skorost_teksta_0"},
        {"value": 0.25, "image": "skorost_teksta_25"},
        {"value": 0.4, "image": "skorost_teksta_40"},
        {"value": 0.5, "image": "skorost_teksta_50"},
        {"value": 0.65, "image": "skorost_teksta_65"},
        {"value": 0.8, "image": "skorost_teksta_80"},
        {"value": 0.0, "image": "skorost_teksta_100"},
    ]

    auto_read_speed_values = [
        {"value": 0.0, "image": "skorost_chteniya_0"},
        {"value": 0.25, "image": "skorost_chteniya_25"},
        {"value": 0.4, "image": "skorost_chteniya_40"},
        {"value": 0.5, "image": "skorost_chteniya_50"},
        {"value": 0.65, "image": "skorost_chteniya_65"},
        {"value": 0.8, "image": "skorost_chteniya_80"},
        {"value": 0.99, "image": "skorost_chteniya_100"},
    ]

    contrast_values = [
        {"value": False, "image": "kontrast_vykl"},
        {"value": True, "image": "kontrast_vkl"},
    ]

    font_values = [
        {"value": "renpy_default", "image": "shrift_orig"},
        {"value": "our_custom", "image": "shrift_kastomn"},
    ]

    mute_values = [
        {"value": False, "image": "bezzvuka_vykl"},
        {"value": True, "image": "bezzvuka_vkl"},
    ]

    skip_text_values = [
        {"value": False, "image": "propusk_teksta_prochit"},
        {"value": True, "image": "propusk_teksta_ves_tekst"},
    ]

    screen_mode_values = [
        {"value": False, "image": "rezhim_ekrana_okno"},
        {"value": True, "image": "rezhim_ekrana_polnyi"},
    ]

    def get_closest_pref_image(values_list, current_value):
        if not values_list:
            return None
        min_diff = float('inf')
        best_img = None
        for d in values_list:
            v = d["value"]
            if isinstance(v, (int, float)) and isinstance(current_value, (int, float)):
                diff = abs(v - current_value)
            else:
                diff = 0 if v == current_value else 1
            if diff < min_diff:
                min_diff = diff
                best_img = d["image"]
        return best_img

    def get_pref_image(values_list, current_value):
        if not values_list:
            return None
        for d in values_list:
            if d["value"] == current_value:
                return d["image"]
        return None

    def cycle_pref_value(values_list, getter, setter):
        current_val = getter()
        nearest_idx = 0
        min_diff = float('inf')
        for i, d in enumerate(values_list):
            v = d["value"]
            if isinstance(v, (int, float)) and isinstance(current_val, (int, float)):
                diff = abs(v - current_val)
            else:
                diff = 0 if v == current_val else 1
            if diff < min_diff:
                min_diff = diff
                nearest_idx = i
        new_idx = (nearest_idx + 1) % len(values_list)
        setter(values_list[new_idx]["value"])
        renpy.restart_interaction()

default persistent.current_font = "our_custom"
default persistent.high_contrast = False

init python:
    def get_music_vol(): 
        return _preferences.get_volume('music')

    def get_sound_vol(): 
        return _preferences.get_volume('sfx')

    def get_auto_speed():
        return 1.0 - (float(_preferences.afm_time) / 30.0)

    def get_text_cps(): 
        return _preferences.text_cps / 100.0

    def get_mute(): 
        return _preferences.get_mute('music')

    def get_fullscreen(): 
        return _preferences.fullscreen

    def get_skip(): 
        return _preferences.skip_unseen

    def get_font(): 
        return persistent.current_font
    
    def get_contrast(): 
        return persistent.high_contrast

    def set_music_vol(v): 
        _preferences.set_volume('music', v)

    def set_sound_vol(v):
        _preferences.set_volume('sfx', v)

    def set_auto_speed(v):
        _preferences.afm_time = (1.0 - v) * 30.0
        renpy.restart_interaction()

    def set_text_cps(v): 
        _preferences.text_cps = int(v * 100) if v > 0 else 0

    def set_mute(v):
        _preferences.set_mute('music', v)
        _preferences.set_mute('sfx', v)
        _preferences.set_mute('voice', v)

    def set_fullscreen(v): 
        _preferences.fullscreen = v

    def set_skip(v): 
        _preferences.skip_unseen = v

    def set_font(v): 
        persistent.current_font = v
        if v == "our_custom":
            _preferences.font_transform = None
        elif v == "renpy_default":
            _preferences.font_transform = "dejavusans"
        
        style.rebuild()
        renpy.restart_interaction()

        notification_text = ""
        if v == "our_custom":
            notification_text = "Установлен кастомный шрифт"
        elif v == "renpy_default":
            notification_text = "Установлен шрифт Ren'Py по умолчанию"

        renpy.notify(notification_text)

    def set_contrast(v): 
        persistent.high_contrast = v
        _preferences.high_contrast = v
        style.rebuild()
        renpy.restart_interaction()

        notification_text = ""

        if v:
            notification_text = "Теперь текст будет отображаться с черной подложкой"
        else:
            notification_text = "Теперь текст будет отображаться без черной подложки"

        renpy.notify(notification_text)

    def update_font_size():
        if persistent.current_font == "our_custom" and _preferences.font_transform is None:
            _preferences.font_transform = None
        else:
            _preferences.font_transform = "dejavusans"
        
        style.rebuild()
        renpy.restart_interaction()

    config.start_callbacks.append(update_font_size)

    def reset_preferences():
        set_music_vol(0.5)
        set_sound_vol(0.5)
        set_text_cps(0.4)
        set_auto_speed(0.5)
        set_mute(False)
        set_fullscreen(False)
        set_skip(False)
        set_font("default")
        set_contrast(False)
        renpy.style.rebuild()
        renpy.restart_interaction()

screen preferences():
    tag menu

    add "nastroiki_bg"

    # Current states visuals
    $ music_img = get_closest_pref_image(music_values, get_music_vol())
    if music_img:
        add music_img
    
    $ sound_img = get_closest_pref_image(sound_values, get_sound_vol())
    if sound_img:
        add sound_img

    $ auto_img = get_closest_pref_image(auto_read_speed_values, get_auto_speed())
    if auto_img:
        add auto_img

    $ text_img = get_closest_pref_image(text_speed_values, get_text_cps())
    if text_img:
        add text_img

    $ mute_img = get_pref_image(mute_values, get_mute())
    if mute_img:
        add mute_img

    $ skip_img = get_pref_image(skip_text_values, get_skip())
    if skip_img:
        add skip_img

    $ screen_img = get_pref_image(screen_mode_values, get_fullscreen())
    if screen_img:
        add screen_img

    $ font_img = get_pref_image(font_values, get_font())
    if font_img:
        add font_img

    $ contrast_img = get_pref_image(contrast_values, get_contrast())
    if contrast_img:
        add contrast_img

    style_prefix "pref_hotspot"
    
    # Display Mode
    button area (112, 590, 268, 350) action Function(cycle_pref_value, screen_mode_values, get_fullscreen, set_fullscreen)

    # Skip Text
    button area (403, 600, 333, 350) action Function(cycle_pref_value, skip_text_values, get_skip, set_skip)

    # Mute
    button area (755, 600, 251, 350) action Function(cycle_pref_value, mute_values, get_mute, set_mute)

    # Font
    button area (1035, 600, 289, 350) action Function(cycle_pref_value, font_values, get_font, set_font)

    # Contrast
    button area (1364, 600, 259, 350) action Function(cycle_pref_value, contrast_values, get_contrast, set_contrast)

    # Blocks for speeds and volumes
    button area (104, 296, 314, 280) action Function(cycle_pref_value, auto_read_speed_values, get_auto_speed, set_auto_speed)
    button area (426, 286, 349, 300) action Function(cycle_pref_value, text_speed_values, get_text_cps, set_text_cps)
    button area (782, 271, 376, 326) action Function(cycle_pref_value, sound_values, get_sound_vol, set_sound_vol)
    button area (1185, 237, 451, 350) action Function(cycle_pref_value, music_values, get_music_vol, set_music_vol)

    # Back
    imagebutton:
        idle "knopka_nazad"
        hover At("knopka_nazad", set_bright_hovered(0.1))
        action Return()
        align (0.95, 0.95)
        focus_mask True