#images 

## Определения фоновых изображений
# Фоны с прозрачностью
init -1:
    image bg_commander_block_default = "images/Backgrounds/Commander Block_default.png"
    image bg_commander_block_red = "images/Backgrounds/Commander Block_red.png"
    image bg_commander_block_dark = "images/Backgrounds/Commander Block_dark.png"

    image bg_commander_block_transparent_default = "images/Backgrounds/Commander Block_default.png"
    image bg_commander_block_transparent_red = "images/Backgrounds/Commander Block_red.png"
    image bg_commander_block_transparent_dark = "images/Backgrounds/Commander Block_dark.png"
    image bg_commander_block_transparent_chair = "images/Backgrounds/Commander Block_chair.png"
    image bg_stul_s_iglami = "images/Backgrounds/stul_s_iglami_stul.png"
    image bg_stul_bez_igl = "images/Backgrounds/stul_bez_igl.png"

    image bg_room_rayan_default = "images/Backgrounds/Room Rayan.png"
    image bg_room_rayan_dark = "images/Backgrounds/Room_Rayan_dark.png"
    image bg_room_viktor_dark = "images/Backgrounds/Room Viktor_dark.png"
    image bg_room_viktor_default = "images/Backgrounds/Room Viktor_default.png"


# Фоны
image bg_coridor1_dark = "images/Backgrounds/Coridor1_dark.jpg"
image bg_coridor1_default = "images/Backgrounds/Coridor1_default.jpg"
image bg_coridor1_red = "images/Backgrounds/Coridor1_red.jpg"
image bg_coridor2_dark = "images/Backgrounds/Coridor2_dark.jpg"
image bg_coridor2_default = "images/Backgrounds/Coridor2_default.jpg"
image bg_coridor2_red = "images/Backgrounds/Coridor2_red.jpg"
image bg_coridor2_red_smoke = "images/Backgrounds/Coridor2_red_smoke.png"
image bg_coridor3_dark = "images/Backgrounds/Coridor3_dark.jpg"
image bg_coridor3_default = "images/Backgrounds/Coridor3_default.jpg"
image bg_coridor3_red = "images/Backgrounds/Coridor3_red.jpg"
image bg_coridor3_default_cylinders = "images/Backgrounds/Coridor3_default_cylinders.jpg"
image bg_coridor3_red_cylinders = "images/Backgrounds/Coridor3_red_cylinders.jpg"
image bg_coridor3_red_cylinders_smoke = "images/Backgrounds/Coridor3_red_cylinders_smoke.png"
image bg_coridor3_dark_cylinders = "images/Backgrounds/Coridor3_dark_cylinders.jpg"
image bg_dinner_block = "images/Backgrounds/Dinner_Block.jpg"
image bg_dinner_block_dark = "images/Backgrounds/Dinner_Block_dark.jpg"
image bg_med_block = "images/Backgrounds/Med_Block.jpg"
image bg_med_block_red = "images/Backgrounds/Med_Block_red.jpg"
image bg_med_block_dark = "images/Backgrounds/Med_Block_dark.jpg"
image bg_generator = "images/Backgrounds/Generator.jpg"
image bg_generator_blue_screen = "images/Backgrounds/Generator_default_blue_screen.jpg"
image bg_generator_red = "images/Backgrounds/Generator_red.jpg"
image bg_generator_dark = "images/Backgrounds/Generator_dark.jpg"
image bg_engine = "images/Backgrounds/Engine.jpg"
image bg_safe = "images/Backgrounds/Safe.jpg"
image bg_monitors_block = "images/Backgrounds/Monitors_Block.jpg"
image bg_warehouse = "images/Backgrounds/Warehouse.jpg"
image bg_exit = "images/Backgrounds/Exit.png"
image bg_exit_open = "images/Backgrounds/Exit_without_door.png"
image exit_door = "images/Backgrounds/Exit_door.png"
image bg_safe_open = "images/Backgrounds/Safe_open.jpg"


# credits images
image logo_short:
    "gui/menu/Logo_short.png"
    matrixcolor BrightnessMatrix(-0.3)

image credits_img_1:
    "images/Credits/1.jpg"
image credits_img_2:
    "images/Credits/2.png"
image credits_img_3:
    "images/Credits/3.jpg"
image credits_img_4:
    "images/Credits/4_1.jpg"
    0.3
    "images/Credits/4_2.jpg"
    0.3
    "images/Credits/4_3.jpg"
    0.3
    "images/Credits/4_2.jpg"
    0.3   
    repeat
image credits_img_5:
    "images/Credits/5.jpg"
image credits_img_6:
    "images/Credits/6.jpg"
image credits_img_7:
    "images/Credits/7.jpg"

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
image mirror_default:
    "images/CG/CG_mirror/CG_mirror.png"

image mirror_dark:
    "images/CG/CG_mirror/CG_mirror_dark.png"

image mirror_water:
    "images/CG/CG_mirror/CG_mirror_water.png"

image room_viktor1:
    "images/CG/CG_Victor_room/cg_Room Viktor1.png"

image room_viktor2:
    "images/CG/CG_Victor_room/cg_Room Viktor2.jpg"

image room_viktor3:
    "images/CG/CG_Victor_room/cg_Room Viktor3.jpg"

image bg_menu_main = "gui/menu/bg.png"



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


