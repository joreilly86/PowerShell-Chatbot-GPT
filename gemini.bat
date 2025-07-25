@echo off
chcp 65001 > nul
echo Starting Gemini Chatbot...
call .venv\Scripts\activate.bat
python -m src.gem
deactivate
pause
