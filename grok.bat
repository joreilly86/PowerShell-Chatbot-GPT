@echo off
chcp 65001 > nul
echo Starting Grok Chatbot...
call .venv\Scripts\activate.bat
python -m src.grok
deactivate
pause
