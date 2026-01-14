#region characters
define E = Character("Эхо", image="e")
define E_t = Character(None, image="r")
define E_f = Character("Эхо", image="e_f")
define R = Character("Рэйзор", image="r")
define R_side = Character("Рэйзор", image="r_side")
define N = Character("Нектар", image="n")
define N_side = Character("Нектар", image="n_side")
define S = Character("Стальной", image="s")
define S_side = Character("Стальной", image="s_side")
define CH = Character("Стальной", image="s")
define L = Character("Леон-2", image="l")
define L_side = Character("Леон-2", image="l_side")
define B = Character("Штаб", image="b")
define story_teller = Character(None, kind=nvl, color="#1a1a1f")

#универсальный перс
init python:
    def speak_as(name, text, color="#ffffff"):
        Character(name, color=color)(text)

#картинка для рации штаба
image b_side = LayeredImageProxy("b", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60))

#endregion

#region Эхо

image side e = LayeredImageProxy("e_f", Transform(crop=(0, 0, 800, 550), yoffset=85, zoom=1.0))
image e_radio = LayeredImageProxy("e_f", Transform(crop=(0, 0, 800, 550), yoffset=85, zoom=1.0))

layeredimage e_f:

    at auto_flip("e_f", "right")

    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute tired default:
            Null()
        attribute thinking:
            Null()
        attribute base:
            Null()
        attribute ear:
            Null()

    group emotion if_any "tired":
        attribute idle default:
            "images/Sprites/Exo/Exo_tired_idle.png"
        attribute surprised:
            "images/Sprites/Exo/Exo_tired_surprised.png"

    group emotion if_any "thinking":
        xoffset -40
        yoffset 10
        attribute smile default:
            "images/Sprites/Exo/Exo_thinking_smile.png"
        attribute happy:
            "images/Sprites/Exo/Exo_thinking_happy.png"

    group emotion if_any "base":
        xoffset 10
        yoffset 10
        attribute annoyed default:
            "images/Sprites/Exo/Exo_base_annoyed.png"
        attribute sad:
            "images/Sprites/Exo/Exo_base_sad.png"
    
    group emotion if_any "ear":
        xoffset -40
        yoffset 10
        attribute think:
            "images/Sprites/Exo/Exo_ear_think.png"
        attribute asharashen:
            "images/Sprites/Exo/Exo_ear_asharashen.png"

#endregion

#region Рэйзор
layeredimage r:
    zoom 1.1
    at auto_flip("r", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute stretching default:
            Null()
        attribute seriously:
            Null()
        attribute base:
            Null()

    group emotion if_any "stretching":
        attribute dissatisfied default:
            "images/Sprites/Razer/Razer_stretching_dissatisfied.png"
        attribute mad:
            "images/Sprites/Razer/Razer_stretching_mad.png"
        attribute rage:
            "images/Sprites/Razer/Razer_stretching_rage.png"            

    group emotion if_any "seriously":
        attribute happy:
            "images/Sprites/Razer/Razer_seriously_happy.png"
        attribute idle default:
            "images/Sprites/Razer/Razer_seriously_idle.png"
        attribute serious:
            "images/Sprites/Razer/Razer_seriously_serious.png"

    group emotion if_any "base":
        zoom 0.95
        attribute sad:
            "images/Sprites/Razer/Razer_base_sad.png"
        attribute smile default:
            "images/Sprites/Razer/Razer_base_smile.png"
        attribute surprised:
            "images/Sprites/Razer/Razer_base_surprised.png"
        attribute asharashen:
            "images/Sprites/Razer/Razer_base_asharashen.png"

image side r_side = LayeredImageProxy("r", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=100, zoom=0.8, xzoom=-1.0))
image r_radio = LayeredImageProxy("r", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=100))
#endregion

