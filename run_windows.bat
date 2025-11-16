@echo off
REM Single unified command to run VirusLens on Windows
REM Usage: Just double-click this file or run: run_windows.bat

cd /d "%~dp0"

echo 🛡️  VirusLens - Starting...
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

REM Create venv if not exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate venv and install dependencies
echo 📥 Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip -q >nul 2>&1
python -m pip install -r requirements.txt -q
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

REM Create .env if not exists
if not exist ".env" (
    echo 📝 Creating .env file template...
    (
        echo VIRUSTOTAL_API_KEY=your_api_key_here
        echo # Get your free API key from: https://www.virustotal.com/gui/join-us
    ) > .env
    echo ⚠️  Please edit .env and add your VirusTotal API key
)

REM Check port and start server
echo.
echo ========================================
echo 🚀 Starting VirusLens...
echo ========================================
echo.
echo 🌐 Opening browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

REM Try to open browser automatically after 3 seconds
start "" "http://localhost:8501"

REM Start Streamlit
python -m streamlit run main.py --server.port 8501 --server.address localhost

pause

