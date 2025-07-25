@echo off
chcp 65001 > nul
echo Starting Anthropic Chatbot...
call .venv\Scripts\activate.bat
python -m src.anthropic
deactivate
pause
