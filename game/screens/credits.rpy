define credits_duration = 50#40.0

init python:    
    class Credits(renpy.Displayable):
        def __init__(self, content, duration=credits_duration):
            super(Credits, self).__init__()
            self.content = content
            self.duration = duration
            self.height = 0
            self.time = 0
            self.finished = False
            
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            
            text = Text(self.content, text_align=0.5, size=35, font=gui.interface_text_font)
            text_render = renpy.render(text, width, height, st, at)
            
            self.height = text_render.height + height
            
            speed = (self.height + height) / (self.duration * 1.5)
            
            y = height - (st * speed)

            if y < -text_render.height:
                self.finished = True
                y = -text_render.height 
                
            render.blit(text_render, (width//2 - text_render.width//2, y))
            
            if not self.finished:
                renpy.redraw(self, 0)
            return render

label label_credits:
    call screen credits
    with dissolve
    
    $ quick_menu = False
    #pause
    scene bg_black
    with dissolve

    $ quick_menu = True
    return

screen credits():
    default skip_visible = False
    default skip_fading = False
    default skip_time = 0.0
    default credits_obj = Credits(
"""{image=menu_logo}


{size=65}{i}Команда:{/i}{/size}

{size=45}{b}{k=5}Featharine{/k}{/b}{/size}
лидер
художник
(концепты, покрас спрайтов и ЦГ)


{size=45}{b}{k=5}Kapushishin{/k}{/b}{/size}
режиссёр анимаций
референс-концепт
программист

{size=45}{b}{k=5}LehanFox{/k}{/b}{/size}
фоновик
UI (художник)

{size=45}{b}{k=5}Yelenir{/k}{/b}{/size}
идея новеллы
художник спрайтов и ЦГ (лайн)

{size=45}{b}{k=5}Fataler{/k}{/b}{/size}
программист
редактор
UI (программист)

{size=45}{b}{k=5}Danya Balakhnin{/k}{/b}{/size}
сценарист
звуки и музыка


{size=65}{i}Отдельная
благодарность:{/i}{/size}

{size=45}{b}{k=5}Коты Тигр и Лиса{/k}{/b}{/size}
катание по клавиатуре
моральная поддержка





""")
    layer "master"
    
    fixed:
        xfill True
        yfill True
        at show_screen_transform(show_time=1.0, hide_time=1.0)

        add "menu_bg":
            alpha 0.5
        
        timer (credits_duration * 1.00) action Hide("credits_image")
        
        add credits_obj xalign 0.5

        timer credits_duration + 1 action Show("credits_end")

        # Картинки
        timer (credits_duration * 0.18) action Show("credits_image", img_name="credits_img_1", is_left=True)
        timer (credits_duration * 0.30) action Hide("credits_image")

        timer (credits_duration * 0.34) action Show("credits_image", img_name="credits_img_2", is_left=False)
        timer (credits_duration * 0.46) action Hide("credits_image")

        timer (credits_duration * 0.50) action Show("credits_image", img_name="credits_img_3", is_left=True)
        timer (credits_duration * 0.62) action Hide("credits_image")

        timer (credits_duration * 0.66) action Show("credits_image", img_name="credits_img_4", is_left=False)
        timer (credits_duration * 0.78) action Hide("credits_image")

        timer (credits_duration * 0.82) action Show("credits_image", img_name="credits_img_5", is_left=True)
        timer (credits_duration * 0.94) action Hide("credits_image")

        #Click blocker
        button:
            xfill True
            yfill True
            background None
            mouse "default"
            action [SetScreenVariable("skip_visible", True), SetScreenVariable("skip_fading", False), SetScreenVariable("skip_time", 0.0)]
            hover_sound None
            activate_sound None

        if skip_visible:
            textbutton "Пропустить" action Return() xalign 0.95 yalign 0.05 at (skip_button_fadeout if skip_fading else skip_button_appear)

        if skip_visible and not skip_fading:
            timer 9.5 action SetScreenVariable("skip_fading", True)
            timer 10.0 action [SetScreenVariable("skip_visible", False), SetScreenVariable("skip_fading", False)]


    key "K_RETURN" action If(not skip_visible, [SetScreenVariable("skip_visible", True), SetScreenVariable("skip_fading", False), SetScreenVariable("skip_time", 0.0)], NullAction())  # Enter
    key "K_SPACE" action If(not skip_visible, [SetScreenVariable("skip_visible", True), SetScreenVariable("skip_fading", False), SetScreenVariable("skip_time", 0.0)], NullAction())   # Пробел
    key "K_ESCAPE" action If(not skip_visible, [SetScreenVariable("skip_visible", True), SetScreenVariable("skip_fading", False), SetScreenVariable("skip_time", 0.0)], NullAction()) # Escape
    key "mouseup_3" action If(not skip_visible, [SetScreenVariable("skip_visible", True), SetScreenVariable("skip_fading", False), SetScreenVariable("skip_time", 0.0)], NullAction())  # Правая кнопка мыши

screen credits_end():
    layer "master"

    fixed:
        at credits_thanks()

        text "Спасибо за игру!":
            style "gui_text"
            size 95 
            align (0.5, 0.5)
            color "#ffffff"

    timer 10.0 action Return()

transform credits_thanks:
    subpixel True
    alpha 0.0
    ease 1.0 alpha 1.0

screen credits_image(img_name=None, is_left=True):
    layer "master"
    fixed:
        xfill True
        yfill True
        at show_screen_transform
            
        if img_name:
            $ xpos = 0.01 if is_left else 0.99
            $ trans = credits_left_appear if is_left else credits_right_appear
            add img_name at trans xalign xpos yalign 0.5 xsize 640 ysize 360

transform credits_left_appear:
    subpixel True
    alpha 0.0 xoffset -50
    ease 3 alpha 1.0 xoffset 0

transform credits_right_appear:
    subpixel True
    alpha 0.0 xoffset 50
    ease 3 alpha 1.0 xoffset 0

transform skip_button_appear:
    alpha 0.0
    ease 0.5 alpha 1.0

transform skip_button_fadeout:
    alpha 1.0
    ease 0.5 alpha 0.0
