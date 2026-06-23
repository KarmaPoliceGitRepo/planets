@echo off
REM Launch ReelCut on Windows. Needs Python 3 and FFmpeg on PATH.
where ffmpeg >nul 2>nul || (echo FFmpeg not found - install it first ^(see README^). & exit /b 1)
python "%~dp0app\server.py"
