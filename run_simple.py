#!/usr/bin/env python3
"""Simple run script without SSL"""
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
APP = "app/pages/01_Scan.py"
PORT = "8501"
ADDRESS = "localhost"

args = [
    sys.executable, "-m", "streamlit", "run", str(BASE_DIR / APP),
    "--server.address", ADDRESS,
    "--server.port", PORT,
]

print(f"Starting Streamlit on http://{ADDRESS}:{PORT}")
print(f"Running: {' '.join(args)}")
sys.exit(subprocess.call(args))