#region Нектар
layeredimage n:
    zoom 0.8
    at auto_flip("n", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute base default:
            Null()
        attribute hands:
            Null()
        attribute hand_hide:
            Null()

    group emotion if_any "base":
        attribute idle default:
            "images/Sprites/Nektar/Nektar_base_idle.png"
        attribute smile:
            "images/Sprites/Nektar/Nektar_base_smile.png"
        attribute serious:
            "images/Sprites/Nektar/Nektar_base_serious.png"            

    group emotion if_any "hands":
        attribute sad:
            "images/Sprites/Nektar/Nektar_hands_sad.png"
        attribute relief default:
            "images/Sprites/Nektar/Nektar_hands_relief.png"
        attribute fear:
            "images/Sprites/Nektar/Nektar_hands_fear.png"

    group emotion if_any "hand_hide":
        xoffset -30
        attribute shy:
            "images/Sprites/Nektar/Nektar_hand_hide_shy.png"
        attribute surprised default:
            "images/Sprites/Nektar/Nektar_hand_hide_surprised.png"

image side n_side = LayeredImageProxy("n", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60, zoom=0.8, xzoom=-1.0))
image n_radio = LayeredImageProxy("n", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60))

# image s_radio = LayeredImageProxy("s", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60))

#endregion

#region Леон-2
layeredimage l:
    zoom 0.95
    at auto_flip("l", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute thinking default:
            Null()
        attribute closed:
            Null()
        attribute half_closed:
            Null()

    group emotion if_any "thinking":
        attribute idle default:
            "images/Sprites/Leon2/Leon2_thinking_idle.png"
        attribute sad:
            "images/Sprites/Leon2/Leon2_thinking_sad.png"
        attribute embarrassed:
            "images/Sprites/Leon2/Leon2_thinking_embarrassed.png"            

    group emotion if_any "closed":
        xoffset 70
        attribute shy:
            "images/Sprites/Leon2/Leon2_closed_shy.png"
        attribute serious default:
            "images/Sprites/Leon2/Leon2_closed_serious.png"
        attribute smile:
            "images/Sprites/Leon2/Leon2_closed_smile.png"

    group emotion if_any "half_closed":
        xoffset 90
        attribute surprised default:
            "images/Sprites/Leon2/Leon2_half_closed_surprised.png"

image side l_side = LayeredImageProxy("l", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60, zoom=0.8, xzoom=-1.0))
image l_radio = LayeredImageProxy("l", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60))
#endregion

#region Стальной
layeredimage s:
    at auto_flip("s", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute radio default:
            Null()
        attribute explain:
            Null()
        attribute handsome:
            Null()

    group emotion if_any "radio":
        attribute idle default:
            "images/Sprites/Leon2/Leon2_thinking_idle.png"
        attribute evil:
            "images/Sprites/Leon2/Leon2_thinking_sad.png"
        attribute thinking:
            "images/Sprites/Leon2/Leon2_thinking_embarrassed.png"            
        attribute surprised:
            "images/Sprites/Leon2/Leon2_thinking_embarrassed.png" 

    group emotion if_any "explain":
        xoffset 70
        attribute smile:
            "images/Sprites/Leon2/Leon2_closed_shy.png"
        attribute serious default:
            "images/Sprites/Leon2/Leon2_closed_serious.png"
        attribute happy:
            "images/Sprites/Leon2/Leon2_closed_smile.png"

    group emotion if_any "handsome":
        xoffset 90
        attribute sad default:
            "images/Sprites/Leon2/Leon2_half_closed_surprised.png"
        attribute smug default:
            "images/Sprites/Leon2/Leon2_half_closed_surprised.png"
        attribute annoyed default:
            "images/Sprites/Leon2/Leon2_half_closed_surprised.png"

image s_side = LayeredImageProxy("s", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60, zoom=0.8, xzoom=-1.0))
image s_radio = LayeredImageProxy("s", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60))
#endregion

#region Штаб

image side b_side = LayeredImageProxy("b", Transform(crop=(0, 0, 800, 550), yoffset=85, zoom=1.0))
image b_radio = LayeredImageProxy("b", Transform(crop=(0, 0, 800, 550), yoffset=85, zoom=1.0))

layeredimage b:

    at auto_flip("b", "right")

    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute base default:
            Null()
        attribute man:
            Null()

    group emotion if_any "base":
        attribute idle default:
            "images/Sprites/Base/base_racia.png"

    group emotion if_any "man":
        attribute idle default:
            "images/Sprites/Base/man_racia.png"

#endregion