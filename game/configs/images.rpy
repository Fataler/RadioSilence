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
image razer_nektar:
    "images/CG/Razer_Nektar/Razer_Nektar.png"


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