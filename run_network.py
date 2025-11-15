#!/usr/bin/env python3
"""
Network-enabled launcher for VirusLens.
Automatically detects your network IP and starts the server accessible from other devices.
"""
import os
import sys
import socket
import subprocess
from pathlib import Path

def get_local_ip():
    """Get the local network IP address."""
    try:
        # Connect to a remote address to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't actually connect, just determines the route
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        # Fallback: try to get hostname IP
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        except Exception:
            return "localhost"

def main():
    BASE_DIR = Path(__file__).resolve().parent
    APP = os.getenv("VL_APP", "main.py")
    PORT = int(os.getenv("VL_PORT", "8501"))
    
    # Get network IP
    network_ip = get_local_ip()
    
    print("=" * 60)
    print("🛡️  VirusLens - Network Mode")
    print("=" * 60)
    print(f"\n🌐 Starting server on all network interfaces...")
    print(f"📡 Your network IP: {network_ip}")
    print(f"🔗 Access from other devices:")
    print(f"   http://{network_ip}:{PORT}")
    print(f"\n💻 Local access:")
    print(f"   http://localhost:{PORT}")
    print("\n" + "=" * 60)
    print("Press Ctrl+C to stop the server\n")
    
    # Start Streamlit on all interfaces (0.0.0.0)
    args = [
        sys.executable, "-m", "streamlit", "run", str(BASE_DIR / APP),
        "--server.address", "0.0.0.0",
        "--server.port", str(PORT),
    ]
    
    try:
        subprocess.call(args)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped.")
        return 0
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

