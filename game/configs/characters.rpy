#region characters
define R = Character("Райан", image="r", callback=speaker('r_f'))
define R_t = Character(None, image="r")
define R_f = Character("Райан", image="r_f", callback=speaker('r_f'))
define I = Character("Ирис", image="i", callback=speaker('i'))
define V = Character("Виктор", image="v", callback=speaker('v'))
define D = Character("Дэвид", image="d", callback=speaker('d'))
define S = Character("Софи", image="s", callback=speaker('s'))
define N = Character("Неизвестный голос")
define E = Character("Элис")
define story_teller = Character(None, kind=nvl, color="#1a1a1f")

#универсальный перс
init python:
    def speak_as(name, text, color="#232324"):
        Character(name, color=color)(text)

#endregion

#region Ryan

image side r = LayeredImageProxy("r_f", Transform(crop=(0, 0, 800, 550), xoffset=-80, zoom=0.8))

layeredimage r_f:
    at auto_flip("r_f", "right")

    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute serious default:
            Null()
        attribute thinking:
            Null()
        attribute ear:
            Null()
        attribute crazy:
            Null()

    group emotion if_any "serious":
        attribute think default:
            "images/Rayan/Rayan_seryoznii_thinking.png"
        attribute angry:
            "images/Rayan/Rayan_seryoznii_angry.png"
        attribute very_angry:
            "images/Rayan/Rayan_seryoznii_very_angry.png"
        attribute fainting:
            "images/Rayan/Rayan_seryoznii_fainting.png"
        attribute fainting_blood:
            "images/Rayan/Rayan_seryoznii_fainting_blood.png"
        attribute happy:
            "images/Rayan/Rayan_seryoznii_happy.png"

    group emotion if_any "thinking":
        attribute neutral default:
            "images/Rayan/Rayan_thinking_calm.png"
        attribute not_sure:
            "images/Rayan/Rayan_thinking_interrogative.png"
        attribute ne_ponyal:
            "images/Rayan/Rayan_thinking_ne_ponyal.png"
        attribute osharashen:
            "images/Rayan/Rayan_thinking_osharashen.png"
        attribute suspicious:
            "images/Rayan/Rayan_thinking_suspicious.png"
        attribute happy:
            "images/Rayan/Rayan_thinking_happy.png"

    group emotion if_any "ear":
        xoffset -20
        attribute neutral default:
            "images/Rayan/Rayan_yxo_neutral.png"
        attribute dissatisfied:
            "images/Rayan/Rayan_yxo_dissatisfied.png"
        attribute hehe:
            "images/Rayan/Rayan_yxo_hehe.png"
        attribute smile:
            "images/Rayan/Rayan_yxo_double_hehe.png"
        attribute sick:
            "images/Rayan/Rayan_yxo_sick.png"
        attribute surprised:
            "images/Rayan/Rayan_yxo_surprised.png"
    
    group emotion if_any "crazy":
        attribute mnogo:
            "images/Rayan/Rayan_crazy_mnogo.png"
        attribute nemnogo:
            "images/Rayan/Rayan_crazy_nemnogo.png"
        attribute pizdec:
            "images/Rayan/Rayan_crazy_pizdec.png"

    group mouth if_any "serious" if_not "fainting_blood":
        attribute talk:
            WhileSpeaking('r_f', 'rayan_talk_seryoznii', Null())

    group mouth if_any "thinking":
        attribute talk:
            WhileSpeaking('r_f', 'rayan_talk_thinking', Null())

    group mouth if_any "ear":
        xoffset -20
        attribute talk:
            WhileSpeaking('r_f', 'rayan_talk_ear', Null())

    group mouth if_any "crazy":
        attribute talk:
            Null()

    group beard:
        attribute beard_off default:
            Null()
        attribute beard_on if_any "serious":
            "images/Rayan/Rayan_seryoznii_boroda.png"
        attribute beard_on if_any "thinking":
            "images/Rayan/Rayan_thinking_boroda.png"
        attribute beard_on if_any "ear":
            xoffset -20
            "images/Rayan/Rayan_yxo_boroda.png"
        attribute beard_on if_any "crazy":
            Null()

image rayan_talk_seryoznii:
    'images/Rayan/Rayan_seryoznii_rot1.png'
    pause 0.1
    'images/Rayan/Rayan_seryoznii_rot2.png'
    pause 0.1
    'images/Rayan/Rayan_seryoznii_rot3.png'
    repeat

