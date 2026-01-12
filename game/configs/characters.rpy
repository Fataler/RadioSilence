#region characters
define E = Character("Эхо", image="e")
define E_t = Character(None, image="r")
define E_f = Character("Эхо", image="e_f")
define R = Character("Рэйзор", image="r")
define N = Character("Нектар", image="n")
define S = Character("Стальной", image="s")
define L = Character("Леон-2", image="l")
define B = Character("Штаб")
define story_teller = Character(None, kind=nvl, color="#1a1a1f")

#универсальный перс
init python:
    def speak_as(name, text, color="#232324"):
        Character(name, color=color)(text)

#endregion

#region Эхо

image side e = LayeredImageProxy("e_f", Transform(crop=(0, 0, 800, 550), yoffset=80, zoom=1.0))

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
        attribute smile default:
            "images/Sprites/Exo/Exo_thinking_smile.png"
        attribute happy:
            "images/Sprites/Exo/Exo_thinking_happy.png"

    group emotion if_any "base":
        xoffset 10
        attribute annoyed default:
            "images/Sprites/Exo/Exo_base_annoyed.png"
        attribute sad:
            "images/Sprites/Exo/Exo_base_sad.png"
    
    #group emotion if_any "ear":
    #    attribute think:
    #        "images/Sprites/Exo/Exo_ear_think.png"
    #    attribute asharashen:
    #        "images/Sprites/Exo/Exo_ear_asharashen.png"

#endregion

#region Рэйзор
layeredimage r:
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
        xoffset -70
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
        #attribute surprised default:
        #    "images/Sprites/Nektar/Nektar_hand_hide_surprised.png"

image n_side = LayeredImageProxy("n", Transform(xalign=0.5, yalign=0.0, crop=(0.2, 0.0, 0.8, 0.8), crop_relative=True, yoffset=60))
#endregion


