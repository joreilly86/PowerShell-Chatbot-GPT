@echo off
chcp 65001 > nul
echo Starting Perplexity Chatbot...
call .venv\Scripts\activate.bat
python -m src.plex
deactivate
pause
