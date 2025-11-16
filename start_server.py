#!/usr/bin/env python3
"""Start VirusLens server"""
import sys
import os
import subprocess
import time
from pathlib import Path

# Change to project directory
os.chdir(Path(__file__).parent)

# Ensure dependencies are installed
try:
    import streamlit
except ImportError:
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    import streamlit

# Start Streamlit
print("Starting VirusLens on http://localhost:8501")
print("Press Ctrl+C to stop")

cmd = [
    sys.executable, "-m", "streamlit", "run", "main.py",
    "--server.port", "8501",
    "--server.address", "localhost"
]

try:
    subprocess.run(cmd, check=False)
except KeyboardInterrupt:
    print("\nStopping server...")
    sys.exit(0)

