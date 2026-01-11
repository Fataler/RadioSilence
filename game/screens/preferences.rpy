## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

default mouse_xy = (0, 0)

default persistent.current_font = "default"

init python:
    if persistent.current_font is None:
        persistent.current_font = "default"

    def update_font_size():
        # if (persistent.current_font == "default"):
        #     gui.text_size = 10
        #     style.navigation_button_text.size = 30
        #     #style.navigation_vbox.area = (0, 300, 700, 100)
        # else:
        #     gui.text_size = 10
        #     style.navigation_button_text.size = 10
        #     #style.navigation_vbox.area = (0, 330, 700, 100)
        
        style.rebuild()
        renpy.restart_interaction()

    config.start_callbacks.append(update_font_size)

    def reset_preferences():
        _preferences.set_volume('music', 0.1)
        _preferences.set_volume('sfx', 0.1)
        _preferences.set_volume('voice', config.default_voice_volume if hasattr(config, 'default_voice_volume') else 1.0)

        _preferences.text_cps = config.default_text_cps if hasattr(config, 'default_text_cps') else 40
        _preferences.afm_time = config.default_afm_time if hasattr(config, 'default_afm_time') else 15
        _preferences.font_transform = None
        persistent.current_font = "default"
        _preferences.font_size = 1.0

        if renpy.variant("pc"):
            _preferences.fullscreen = config.default_fullscreen if hasattr(config, 'default_fullscreen') else False

        renpy.style.rebuild()
        renpy.restart_interaction()

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):
        style_prefix "pref"

        vbox:
            xfill True
            xalign 0.5
            spacing 20

            vbox:
                xalign 0.5
                spacing 10
                xsize 900
                label _("{u}Режим экрана{/u}"):
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 30
                    if renpy.variant("pc") or renpy.variant("web"):
                        style_prefix "radio"
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

            vbox:
                xalign 0.5
                spacing 20
                
                label _("{u}Текст{/u}"):
                    xalign 0.5
                
                vpgrid:
                    cols 2
                    rows 2
                    xspacing 250
                    xsize 900
                        
                    text _("Скорость\nтекста"):
                        style "pref_text_label"
                        
                    bar value Preference("text speed"):
                        style "pref_bar"
                        
                    text _("Скорость\nавточтения"):
                        style "pref_text_label"
                        
                        
                    bar value Preference("auto-forward time"):
                        style "pref_bar"

                vbox:
                    xalign 0.5
                    spacing 15
                    
                    label _("{u}Пропускать{/u}"):
                        xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 30
                        style_prefix "check"
                        
                        textbutton _("Прочитанный текст"):
                            action Preference("skip", "seen")
                            
                        textbutton _("Весь текст"):
                            action Preference("skip", "all")

            vbox:
                xalign 0.5
                spacing 20
                
                label _("{u}Звук{/u}"):
                    xalign 0.5
                
                # Слайдеры громкости
                vpgrid:
                    cols 2
                    rows 2
                    xspacing 250
                    yspacing 20
                    xsize 900
                    
                    if config.has_music:
                        text _("Громкость музыки"):
                            style "pref_text_label"
                            
                        bar value Preference("music volume"):
                            style "pref_bar"
                            
                        if config.sample_sound:
                            textbutton _("Тест"):
                                action Play("sound", config.sample_sound)
                                xsize 100
                                    
                    if config.has_sound:
                            text _("Громкость звуков"):
                                style "pref_text_label"
                                
                            bar value Preference("sound volume"):
                                style "pref_bar"
                                
                            if config.sample_sound:
                                textbutton _("Тест"):
                                    action Play("sound", config.sample_sound)
                                    xsize 100
                
                # Кнопка "Без звука"
                if config.has_music or config.has_sound or config.has_voice:
                    vbox:
                        xalign 0.5
                        
                        style_prefix "check"
                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            xalign 0.5

            vbox:
                xalign 0.5
                spacing 20
                
                label _("{u}Специальные возможности{/u}"):
                    xalign 0.5
                
                # Настройки шрифта и контрастности в отдельных строках
                vbox:
                    xalign 0.5
                    spacing 25
                    style_prefix "radio"
                    
                    # Секция шрифта
                    vbox:
                        xalign 0.5
                        spacing 15
                        
                        label _("{u}Шрифт{/u}"):
                            xalign 0.5

                        hbox:
                            xalign 0.5
                            spacing 30
                            
                            textbutton _("Оригинальный"):
                                action [
                                    Preference("font transform", None), 
                                    SetField(persistent, "current_font", "default"),
                                    Function(update_font_size)
                                ]
                                style_suffix "radio_button"

                            textbutton _("DejaVu Sans"):
                                action [
                                    SetField(persistent, "current_font", "dejavusans"),
                                    Function(update_font_size),
                                    Preference("font transform", "dejavusans")
                                ]
                                style_suffix "radio_button"
                                tooltip "Шрифт, используемый в \nRen'Py по умолчанию"
                    
                    # Секция контрастности
                    vbox:
                        xalign 0.5
                        spacing 15
                        
                        label _("{u}Высококонтрастный текст{/u}"):
                            xalign 0.5

                        hbox:
                            xalign 0.5
                            spacing 30
                            
                            textbutton _("Enable"):
                                action Preference("high contrast text", "enable")
                                style_suffix "radio_button"

                            textbutton _("Disable"):
                                action Preference("high contrast text", "disable")
                                style_suffix "radio_button"

    fixed:
        textbutton _("Сброс"):
            style "reset_button"
            action Function(reset_preferences)
            tooltip "Сбросить настройки\nна значения по умолчанию"

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            has frame padding 15,15,15,15
            xalign 0.3
            text tooltip style "tooltip"

transform move_appear(from_x=0, from_y=0, to_x=1588,to_y=588):
    xpos 1368
    ypos 688
    ease 0.5 alpha 1 xpos to_x ypos to_y

init -2 python:
    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()

style pref_label is gui_label
style pref_label_text is gui_label_text

style radio_label is pref_label
style radio_label_text is pref_label_text
style label_bar_text is pref_label_text
style radio_button is gui_button

style radio_button_text is gui_button_text:
    text_align 0.5
    yalign 0.5
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button:
    yalign 0.5
style check_button_text is gui_button_text:
    text_align 0.5
    yalign 0.5
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 10

style pref_label_text:
    yalign 1.0
    font gui.interface_text_font
    color gui.interface_text_color
    text_align 0.5
    size 42

style label_bar_text:
    color gui.interface_text_color
    font gui.interface_text_font
    text_align 0.5
    yalign 0.5

style settings_text is label_bar_text:
    size 30
    bold False

style pref_vbox:
    xsize 900

style pref_section_vbox:
    spacing 20
    xalign 0.5

style pref_control_hbox:
    spacing 40
    xalign 0.5
    xsize 800

style pref_bar is gui_bar:
    xsize 380
    yalign 0.5

style pref_text_label is settings_text:
    xsize 280
    text_align 0.0
    yalign 0.5

style tooltip:
    size 35
    font gui.interface_text_font
    color "#f4e5d0"

style reset_button:
    anchor (1.0, 0.5)
    xpos gui.navigation_xpos
    yalign 0.0
    yoffset 45