@echo off
REM One unified command for Windows - Simple version
cd /d "%~dp0"
if not exist venv python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt -q >nul 2>&1
python -m streamlit run main.py --server.port 8501

