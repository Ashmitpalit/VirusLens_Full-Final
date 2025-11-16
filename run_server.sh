#!/bin/bash
cd "$(dirname "$0")"

# Install dependencies if needed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "Installing dependencies..."
    python3 -m pip install -r requirements.txt --quiet
fi

# Kill any existing streamlit processes
pkill -f "streamlit.*main.py" 2>/dev/null
sleep 1

# Start streamlit
echo "Starting VirusLens..."
echo "Access at: http://localhost:8501"
python3 -m streamlit run main.py --server.port 8501 --server.address localhost

