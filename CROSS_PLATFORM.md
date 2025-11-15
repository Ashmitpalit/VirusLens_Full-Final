# Cross-Platform Compatibility Guide

VirusLens is designed to work seamlessly on **Windows**, **macOS**, and **Linux**. This document explains the cross-platform features and how they work.

## ✅ Cross-Platform Features

### 1. Path Handling

All file paths use Python's `pathlib.Path`, which automatically handles platform differences:

- **Windows**: Uses backslashes (`\`) internally, but `pathlib` handles conversion
- **macOS/Linux**: Uses forward slashes (`/`)
- **All platforms**: Code uses `/` operator for path joining (works everywhere)

**Example:**
```python
from pathlib import Path
db_path = Path(__file__).parent / "viruslens.db"  # Works on all platforms
```

### 2. Database Paths

The database location is automatically detected using cross-platform logic:

1. Environment variable `VL_DB_FILE` (if set)
2. Project root directory
3. Current working directory

**No hardcoded paths** - everything is relative or uses environment variables.

### 3. Script Launchers

Three launcher scripts are provided:

- **`run.bat`** - Windows batch script
- **`run.sh`** - Unix shell script (macOS/Linux)
- **`run.py`** - Python script (works on all platforms)

### 4. Configuration Files

- **`.env`** - Environment variables (works on all platforms)
- **`.streamlit/config.toml`** - Streamlit config (platform-agnostic)
- **`.streamlit/secrets.toml`** - No hardcoded paths (commented out)

## 🔧 Platform-Specific Notes

### Windows

- Use `python` command (not `python3`)
- Paths automatically use backslashes internally
- Batch script: `run.bat`
- Virtual environment: `venv\Scripts\activate`

### macOS

- Use `python3` command
- May need to install Python via Homebrew
- Shell script: `./run.sh` (make executable: `chmod +x run.sh`)
- Virtual environment: `source venv/bin/activate`

### Linux

- Use `python3` command
- Install via package manager (apt, dnf, pacman, etc.)
- Shell script: `./run.sh` (make executable: `chmod +x run.sh`)
- Virtual environment: `source venv/bin/activate`

## 🚀 Running on Different Platforms

### Windows
```cmd
run.bat
```

### macOS/Linux
```bash
chmod +x run.sh
./run.sh
```

### All Platforms (Python)
```bash
python -m streamlit run main.py
# or
python3 -m streamlit run main.py
```

## 📁 Directory Structure

The application creates directories automatically using cross-platform methods:

```
VirusLens_Full-Final/
├── viruslens.db          # Database (auto-created)
├── data/                 # Data directory (auto-created)
├── reports/              # Reports directory (auto-created)
├── certs/                # SSL certificates (optional)
└── ...
```

All directories are created using `pathlib.Path.mkdir(parents=True, exist_ok=True)` which works on all platforms.

## 🔍 Verification

Run the verification script to check your setup:

```bash
python verify_setup.py
# or
python3 verify_setup.py
```

This will check:
- ✅ Python version
- ✅ Dependencies
- ✅ Path handling
- ✅ Configuration files

## ⚙️ Environment Variables

All platform-specific configuration uses environment variables:

```bash
# Windows (Command Prompt)
set VIRUSTOTAL_API_KEY=your_key
set VL_PORT=8501

# Windows (PowerShell)
$env:VIRUSTOTAL_API_KEY="your_key"
$env:VL_PORT="8501"

# macOS/Linux
export VIRUSTOTAL_API_KEY=your_key
export VL_PORT=8501
```

Or use `.env` file (works on all platforms):
```env
VIRUSTOTAL_API_KEY=your_key
VL_PORT=8501
```

## 🐛 Troubleshooting

### Path Issues

If you encounter path-related errors:

1. **Check Python version**: Python 3.8+ required
2. **Use pathlib**: All paths should use `Path()` objects
3. **Avoid hardcoded paths**: Use relative paths or environment variables

### Database Location

The database is created at:
- Project root: `./viruslens.db`
- Or custom: Set `VL_DB_FILE` environment variable

### Port Conflicts

Change the port if 8501 is in use:

```bash
# Windows
set VL_PORT=8502 && python run.py

# macOS/Linux
VL_PORT=8502 python3 run.py
```

## ✅ Testing Cross-Platform Compatibility

The codebase has been tested for:

- ✅ Path operations (all use `pathlib.Path`)
- ✅ File I/O (all use `pathlib`)
- ✅ Database paths (relative paths)
- ✅ Environment variables (platform-agnostic)
- ✅ Script launchers (platform-specific scripts provided)

## 📝 Best Practices

1. **Always use `pathlib.Path`** for file operations
2. **Use environment variables** for configuration
3. **Avoid hardcoded paths** (especially Windows paths like `C:\Users\...`)
4. **Test on multiple platforms** if possible
5. **Use relative paths** when possible

## 🔗 Related Files

- `SETUP.md` - Detailed setup instructions
- `README.md` - Project overview
- `verify_setup.py` - Setup verification script
- `run.py` - Cross-platform Python launcher
- `run.bat` - Windows launcher
- `run.sh` - Unix launcher

---

**All code is designed to work on Windows, macOS, and Linux without modification.**

