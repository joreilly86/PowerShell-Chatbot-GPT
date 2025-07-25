@echo off
chcp 65001 > nul
echo Starting OpenAI Chatbot...
call .venv\Scripts\activate.bat
python -m src.bot
deactivate
pause
