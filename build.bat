@echo off
setlocal enabledelayedexpansion

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

python -m pip install --upgrade pip pyinstaller -r requirements.txt
if errorlevel 1 exit /b 1

python -m PyInstaller --noconfirm --onefile --name total-score main.py
if errorlevel 1 exit /b 1

copy /y dist\total-score.exe dist\total-score-windows-x64.exe
if errorlevel 1 exit /b 1
