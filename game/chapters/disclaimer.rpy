
screen disclaimer():
    tag menu
    modal True
    
    add "bg_black"
    
    vbox:
        align (0.5, 0.5)
        spacing 60
        xsize 1400

        null height 200
        
        text "Эта аниме-игра, сделанная авторами на коленке за 2 недели, не ставит цель отразить реалии войны, но в ней могут содержаться неприятные темы, связанные с этим.\nВ игре присутствует жестокость и некоторые нехорошие вещи.\nАвторы не призывают к политическим и идеологическим идеям и настроениям.\nВсе совпадения случайны.\nЕсли вас триггерит тема войны, то лучше закрыть эту игру, попить чайку и переключиться на что-то расслабляющее, а об этой игре забыть.\nЕсли нет – будет круто, если вам понравится.":
            text_align 0.5
            xalign 0.5
            size 36
            font gui.text_font
            color gui.text_color
            
        vbox:
            at delay_appear(5, 1)

            xalign 0.5
            spacing 20
            
            null height 110

            textbutton _("Продолжить") at hover_shake_y(dy=3, speed=0.5):
                action Return()
                style "confirm_button"
                text_style "confirm_button_text"
                xalign 0.5
                text_size 50
                
            textbutton _("Назад") at hover_shake_x(dx=3, speed=0.5):
                action MainMenu()
                style "confirm_button"
                text_style "confirm_button_text"
                xalign 0.5
                text_size 40

label show_disclaimer:
    scene bg_black
    play sfx "audio/sfx/udar.ogg"
    call screen disclaimer
    return
