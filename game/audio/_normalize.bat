@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem ===== Usage =========================================================
rem normalize_audio.bat [music|sfx|auto] [root_folder]
rem Примеры:
rem   normalize_audio.bat music
rem   normalize_audio.bat sfx "D:\VN\assets\audio"
rem   normalize_audio.bat auto
rem =====================================================================

rem ---------- Параметры запуска ----------
set "MODE=%~1"
if "%MODE%"=="" set "MODE=auto"
set "ROOT=%~2"
if "%ROOT%"=="" set "ROOT=%~dp0"

rem ---------- Где брать ffmpeg ----------
set "FFMPEG=ffmpeg"
where "%FFMPEG%" >nul 2>nul
if errorlevel 1 (
  if exist "%~dp0ffmpeg.exe" ( set "FFMPEG=%~dp0ffmpeg.exe" ) else (
    echo [ERR] ffmpeg не найден. Положи ffmpeg.exe рядом с .bat или добавь в PATH.
    pause & exit /b 1
  )
)

rem ---------- Профили (подправь под себя) ----------
rem MUSIC: обычный BGM / лупы
set "MUSIC_I=-18"      rem целевой LUFS
set "MUSIC_TP=-1.5"    rem потолок true peak
set "MUSIC_VORBIS_Q=6" rem OGG q (0..10)
set "MUSIC_LAME_Q=2"   rem MP3 -q:a (0..9, 0 = лучшее)

rem SFX: клики/шаги/импакты
set "SFX_I=-20"
set "SFX_TP=-1.0"
set "SFX_LRA=7"
set "SFX_VORBIS_Q=5"
set "SFX_LAME_Q=2"

rem (необязательно) зафиксировать частоту: 44100. Оставь пустым, чтобы не менять.
rem set "SR=44100"

set /a PROCESSED=0
echo Mode: %MODE%
echo Root: "%ROOT%"
echo.

rem ===== Рекурсивная обработка OGG и MP3 =====
for /R "%ROOT%" %%F in (*.ogg *.mp3) do (
  set "FULL=%%~fF"
  set "DIR=%%~dpF"
  set "BASE=%%~nF"
  set "EXT=%%~xF"

  rem ----- Определить профиль -----
  set "PROFILE=%MODE%"
  if /I "%MODE%"=="auto" (
    set "PROFILE=music"
    rem Heuristic: если в пути встречается "sfx" (регистр не важен) -> SFX
    set "T=!DIR!"
    set "T=!T:sfx=!"
    if not "!T!"=="!DIR!" set "PROFILE=sfx"
    rem При желании добавь ещё ключевые слова, например:
    rem   set "T=!DIR!" & set "T=!T:\fx\=!" & if not "!T!"=="!DIR!" set "PROFILE=sfx"
  )

  rem ----- Сообщить какой профиль -----
  if /I "!PROFILE!"=="music" ( echo [MUSIC] "!FULL!" ) else ( echo [SFX  ] "!FULL!" )

  rem ----- Сборка фильтра и кодека -----
  if /I "!PROFILE!"=="music" (
    set "FILTER=loudnorm=I=%MUSIC_I%:TP=%MUSIC_TP%"
  ) else (
    set "FILTER=silenceremove=start_periods=1:start_duration=0.02:start_threshold=-40dB:stop_periods=1:stop_duration=0.05:stop_threshold=-40dB,loudnorm=I=%SFX_I%:TP=%SFX_TP%:LRA=%SFX_LRA%,alimiter=limit=0.98:attack=5:release=50"
  )

  if /I "!EXT!"==".ogg" (
    set "OUTTMP=!DIR!!BASE!.__tmp__.ogg"
    if defined SR (
      "%FFMPEG%" -y -v error -hide_banner -i "!FULL!" -af "!FILTER!" -ar %SR% -c:a libvorbis -q:a !MUSIC_VORBIS_Q! -map_metadata 0 "!OUTTMP!"
    ) else (
      "%FFMPEG%" -y -v error -hide_banner -i "!FULL!" -af "!FILTER!"           -c:a libvorbis -q:a !MUSIC_VORBIS_Q! -map_metadata 0 "!OUTTMP!"
    )
  ) else (
    set "OUTTMP=!DIR!!BASE!.__tmp__.mp3"
    if defined SR (
      "%FFMPEG%" -y -v error -hide_banner -i "!FULL!" -af "!FILTER!" -ar %SR% -c:a libmp3lame -q:a !MUSIC_LAME_Q! -map_metadata 0 -id3v2_version 3 "!OUTTMP!"
    ) else (
      "%FFMPEG%" -y -v error -hide_banner -i "!FULL!" -af "!FILTER!"           -c:a libmp3lame -q:a !MUSIC_LAME_Q! -map_metadata 0 -id3v2_version 3 "!OUTTMP!"
    )
  )

  rem ----- Проверка результата и замена -----
  if errorlevel 1 (
    echo   !! Ошибка ffmpeg, файл пропущен
    del /Q "!OUTTMP!" 2>nul
  ) else (
    move /Y "!OUTTMP!" "!FULL!" >nul
    if not errorlevel 1 set /a PROCESSED+=1
  )
)

if %PROCESSED% EQU 0 (
  echo [INFO] Ничего не обработано. Проверь, что есть .ogg/.mp3 под "%ROOT%".
  echo Для отладки: dir /s /b "%ROOT%\*.ogg" ^& dir /s /b "%ROOT%\*.mp3"
) else (
  echo Готово. Обработано файлов: %PROCESSED%.
)
pause
