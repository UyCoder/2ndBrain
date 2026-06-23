@echo off
cd /d "%~dp0"
title Bilik AI Studio - Setup

echo.
echo ============================================
echo   Bilik AI Studio Terjime Qurali - Setup
echo ============================================
echo.

py --version >nul 2>&1
if errorlevel 1 ( python --version >nul 2>&1 && set PY=python || goto nopy )
if not defined PY set PY=py

echo [1/3] Kutupxaniler ornitilwatidu...
%PY% -m pip install -r requirements.txt
if errorlevel 1 ( echo [ERROR] pip install magazlup ketti & pause & exit /b 1 )

echo.
echo [2/3] Playwright Chromium yukleniwatidu...
%PY% -m playwright install chromium
if errorlevel 1 ( echo [ERROR] playwright install magazlup ketti & pause & exit /b 1 )

echo.
echo [3/3] .env teyerlang...
if not exist ".env" (
    copy ".env.example" ".env" >nul
    echo [INFO] .env quruldi — ichige Gmail hesabliringizni kirguzing!
    notepad .env
) else (
    echo [OK] .env bar
)

echo.
echo ============================================
echo   Setup tamam! Endi run.bat ni ishletkile.
echo ============================================
pause
exit /b 0

:nopy
echo [ERROR] Python tapilmidi! https://www.python.org/downloads/
pause
exit /b 1
