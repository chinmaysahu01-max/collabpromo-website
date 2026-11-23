@echo off
title CollabPromo.com Launcher
echo ========================================================
echo  Launching CollabPromo.com in your default browser...
echo ========================================================
cd /d "%~dp0"

:: Open index.html directly in the default browser
start "" "index.html"

:: Also start the local server in case http://localhost:8000 is preferred
echo.
echo Starting local web server at http://localhost:8000 ...
echo You can also access the website at http://localhost:8000
echo Close this window to stop the local server.
python server.py 8000
pause
