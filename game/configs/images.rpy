#images 

## Определения фоновых изображений
# Фоны с прозрачностью
#init -1:


# Фоны
image bg_1_1 = "images/Backgrounds/Background1_1.jpg"
image bg_1_1_blur = "images/Backgrounds/Background1_1Blur.jpg"
image bg_2_1_day = "images/Backgrounds/Background2_1Day.jpg"
image bg_2_1_night = "images/Backgrounds/Background2_1Night.jpg"
image bg_3_1_shadow = "images/Backgrounds/Background3_1Shadow.jpg"
image bg_3_2 = "images/Backgrounds/Background3_2.jpg"
image bg_4_1 = "images/Backgrounds/Background4.jpg"
image bg_4_2Dummy = "images/Backgrounds/Background4Dummy.jpg"
image bg_base_day = "images/Backgrounds/Base_day.jpg"
image bg_base_night = "images/Backgrounds/Base_night.jpg"
image bg_cars = "images/Backgrounds/Cars.jpg"
image bg_hrushevki = "images/Backgrounds/Hrushevki.jpg"
image bg_square = "images/Backgrounds/Ploschad.jpg"
image bg_ovrag = "images/Backgrounds/Ovrag.jpg"


# credits images


## Общие изображения
image bg_black = Solid("#000")
image bg_white = Solid("#fff")
image bg_red = Solid("#ff1304")
image bg_paper = Solid("#FFE7CE")
image pulse_mask = "gui/masks/eye_mask2.png"

image bg_black_t_10 = Solid("#0000001a")
image bg_black_t_20 = Solid("#00000033")
image bg_black_t_30 = Solid("#0000004d")
image bg_black_t_40 = Solid("#00000066")
image bg_black_t_50 = Solid("#00000080")
image bg_black_t_60 = Solid("#00000099")
image bg_black_t_70 = Solid("#000000b3")
image bg_black_t_80 = Solid("#000000cc")
image bg_black_t_90 = Solid("#000000e6")

## цгшки
image CG_knife_1:
    "images/CG/Knife/CG_knife_1.png"
image CG_knife_2:
    "images/CG/Knife/CG_knife_2.png"
image CG_knife_3:
    "images/CG/Knife/CG_knife_3.png"
image CG_knife_nektar_fear = At("CG/Knife/CG_knife_nektar_fear.png", fade_on_show)
image CG_knife_nektar_fear_cry = At("CG/Knife/CG_knife_nektar_fear_cry.png", fade_on_show)
image CG_knife_nektar_smile = At("CG/Knife/CG_knife_nektar_smile.png", fade_on_show)
image CG_knife_nektar_smile_cry = At("CG/Knife/CG_knife_nektar_smile_cry.png", fade_on_show)
image CG_knife_nektar_hurt = At("CG/Knife/CG_knife_nektar_hurt.png", fade_on_show)
image CG_knife_ray_asharashen = At("CG/Knife/CG_knife_ray_asharashen.png", fade_on_show)
image CG_knife_ray_cry = At("CG/Knife/CG_knife_ray_cry.png", fade_on_show)
image CG_knife_ray_rage = At("CG/Knife/CG_knife_ray_rage.png", fade_on_show)
image CG_knife_tumansk = At("images/CG/Knife/CG_knife_tumansk.png", soot_drift_bottom)

image CG_Stalnoy_duel_serious:
    "images/CG/StalnoyxStalnoy/eto_baza_seryozniy.png"
image CG_Stalnoy_duel_evil:
    "images/CG/StalnoyxStalnoy/eto_baza_zloy.png"
image CG_Stalnoy_duel_ST1_seryozniy = At("CG/StalnoyxStalnoy/ST1_seryozniy.png", fade_on_show)
image CG_Stalnoy_duel_ST1_smile = At("CG/StalnoyxStalnoy/ST1_zloy.png", fade_on_show)
image CG_Stalnoy_duel_CH_seryozniy = At("CG/StalnoyxStalnoy/ST2_seryozniy.png", fade_on_show)
image CG_Stalnoy_duel_CH_smile = At("CG/StalnoyxStalnoy/ST2_zloy.png", fade_on_show)
image CG_Stalnoy_duel_tumansk = At("CG/StalnoyxStalnoy/tumansk.png", soot_drift_bottom)
image CG_Stalnoy_aim = At("CG/StalnoyxStalnoy/aim.png", soot_drift_bottom)

image CG_LeonxExo:
    "images/CG/LeonxExo/ETO_BAZA.png"
image CG_LeonxExo_Exo_smile = At("CG/LeonxExo/ebich_EXO_hehe.png", fade_on_show)
image CG_LeonxExo_Exo_idle = At("CG/LeonxExo/ebich_EXO_mmm.png", fade_on_show)
image CG_LeonxExo_Leon_smile = At("CG/LeonxExo/ebich_LEON_hehe.png", fade_on_show)
image CG_LeonxExo_Leon_shy = At("CG/LeonxExo/ebich_LEON_oy.png", fade_on_show)
image CG_LeonxExo_tumansk = At("CG/LeonxExo/tumansk-nad.png", soot_drift_bottom)

## Эффекты
transform darken:
    matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

transform lighten:
    matrixcolor TintMatrix("#ffffff") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное затемнение
transform fade_to_dark:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное осветление
transform fade_to_light:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)


image shadow = "images/Sprites/Base/shadow.png"