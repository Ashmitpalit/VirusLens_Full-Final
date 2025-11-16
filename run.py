#!/usr/bin/env python3
"""Final startup script - installs deps and runs VirusLens"""
import subprocess
import sys
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

# Install deps
print("Checking dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"])

# Run
print("\n🚀 Starting VirusLens at http://localhost:8501\n")
subprocess.run([sys.executable, "-m", "streamlit", "run", "main.py", "--server.port", "8501"])
