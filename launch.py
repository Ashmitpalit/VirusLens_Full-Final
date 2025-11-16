#!/usr/bin/env python3
"""Launch script for VirusLens - verifies setup and starts server"""
import sys
import subprocess
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()
os.chdir(BASE_DIR)

print("=" * 70)
print("🛡️  VirusLens — Cyber Threat Analyzer")
print("=" * 70)
print(f"\nWorking directory: {BASE_DIR}")
print(f"Python: {sys.executable} ({sys.version.split()[0]})")
print()

# Step 1: Check and install dependencies
print("Step 1: Checking dependencies...")
try:
    import streamlit
    print(f"  ✓ Streamlit {streamlit.__version__}")
except ImportError:
    print("  ✗ Streamlit not found. Installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    import streamlit
    print(f"  ✓ Streamlit {streamlit.__version__} installed")

try:
    import pandas
    print(f"  ✓ pandas {pandas.__version__}")
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pandas"], check=True)
    print("  ✓ pandas installed")

try:
    import requests
    print(f"  ✓ requests {requests.__version__}")
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
    print("  ✓ requests installed")

try:
    from dotenv import load_dotenv
    print("  ✓ python-dotenv")
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "python-dotenv"], check=True)
    print("  ✓ python-dotenv installed")

print()

# Step 2: Test imports
print("Step 2: Testing imports...")
try:
    sys.path.insert(0, str(BASE_DIR))
    from app.utils.ui import setup_page, apply_theme
    print("  ✓ app.utils.ui")
except Exception as e:
    print(f"  ✗ app.utils.ui: {e}")
    sys.exit(1)

try:
    from app.utils.paths import ensure_dirs
    print("  ✓ app.utils.paths")
    ensure_dirs()
except Exception as e:
    print(f"  ✗ app.utils.paths: {e}")
    sys.exit(1)

try:
    from scan import init_db, get_db_path
    print("  ✓ scan module")
    db_path = get_db_path()
    init_db(db_path)
    print(f"  ✓ Database initialized at: {db_path}")
except Exception as e:
    print(f"  ⚠ Database initialization: {e} (may be okay)")

print()

# Step 3: Check port
print("Step 3: Checking port 8501...")
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('localhost', 8501))
sock.close()

if result == 0:
    print("  ⚠ Port 8501 is in use")
    print("  Attempting to free the port...")
    try:
        import psutil
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if any('streamlit' in str(arg).lower() or 'main.py' in str(arg) for arg in (proc.info.get('cmdline') or [])):
                    proc.kill()
                    print(f"  ✓ Killed process {proc.info['pid']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    except ImportError:
        pass
    
    # Try killing with lsof if available
    try:
        subprocess.run(["lsof", "-ti:8501"], check=False, capture_output=True)
        subprocess.run(["kill", "-9", "$(lsof -ti:8501)"], shell=True, check=False)
    except:
        pass
    
    import time
    time.sleep(2)
else:
    print("  ✓ Port 8501 is available")

print()

# Step 4: Start server
print("=" * 70)
print("Starting VirusLens Server...")
print("=" * 70)
print()
print("🌐 Access the app at: http://localhost:8501")
print()
print("Press Ctrl+C to stop the server")
print()
print("-" * 70)
print()

# Run streamlit
try:
    subprocess.run(
        [
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--server.headless", "true"
        ],
        cwd=BASE_DIR
    )
except KeyboardInterrupt:
    print("\n\n✓ Server stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

