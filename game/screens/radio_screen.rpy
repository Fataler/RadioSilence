image bg_radio = "images/Radio/Racia.png"
image noise = "images/Radio/Noise.png"

transform radio_content_animation:
    on show:
        alpha 0.0
        pause 0.5
        linear 0.5 alpha 1.0
    on replace:
        alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform radio_bg_animation:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on replace:
        alpha 1.0
    on hide:
        pause 0.5
        linear 0.5 alpha 0.0

screen radio_screen(char_img, xoffsetRadio=0, ypos=0, noise=1.0, jitter=0.01, z=1.03):
    tag radio_ui
    
    python:
        tint_color = (0.5, 1.0, 0.5)
        
        noise_part = At(
            Transform("noise", align=(0.5, 0.5), yoffset=-11, xoffset=-9, zoom=z),
            radio_crt_effect(tint=tint_color, noise=noise, jitter=jitter, curvature=0.0)
        )
        
        char_part = At(
            Transform(char_img, align=(0.5, 0.5), zoom=0.6),
            radio_crt_effect(tint=tint_color, noise=noise, jitter=jitter, curvature=0.08), 
            radio_content_animation
        )
        
        fixed_content = Fixed(noise_part, char_part, xsize=360, ysize=190)
        content = AlphaMask(fixed_content, "images/Radio/noise.png")

    fixed:
        at radio_bg_animation
        xpos xoffsetRadio ypos ypos
        
        add content:
            xpos 1225 ypos 328
            zoom 1.05

        add "bg_radio"


label test_radio:
    scene bg_ulitsa
    
    show screen radio_screen("e_radio")
    "Эхо"
    
    show screen radio_screen("r_radio")
    "Рэйзор"
    
    show screen radio_screen("n_radio")
    "Нектар"
    
    show screen radio_screen("l_radio")
    "Леон-2"
    
    show screen radio_screen("b_radio man")
    "Штаб"
    
    hide screen radio_screen
    "Рация скрыта."
    return
