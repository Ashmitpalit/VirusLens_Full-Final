#!/bin/bash
# Diagnostic and run script for VirusLens

cd "$(dirname "$0")"

echo "=== VirusLens Startup Diagnostics ==="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: python3 not found!"
    exit 1
fi
echo "✓ Python3 found: $(python3 --version)"

# Check Streamlit
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "❌ Streamlit not installed. Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ ERROR: Failed to install dependencies"
        exit 1
    fi
    echo "✓ Dependencies installed"
else
    echo "✓ Streamlit installed: $(python3 -c 'import streamlit; print(streamlit.__version__)')"
fi

# Check if port is in use
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  Port 8501 is already in use"
    echo "   You can either:"
    echo "   1. Stop the process using port 8501"
    echo "   2. Use a different port: VL_PORT=8502 python3 run.py"
    read -p "   Kill existing process? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        kill -9 $(lsof -ti:8501) 2>/dev/null
        echo "✓ Killed existing process"
    else
        echo "❌ Exiting. Please free port 8501 or use a different port."
        exit 1
    fi
fi

echo ""
echo "=== Starting VirusLens ==="
echo "Access at: http://localhost:8501"
echo "Press Ctrl+C to stop"
echo ""

# Run the application
python3 run.py

