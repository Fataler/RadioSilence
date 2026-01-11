screen achievements_screen():
    tag menu
    
    use game_menu(_("Достижения"), scroll="viewport"):
        
        vbox:
            spacing 10

            if (config.developer):
                textbutton _("Cброс") action Function(reset_achievements)
                textbutton _("Test") action Function(unlock_achievement, ACHIEVEMENT_ATTACK)
                textbutton _("Unlock All") action Function(unlock_all_achievements)
            
            frame:
                style "achievements_stats_frame"
                
                python:
                    total = len(achievements)
                    unlocked = sum(1 for ach in achievements.values() if ach.unlocked)
                    percentage = (unlocked * 100) // total
                
                vbox:
                    spacing 20
                    xfill True
                    
                    text "Прогресс достижений: [unlocked]/[total] ([percentage]%)" style "achievements_stats_text"
                    
                    bar:
                        value percentage
                        range 100
                        xfill True
                        style "achievements_progress_bar"
            
            python:
                unlocked_achievements = [ach for ach in achievements.values() if ach.unlocked]
                locked_achievements = [ach for ach in achievements.values() if not ach.unlocked]

            if unlocked_achievements:
                text "Полученные достижения:" style "achievements_group_header"
                
                for ach in unlocked_achievements:
                    frame:
                        style "achievement_item_frame"
                        
                        hbox:
                            spacing 10
                            xfill True
                            
                            # Иконка
                            frame:
                                style "achievement_icon_frame"
                                xsize ACHIEVEMENT_ICON_SIZE + 20
                                ysize ACHIEVEMENT_ICON_SIZE + 20
                                
                                add ach.icon:
                                    size (ACHIEVEMENT_ICON_SIZE, ACHIEVEMENT_ICON_SIZE)
                                    fit "contain"
                                    xalign 0.5
                                    yalign 0.5

                            vbox:
                                spacing 40
                                xfill True

                                hbox:
                                    spacing 5
                                    xfill True

                                    frame:
                                        background None
                                        xsize 750
                                        ysize 50
                                        text ach.name style "achievement_name":
                                            xalign 0.0
                                            yalign 0.5

                                    fixed:
                                        xsize 50
                                        ysize 50
                                        xoffset -10
                                        add "check_bg":
                                            xalign 0.5
                                            yalign 0.5
                                        add "check":
                                            xalign 0.5
                                            yalign 0.5

                                text ach.description style "achievement_description"
                            
                    

            if locked_achievements:
                text "Неполученные достижения:" style "achievements_group_header"
                
                for ach in locked_achievements:
                    frame:
                        style "achievement_item_frame"

                        hbox:
                            spacing 10
                            xfill True
                            
                            frame:
                                style "achievement_icon_frame"
                                xsize ACHIEVEMENT_ICON_SIZE + 20
                                ysize ACHIEVEMENT_ICON_SIZE + 20
                                
                                add ach.lock_icon:
                                    size (ACHIEVEMENT_ICON_SIZE, ACHIEVEMENT_ICON_SIZE)
                                    fit "contain"
                                    xalign 0.5
                                    yalign 0.5

                            vbox:
                                spacing 40
                                xfill True

                                hbox:
                                    spacing 5
                                    xfill True

                                    frame:
                                        background None
                                        xsize 750
                                        ysize 50
                                        if ach.hidden:
                                            text "???" style "achievement_name":
                                                xalign 0.0
                                                yalign 0.5
                                        else:
                                            text ach.name style "achievement_name":
                                                xalign 0.0
                                                yalign 0.5

                                    fixed:
                                        xsize 50
                                        ysize 50
                                        xoffset -10

                                        add "check_bg":
                                            xalign 0.5
                                            yalign 0.5

                                if ach.hidden:
                                    text "Секретное достижение" style "achievement_description"
                                else:
                                    text ach.description style "achievement_description"

style achievements_stats_frame:
    background None #Frame("gui/frame.png", 40, 40)
    padding (20, 20)
    margin (0, 0, 0, 20)
    xfill True

style achievements_stats_text is gui_text:
    color gui.interface_text_color
    xalign 0.5
    text_align 0.5

style achievements_progress_bar:
    ysize 40
    left_bar Frame("gui/slider/horizontal_hover_bar.png", 10, 10)
    right_bar Frame("gui/slider/horizontal_idle_bar.png", 10, 10)
    thumb None
    thumb_offset 0
    xalign 0.5

style achievement_item_frame:
    background "#f3f3f334" #Frame("gui/frame.png", 40, 40)
    padding (20, 20)
    xfill True
    margin (0, 0, 0, 10)
    
style achievement_name is gui_text:
    color gui.accent_color
    size 35
    xalign 0.0

style achievement_description is gui_text:
    color gui.text_color
    #size 24
    xalign 0.5

style achievements_group_header is gui_text:
    size 36
    color gui.accent_color

style achievement_popup_frame:
    xalign 1.0
    yalign 0.0
    xsize 800
    background Frame("gui/frame_achievement.png", 80, 40, 80, 40)
    padding (80, 40)

style achievement_popup_title:
    color "#ffffff"
    size 30
    xalign 0.5
    text_align 0.5

style achievement_popup_name:
    color "#ffffff"
    size 35

style achievement_popup_description:
    color gui.text_color
    size 30
    #size 24

style achievement_icon_frame:
    background Frame("gui/frame.png", 10, 10)
    padding (0, 0)
    margin (0, 0)

style achievement_icon:
    xalign 0.5
    yalign 0.5

style achievement_check is gui_text:
    color gui.accent_color
    size 30
    xalign 1.0
    yalign 0.5

screen achievement_popup(achievement):
    modal False
    zorder 100
    style_prefix "achievement_popup"
    
    timer 7 action Hide("achievement_popup")
    
    frame:
        at achievement_popup_appear
        style "achievement_popup_frame"
        xalign 1.0
        yalign 0.1
        
        vbox:
            spacing 20

            hbox:
                xfill True
                text "Получено достижение!" style "achievement_popup_title"
                
            hbox:
                spacing 20
                
                frame:
                    style "achievement_icon_frame"
                    xsize ACHIEVEMENT_POPUP_ICON_SIZE
                    ysize ACHIEVEMENT_POPUP_ICON_SIZE
                    
                    add achievement.icon:
                        size (ACHIEVEMENT_POPUP_ICON_SIZE, ACHIEVEMENT_POPUP_ICON_SIZE)
                        fit "contain"
                        xalign 0.5
                        yalign 0.5
                
                vbox:
                    spacing 10
                    text achievement.name style "achievement_popup_name"
                    text achievement.description style "achievement_popup_description"

transform achievement_popup_appear:
    subpixel True
    xoffset 400
    alpha 0.0
    parallel:
        easein 0.5 xoffset 0
    parallel:
        easein 0.5 alpha 1.0
    pause 5
    parallel:
        easeout 0.5 xoffset 400
    parallel:
        easeout 0.5 alpha 0.0
