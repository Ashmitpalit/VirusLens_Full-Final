#!/bin/bash
# Linux/Mac shell script to run VirusLens
# Cross-platform launcher for Unix-like systems

# Check for network mode argument
NETWORK_MODE=false
if [ "$1" = "--network" ] || [ "$1" = "-n" ]; then
    NETWORK_MODE=true
fi

echo "Starting VirusLens..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 not found. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists and activate it if present
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
elif [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Get network IP if in network mode
if [ "$NETWORK_MODE" = true ]; then
    # Try to get local IP
    NETWORK_IP=$(python3 -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0]); s.close()" 2>/dev/null)
    
    if [ -n "$NETWORK_IP" ]; then
        echo ""
        echo "============================================================"
        echo "🛡️  VirusLens - Network Mode"
        echo "============================================================"
        echo "🌐 Network IP: $NETWORK_IP"
        echo "🔗 Access from other devices: http://$NETWORK_IP:8501"
        echo "💻 Local access: http://localhost:8501"
        echo "============================================================"
        echo ""
    fi
    
    # Run Streamlit on all interfaces
    python3 -m streamlit run main.py --server.port 8501 --server.address 0.0.0.0
else
    # Run Streamlit on localhost only
    python3 -m streamlit run main.py --server.port 8501 --server.address localhost
fi

# Check exit status
if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Failed to start Streamlit"
    echo "Make sure dependencies are installed:"
    echo "  pip install -r requirements.txt"
    exit 1
fi

