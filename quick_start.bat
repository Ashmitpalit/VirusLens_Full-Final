@echo off
REM Quick Start Script for VirusLens (Windows)
REM This script automates the setup process

echo 🛡️  VirusLens - Quick Start Setup
echo ==================================
echo.

REM Step 1: Check Python
echo Step 1: Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+ first.
    pause
    exit /b 1
)
python --version
echo ✅ Python found
echo.

REM Step 2: Create venv if it doesn't exist
if not exist "venv" (
    echo Step 2: Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo Step 2: Virtual environment already exists
)
echo.

REM Step 3: Activate venv
echo Step 3: Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Step 4: Install dependencies
echo Step 4: Installing dependencies...
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt -q
echo ✅ Dependencies installed
echo.

REM Step 5: Check for .env file
if not exist ".env" (
    echo Step 5: Creating .env file template...
    (
        echo # VirusTotal API Key (Required for scanning^)
        echo # Get your free API key from: https://www.virustotal.com/gui/join-us
        echo VIRUSTOTAL_API_KEY=your_api_key_here
        echo.
        echo # Optional: URLScan.io API Key
        echo # URLSCAN_API_KEY=your_urlscan_key_here
        echo.
        echo # Optional: AlienVault OTX API Key
        echo # OTX_API_KEY=your_otx_key_here
    ) > .env
    echo ⚠️  Created .env file template
    echo    Please edit .env and add your VirusTotal API key
    echo    (The app will still run, but scanning features won't work without it^)
) else (
    echo Step 5: .env file already exists
)
echo.

REM Step 6: Start the server
echo ==================================
echo 🚀 Starting VirusLens...
echo ==================================
echo.
echo 🌐 Access the app at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.
echo ==================================
echo.

python -m streamlit run main.py --server.port 8501 --server.address localhost

pause

