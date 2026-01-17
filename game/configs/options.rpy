## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.


## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("RadioSilence")
define config.image_cache_size_mb = 512

define config.developer = True
define config.fast_skipping = True if config.developer else False

define config.menu_include_disabled = True

## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True

define config.rollback_enabled = True
define config.default_fullscreen = False if config.developer else True
#define config.speaking_attribute = "talk"


## Версия игры.

define config.version = "1.0"

define config.mouse = { 'default' : [ ("gui/Cursor.png", 0, 0)], 'button' : [ ("gui/CursorR.png", 0, 0)]}


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""
Визуальная новелла разработана в рамках игрового джема {a=%(jam)s}Капелла Jam 3 2026{/a} 

Дата релиза: 17.01.2026

Использованные сторонние ресурсы лежат в файле {i}external_resources.txt{/i}.

Авторы: \n
{w=0}     - Featharine ({a=https://vk.com/sweet_sour_figures}ВК{/a}) - \n
{w=0}     - Yele_nir - \n
{w=0}     - LehanFox - \n
{w=0}     - Danya Balakhnin ({a=https://vk.com/gospodin_balakhnin}ВК{/a}) - \n
{w=0}     - Fataler ({a=https://steamcommunity.com/id/fataler}Steam{/a}) - \n
{w=0}     - Kapushishin ({a=https://steamcommunity.com/id/Kapushishin}Steam{/a}) - \n
"""% {"jam": URL_JAM})


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "RadioSilence"


## Звуки и музыка ##############################################################

## Эти три переменные управляют, среди прочего, тем, какие микшеры показываются
## игроку по умолчанию. Установка одной из них в False скроет соответствующий
## микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.default_sfx_volume = 0.6
define config.default_music_volume = 0.6

## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

define config.main_menu_music = music_main_theme


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = Dissolve(0.5)
define config.exit_transition = Dissolve(0.5)
## Переход между экранами игрового меню.
define config.intra_transition = Dissolve(0.5)


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = Dissolve(.2)


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = Dissolve(1)

## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"

#define config.layers = [ 'master', 'transient', 'screens', 'overlay']

## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

init python:
    # Set "A" for auto-forward mode
    for k in ['a', 'A', "ф", "Ф"]:
        if k not in config.keymap['toggle_afm']:
            config.keymap['toggle_afm'].append(k)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 60

## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15

define config.default_text_cps = 60
define config.default_afm_time = 15
## Максимальное количество страниц сохранений

define max_save_pages = 1

define config.has_quicksave = False
define config.has_sync = False
## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>.
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "RadioSilence-10082024"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "gui/window_icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.bat', None)
    build.classify('**/tests/**', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpym', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')


## Для совершения покупок в приложении требуется лицензионный ключ Google Play.
## Его можно найти в консоли разработчика Google Play в разделе "Монетизация" >
## "Настройка монетизации" > "Лицензирование".

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

define build.itch_project = "featharine/radio-silence"