image rayan_talk_thinking:
    'images/Rayan/Rayan_thinking_rot1.png'
    pause 0.1
    'images/Rayan/Rayan_thinking_rot2.png'
    pause 0.1
    'images/Rayan/Rayan_thinking_rot3.png'
    repeat

image rayan_talk_ear:
    'images/Rayan/Rayan_yxo_rot1.png'
    pause 0.1
    'images/Rayan/Rayan_yxo_rot2.png'
    pause 0.1
    'images/Rayan/Rayan_yxo_rot3.png'
    repeat

#endregion

#region Iris
layeredimage i:
    yoffset 2
    zoom 0.90
    at auto_flip("i", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute normal default:
            Null()
        attribute pen:
            Null()
        attribute profile:
            Null()
        attribute smoke:
            Null()

    group emotion if_any "normal":
        attribute angry:
            "images/Iris/Iris_neutral_angry.png"
        attribute bychit:
            "images/Iris/Iris_neutral_bychit.png"
        attribute crazy:
            "images/Iris/Iris_neutral_crazy.png"
        attribute neutral_happy:
            "images/Iris/Iris_neutral_neutral_happy.png"
        attribute neutral default:
            "images/Iris/Iris_neutral_neutral.png"
        attribute ridicule:
            "images/Iris/Iris_neutral_ridicule.png"
        attribute very_ridicule:
            "images/Iris/Iris_neutral_Very_ridicule.png"
            

    group emotion if_any "pen":
        attribute nervous_laughter:
            "images/Iris/Iris_pen_nervous_laughter.png"
        attribute nervous:
            "images/Iris/Iris_pen_nervous.png"
        attribute neutral default:
            "images/Iris/Iris_pen_neutral.png"
        attribute ozadachen:
            "images/Iris/Iris_pen_ozadachen.png"
        attribute sad:
            "images/Iris/Iris_pen_sad.png"

    group emotion if_any "profile":
        attribute ahui:
            "images/Iris/Iris_profile_ahui.png"
        attribute angry:
            "images/Iris/Iris_profile_angry.png"
        attribute neutral default:
            "images/Iris/Iris_profile_neutral.png"
        attribute oooops:
            "images/Iris/Iris_profile_oooops.png"
        attribute osharashen:
            "images/Iris/Iris_profile_osharashen.png"
        attribute tricky:
            "images/Iris/Iris_profile_tricky.png"

    group emotion if_any "smoke":
        attribute calm default:
            "images/Iris/Iris_smoke_calm.png"
        attribute cry:
            "images/Iris/Iris_smoke_cry.png"
        attribute happy:
            "images/Iris/Iris_smoke_happy.png"
        attribute puzzled:
            "images/Iris/Iris_smoke_puzzled.png"
        attribute surprised:
            "images/Iris/Iris_smoke_surprised.png"
        attribute tricky:
            "images/Iris/Iris_smoke_tricky.png"

    group mouth if_any "normal":
        attribute talk:
            WhileSpeaking('i', 'iris_talk_normal', Null())

    group mouth if_any "pen":
        attribute talk:
            WhileSpeaking('i', 'iris_talk_pen', Null())

    group mouth if_any "profile":
        attribute talk:
            WhileSpeaking('i', 'iris_talk_profile', Null())

    group mouth if_any "smoke":
        attribute talk:
            WhileSpeaking('i', 'iris_talk_smoke', Null())

image iris_talk_normal:
    'images/Iris/Iris_neutral_rot1.png'
    pause 0.1
    'images/Iris/Iris_neutral_rot2.png'
    pause 0.1
    'images/Iris/Iris_neutral_rot3.png'
    repeat

image iris_talk_pen:
    'images/Iris/Iris_pen_rot1.png'
    pause 0.1
    'images/Iris/Iris_pen_rot2.png'
    pause 0.1
    'images/Iris/Iris_pen_rot3.png'
    repeat

image iris_talk_profile:
    'images/Iris/Iris_profile_rot1.png'
    pause 0.1
    'images/Iris/Iris_profile_rot2.png'
    pause 0.1
    'images/Iris/Iris_profile_rot3.png'
    repeat

image iris_talk_smoke:
    'images/Iris/Iris_smoke_rot1.png'
    pause 0.1
    'images/Iris/Iris_smoke_rot2.png'
    pause 0.1
    'images/Iris/Iris_smoke_rot3.png'
    repeat

#endregion

#region Viktor
layeredimage v:
    zoom 0.98
    at auto_flip("v", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute profile default:
            Null()
        attribute ruki:
            Null()
        attribute pockets:
            Null()

    group emotion if_any "profile":
        attribute angry:
            "images/Viktor/Viktor_profile_angry.png"
        attribute crazy:
            "images/Viktor/Viktor_profile_crazy.png"
        attribute neutral default:
            "images/Viktor/Viktor_profile_neutral.png"
        attribute sad:
            "images/Viktor/Viktor_profile_sad.png"
        attribute scared:
            "images/Viktor/Viktor_profile_scared.png"
        attribute smile:
            "images/Viktor/Viktor_profile_smile.png"
        attribute serious:
            "images/Viktor/Viktor_profile_suspects.png"
        attribute tricky:
            "images/Viktor/Viktor_profile_tricky.png"

    group emotion if_any "ruki":
        attribute sad:
            "images/Viktor/Viktor_2yxa_sad.png"
        attribute crazy:
            "images/Viktor/Viktor_2yxa_crazy.png"
        attribute crazy_down:
            "images/Viktor/Viktor_2yxa_crazy_down.png"
        attribute cunning:
            "images/Viktor/Viktor_2yxa_cunning.png"
        attribute osharashen:
            "images/Viktor/Viktor_2yxa_osharashen.png"
        attribute puzzled:
            "images/Viktor/Viktor_2yxa_puzzled.png"
        attribute puzzled_sad default:
            "images/Viktor/Viktor_2yxa_puzzled_sad.png"
        attribute shy:
            "images/Viktor/Viktor_2yxa_shy.png"
        attribute tricky:
            "images/Viktor/Viktor_2yxa_tricky.png"

    group emotion if_any "pockets":
        attribute angry:
            "images/Viktor/Viktor_sutuliy_angry.png"
        attribute dream:
            "images/Viktor/Viktor_sutuliy_dream.png"
        attribute fainting:
            "images/Viktor/Viktor_sutuliy_fainting.png"
        attribute happy:
            "images/Viktor/Viktor_sutuliy_happy.png"
        attribute nedovolen:
            "images/Viktor/Viktor_sutuliy_nedovolen.png"
        attribute sad:
            "images/Viktor/Viktor_sutuliy_sad.png"
        attribute sorry:
            "images/Viktor/Viktor_sutuliy_sorry.png"
        attribute suspects:
            "images/Viktor/Viktor_sutuliy_suspects.png"
        attribute think default:
            "images/Viktor/Viktor_sutuliy_think.png"

    group zatichka if_any "pockets":
        attribute zatichka_on default:
            "images/Viktor/zatychka_dlya_viktora.png"
    
    group mouth if_any "profile":
        attribute talk:
            Null()
            
    group mouth if_any "ruki":
        attribute talk:
            WhileSpeaking('v', 'viktor_talk_ruki', Null())

    group mouth if_any "pockets":
        attribute talk:
            WhileSpeaking('v', 'viktor_talk_pockets', Null())

image viktor_talk_ruki:
    'images/Viktor/Viktor_2yxa_rot1.png'
    pause 0.1
    'images/Viktor/Viktor_2yxa_rot2.png'
    pause 0.1
    'images/Viktor/Viktor_2yxa_rot3.png'
    repeat

image viktor_talk_pockets:
    'images/Viktor/Viktor_sutuliy_rot1.png'
    pause 0.1
    'images/Viktor/Viktor_sutuliy_rot2.png'
    pause 0.1
    'images/Viktor/Viktor_sutuliy_rot3.png'
    repeat
#endregion

#region David
layeredimage d:
    zoom 0.95
    at auto_flip("d", "left")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

    group pose:
        attribute serious default:
            Null()
        attribute fist:
            Null()

    group emotion if_any "serious":
        attribute neutral default:
            "images/David/David_delovoi_neutral.png"
        attribute crazy:
            "images/David/David_delovoi_angry.png"
        attribute osharashen:
            "images/David/David_delovoi_asharashen.png"
        attribute calm:
            "images/David/David_delovoi_calm.png"
        attribute angry:
            "images/David/David_delovoi_crazy.png"
        attribute smile:
            "images/David/David_delovoi_dovolen.png"
        attribute fear:
            "images/David/David_delovoi_fear.png"
        attribute happy:
            "images/David/David_delovoi_happy.png"

    group emotion if_any "fist":
        attribute neutral default:
            "images/David/David_kulak_neutral.png"
        attribute angry:
            "images/David/David_kulak_angry.png"
        attribute smug:
            "images/David/David_kulak_calm.png"
        attribute confused:
            "images/David/David_kulak_confused.png"
        attribute happy:
            "images/David/David_kulak_happy.png"
        attribute annoyed:
            "images/David/David_kulak_irritated.png"
        attribute fainting:
            "images/David/David_kulak_obmorok.png"
        attribute fainting_blood:
            "images/David/David_kulak_obmorok2.png"

    group mouth if_any "serious":
        attribute talk:
            WhileSpeaking('d', 'david_talk_serious', Null())

    group mouth if_any "fist":
        attribute talk:
            WhileSpeaking('d', 'david_talk_fist', Null())

image david_talk_serious:
    'images/David/David_delovoi_rot1.png'
    pause 0.1
    'images/David/David_delovoi_rot2.png'
    pause 0.1
    'images/David/David_delovoi_rot3.png'
    repeat

image david_talk_fist:
    'images/David/David_kulak_rot1.png'
    pause 0.1
    'images/David/David_kulak_rot2.png'
    pause 0.1
    'images/David/David_kulak_rot3.png'
    repeat
#endregion

#region Sophie
layeredimage s:
    zoom 0.95
    at auto_flip("s", "right")

    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute profile default:
            Null()
        attribute ruki:
            Null()
        attribute shy:
            Null()

    group emotion if_any "profile":
        attribute annoyed:
            "images/Sofi/Sofi_profile_annoyed.png"
        attribute cry:
            "images/Sofi/Sofi_profile_cry.png"
        attribute despair:
            "images/Sofi/Sofi_profile_despair.png"
        attribute fainting:
            "images/Sofi/Sofi_profile_fainting.png"
        attribute happy:
            "images/Sofi/Sofi_profile_happy.png"
        attribute neutral default:
            "images/Sofi/Sofi_profile_neutral.png"
        attribute sad:
            "images/Sofi/Sofi_profile_sad.png"

    group emotion if_any "ruki":
        attribute calm default:
            "images/Sofi/Sofi_ruki_calm.png"
        attribute crazy:
            "images/Sofi/Sofi_ruki_crazy.png"
        attribute cry:
            "images/Sofi/Sofi_ruki_cry.png"
        attribute happy:
            "images/Sofi/Sofi_ruki_happy.png"
        attribute hurt:
            "images/Sofi/Sofi_ruki_hurt.png"
        attribute neutral:
            "images/Sofi/Sofi_ruki_neutral.png"
        attribute ozadachen:
            "images/Sofi/Sofi_ruki_ozadachen.png"

    group emotion if_any "shy":
        attribute angry:
            "images/Sofi/Sofi_shy_angry.png"
        attribute fainting:
            "images/Sofi/Sofi_shy_fainting.png"
        attribute happy:
            "images/Sofi/Sofi_shy_happy.png"
        attribute nedovolen:
            "images/Sofi/Sofi_shy_nedovolen.png"
        attribute neutral default:
            "images/Sofi/Sofi_shy_neutral.png"
        attribute surprised:
            "images/Sofi/Sofi_shy_surprised.png"
        attribute worried:
            "images/Sofi/Sofi_shy_worried.png"
    
    group mouth if_any "profile":
        attribute talk:
            Null()
            
    group mouth if_any "ruki":
        attribute talk:
            WhileSpeaking('s', 'sofi_talk_ruki', Null())

    group mouth if_any "shy":
        attribute talk:
            WhileSpeaking('s', 'sofi_talk_shy', Null())

image sofi_talk_ruki:
    'images/Sofi/Sofi_ruki_rot1.png'
    pause 0.1
    'images/Sofi/Sofi_ruki_rot2.png'
    pause 0.1
    'images/Sofi/Sofi_ruki_rot3.png'
    repeat

image sofi_talk_shy:
    'images/Sofi/Sofi_shy_rot1.png'
    pause 0.1
    'images/Sofi/Sofi_shy_rot2.png'
    pause 0.1
    'images/Sofi/Sofi_shy_rot3.png'
    repeat
#endregion



