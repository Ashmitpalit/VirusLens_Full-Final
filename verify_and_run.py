#!/usr/bin/env python3
"""Comprehensive verification and startup script"""
import sys
import subprocess
import os
from pathlib import Path

BASE = Path(__file__).parent.absolute()
os.chdir(BASE)

errors = []

# 1. Check Python
print(f"Python: {sys.version}")

# 2. Check/install dependencies  
deps = ['streamlit', 'pandas', 'requests', 'dotenv', 'reportlab']
for dep in deps:
    try:
        if dep == 'dotenv':
            __import__('dotenv')
        else:
            __import__(dep)
        print(f"✓ {dep}")
    except ImportError:
        print(f"✗ {dep} missing, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✓ {dep} installed")

# 3. Test imports
print("\nTesting imports...")
try:
    sys.path.insert(0, str(BASE))
    from app.utils.ui import setup_page, apply_theme
    from app.utils.paths import ensure_dirs
    ensure_dirs()
    print("✓ App modules")
except Exception as e:
    errors.append(f"App import: {e}")
    print(f"✗ App modules: {e}")

try:
    from scan import init_db, get_db_path
    db_path = get_db_path()
    init_db(db_path)
    print(f"✓ Database ready at {db_path}")
except Exception as e:
    print(f"⚠ Database: {e}")

# 4. Check port
import socket
s = socket.socket()
try:
    s.bind(('localhost', 8501))
    print("✓ Port 8501 available")
    s.close()
except:
    print("⚠ Port 8501 in use - may already be running")

if errors:
    print("\nErrors found:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("\n" + "="*60)
print("Starting VirusLens...")
print("Access at: http://localhost:8501")
print("="*60 + "\n")

subprocess.run([sys.executable, "-m", "streamlit", "run", "main.py",
               "--server.port", "8501", "--server.address", "localhost"])

