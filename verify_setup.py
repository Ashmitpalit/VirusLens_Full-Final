#!/usr/bin/env python3
"""
Cross-platform setup verification script for VirusLens.
Run this to verify your installation is correct.
"""

import sys
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required. Found: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_dependencies():
    """Check if required packages are installed."""
    required = [
        'streamlit',
        'pandas',
        'sqlalchemy',
        'requests',
        'reportlab',
        'dotenv'
    ]
    missing = []
    for package in required:
        try:
            if package == 'dotenv':
                __import__('dotenv')
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - not installed")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print("   Install with: pip install -r requirements.txt")
        return False
    return True

def check_paths():
    """Verify cross-platform path handling."""
    print("\n📁 Checking paths...")
    try:
        # Test pathlib operations
        base = Path(__file__).resolve().parent
        db_path = base / "viruslens.db"
        data_dir = base / "data"
        reports_dir = base / "reports"
        
        print(f"✅ Project root: {base}")
        print(f"✅ Database path: {db_path}")
        print(f"✅ Data directory: {data_dir}")
        print(f"✅ Reports directory: {reports_dir}")
        
        # Test cross-platform path joining
        test_path = base / "app" / "pages" / "01_Scan.py"
        if test_path.exists():
            print(f"✅ Found scan page: {test_path}")
        else:
            print(f"⚠️  Scan page not found at: {test_path}")
        
        return True
    except Exception as e:
        print(f"❌ Path check failed: {e}")
        return False

def check_config():
    """Check configuration files."""
    print("\n⚙️  Checking configuration...")
    base = Path(__file__).resolve().parent
    
    # Check .env file
    env_file = base / ".env"
    if env_file.exists():
        print(f"✅ Found .env file")
    else:
        print(f"⚠️  .env file not found (create it with VIRUSTOTAL_API_KEY)")
    
    # Check .streamlit/config.toml
    config_file = base / ".streamlit" / "config.toml"
    if config_file.exists():
        print(f"✅ Found Streamlit config")
    else:
        print(f"⚠️  Streamlit config not found (will use defaults)")
    
    return True

def main():
    """Run all checks."""
    print("=" * 60)
    print("🛡️  VirusLens - Cross-Platform Setup Verification")
    print("=" * 60)
    print(f"\n🖥️  Platform: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.executable}\n")
    
    all_ok = True
    
    print("📦 Checking Python version...")
    if not check_python_version():
        all_ok = False
    
    print("\n📚 Checking dependencies...")
    if not check_dependencies():
        all_ok = False
    
    if not check_paths():
        all_ok = False
    
    if not check_config():
        all_ok = False
    
    print("\n" + "=" * 60)
    if all_ok:
        print("✅ All checks passed! You're ready to run VirusLens.")
        print("\n🚀 To start the app:")
        print("   Windows:   run.bat")
        print("   macOS/Linux: ./run.sh")
        print("   Or:        python -m streamlit run main.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\n📖 See SETUP.md for detailed instructions.")
    print("=" * 60)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())

