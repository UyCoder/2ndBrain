@echo off
cd /d "%~dp0"
title Bilik AI Studio Terjime

py --version >nul 2>&1 && set PY=py || set PY=python
%PY% main.py

if errorlevel 1 (
    echo.
    echo [ERROR] Qurida xataliq chiqi!
    pause
)
