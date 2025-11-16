#!/bin/bash
# Quick Start Script for VirusLens
# This script automates the setup process

set -e  # Exit on error

echo "🛡️  VirusLens - Quick Start Setup"
echo "=================================="
echo ""

# Step 1: Check Python
echo "Step 1: Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found! Please install Python 3.8+ first."
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo "✅ Found: $PYTHON_VERSION"
echo ""

# Step 2: Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Step 2: Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "Step 2: Virtual environment already exists"
fi
echo ""

# Step 3: Activate venv
echo "Step 3: Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Step 4: Install dependencies
echo "Step 4: Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✅ Dependencies installed"
echo ""

# Step 5: Check for .env file
if [ ! -f ".env" ]; then
    echo "Step 5: Creating .env file template..."
    cat > .env << EOF
# VirusTotal API Key (Required for scanning)
# Get your free API key from: https://www.virustotal.com/gui/join-us
VIRUSTOTAL_API_KEY=your_api_key_here

# Optional: URLScan.io API Key
# URLSCAN_API_KEY=your_urlscan_key_here

# Optional: AlienVault OTX API Key
# OTX_API_KEY=your_otx_key_here
EOF
    echo "⚠️  Created .env file template"
    echo "   Please edit .env and add your VirusTotal API key"
    echo "   (The app will still run, but scanning features won't work without it)"
else
    echo "Step 5: .env file already exists"
fi
echo ""

# Step 6: Check port
echo "Step 6: Checking port 8501..."
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  Port 8501 is already in use"
    read -p "   Kill existing process? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        kill -9 $(lsof -ti:8501) 2>/dev/null || true
        echo "✅ Killed existing process"
        sleep 2
    else
        echo "❌ Exiting. Please free port 8501 or use a different port."
        exit 1
    fi
else
    echo "✅ Port 8501 is available"
fi
echo ""

# Step 7: Start the server
echo "=================================="
echo "🚀 Starting VirusLens..."
echo "=================================="
echo ""
echo "🌐 Access the app at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "=================================="
echo ""

python3 -m streamlit run main.py --server.port 8501 --server.address localhost

