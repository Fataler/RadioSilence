image bg_radio = "images/Radio/Racia.png"
image noise = "images/Radio/Noise.png"

screen radio_screen(char_img, xposNoise=1234, xoffsetRadio=0, noise = 1.0, jitter = 0.01, z = 1.03):
    tag radio_ui
    
    fixed:
        at screen_fade_effect(0.3)
        
        fixed:
            xpos xposNoise ypos 339
            xsize 360 ysize 190

            python:
                tint_color = (0.5, 1.0, 0.5)
                
                noise_lvl = noise
                jitter_lvl = jitter
            
            add "noise":
                align (0.5, 0.5)
                yoffset -11
                xoffset -10
                zoom z
                at radio_crt_effect(
                    tint=tint_color, 
                    noise=noise_lvl, 
                    jitter=jitter_lvl,
                    curvature=0.0
                )

            add char_img:
                align (0.5, 0.5)
                zoom 0.6
                at radio_crt_effect(
                    tint=tint_color, 
                    noise=noise_lvl, 
                    jitter=jitter_lvl,
                    curvature=0.08
                )

        add "bg_radio" alpha 1.0:
            xoffset xoffsetRadio


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
