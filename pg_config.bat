@echo off

REM Activate virtual environment
call C:\Users\Laurent\Desktop\Backend\OAuth2.0\venv\Scripts\activate.bat

REM Upgrade pip
pip install --upgrade pip

REM Install dependencies
pip install werkzeug==0.8.3
pip install flask==0.9
pip install Flask-Login==0.1.3
pip install oauth2client
pip install requests
pip install httplib2

REM Deactivate virtual environment
deactivate
