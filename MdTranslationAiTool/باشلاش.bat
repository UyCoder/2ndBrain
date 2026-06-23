@echo off
cd /d "%~dp0"
title Bilik Translation Tool v1.0

echo.
echo ================================================
echo    Bilik Translation Tool  v1.0
echo    http://127.0.0.1:5173
echo ================================================
echo.

py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON=py
    goto check_libs
)

python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON=python
    goto check_libs
)

echo [ERROR] Python tapilmidi!
echo https://www.python.org/downloads/
pause
exit /b 1

:check_libs
echo [Python] %PYTHON% - OK
%PYTHON% -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Kutupxaniler ornitilwatidu...
    %PYTHON% -m pip install flask chardet beautifulsoup4 lxml pymupdf
    if errorlevel 1 (
        echo [ERROR] Pip install failed.
        pause
        exit /b 1
    )
    echo [OK] Done.
    echo.
)

echo [INFO] Clearing cache...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul

echo [INFO] Starting Bilik...
echo [INFO] Browser: http://127.0.0.1:5173
echo.
%PYTHON% main.py

if errorlevel 1 (
    echo.
    echo [ERROR] main.py failed. See error above.
    pause
)
