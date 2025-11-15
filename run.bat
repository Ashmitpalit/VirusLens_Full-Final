@echo off
REM Windows batch script to run VirusLens
REM Cross-platform launcher for Windows

REM Check for network mode
set NETWORK_MODE=false
if "%1"=="--network" set NETWORK_MODE=true
if "%1"=="-n" set NETWORK_MODE=true

if "%NETWORK_MODE%"=="true" (
    echo ============================================================
    echo VirusLens - Network Mode
    echo ============================================================
    echo.
    echo Starting server on all network interfaces...
    echo.
    python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print('Network IP: ' + s.getsockname()[0]); print('Access from other devices: http://' + s.getsockname()[0] + ':8501'); s.close()" 2>nul
    echo Local access: http://localhost:8501
    echo ============================================================
    echo.
    python -m streamlit run main.py --server.port 8501 --server.address 0.0.0.0
) else (
    echo Starting VirusLens...
    python -m streamlit run main.py --server.port 8501 --server.address localhost
)

if errorlevel 1 (
    echo.
    echo Error: Failed to start Streamlit
    echo Make sure Python and dependencies are installed:
    echo   pip install -r requirements.txt
    pause
    exit /b 1
)

