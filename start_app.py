#!/usr/bin/env python3
"""
Simple startup script for VirusLens
This will check dependencies and start the app
"""
import sys
import subprocess
from pathlib import Path

print("=" * 60)
print("🛡️  VirusLens — Cyber Threat Analyzer")
print("=" * 60)
print()

# Check Python version
print(f"Python: {sys.version.split()[0]} ({sys.executable})")
print()

# Check Streamlit
try:
    import streamlit
    print(f"✓ Streamlit {streamlit.__version__} is installed")
except ImportError:
    print("✗ Streamlit is not installed")
    print("  Installing dependencies...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        cwd=Path(__file__).parent
    )
    if result.returncode != 0:
        print("✗ Failed to install dependencies")
        sys.exit(1)
    print("✓ Dependencies installed")
    import streamlit

print()

# Check port availability
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('localhost', 8501))
sock.close()

if result == 0:
    print("⚠️  Port 8501 is already in use")
    print("   The app might already be running at http://localhost:8501")
    print("   Or you can use a different port: VL_PORT=8502 python3 run.py")
    response = input("   Continue anyway? (y/n): ")
    if response.lower() != 'y':
        sys.exit(0)
else:
    print("✓ Port 8501 is available")

print()
print("=" * 60)
print("Starting VirusLens...")
print("=" * 60)
print()
print("🌐 Access the app at: http://localhost:8501")
print()
print("Press Ctrl+C to stop the server")
print()

# Run streamlit
try:
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "main.py",
         "--server.port", "8501",
         "--server.address", "localhost"],
        cwd=Path(__file__).parent
    )
except KeyboardInterrupt:
    print("\n\nServer stopped.")
    sys.exit(0)
except Exception as e:
    print(f"\n✗ Error starting server: {e}")
    sys.exit(1)

