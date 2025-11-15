# VirusLens - Cross-Platform Setup Guide

VirusLens is a modern Cyber Threat Analyzer that works on **Windows**, **macOS**, and **Linux**.

## Prerequisites

- **Python 3.8 or higher** (Python 3.10+ recommended)
- **pip** (Python package manager)

### Check Python Installation

**Windows:**
```cmd
python --version
```

**macOS/Linux:**
```bash
python3 --version
```

## Installation

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd VirusLens_Full-Final

# Or extract the downloaded ZIP file
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or if using pip3:
```bash
pip3 install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

Create a `.env` file in the project root:

```env
# VirusTotal API Key (Required for scanning)
VIRUSTOTAL_API_KEY=your_api_key_here

# Optional: URLScan.io API Key
URLSCAN_API_KEY=your_urlscan_key_here

# Optional: AlienVault OTX API Key
OTX_API_KEY=your_otx_key_here

# Optional: Custom database location
# VL_DB_FILE=./viruslens.db
```

## Running the Application

### Option 1: Using Platform-Specific Scripts

**Windows:**
```cmd
run.bat
```

**macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### Option 2: Using Python Directly

**Windows:**
```cmd
python -m streamlit run main.py
```

**macOS/Linux:**
```bash
python3 -m streamlit run main.py
```

### Option 3: Using the Python Run Script

```bash
python run.py
```

Or with custom settings:
```bash
# Windows
set VL_PORT=8502 && python run.py

# macOS/Linux
VL_PORT=8502 python3 run.py
```

## Accessing the Application

Once started, open your browser and navigate to:

```
http://localhost:8501
```

## Platform-Specific Notes

### Windows

- Use `python` instead of `python3`
- Paths use backslashes (`\`) but Python's `pathlib` handles this automatically
- If you encounter permission errors, run Command Prompt as Administrator

### macOS

- Use `python3` command
- May need to install Python via Homebrew: `brew install python3`
- If you get SSL certificate errors, update certificates: `/Applications/Python\ 3.x/Install\ Certificates.command`

### Linux

- Use `python3` command
- Install Python 3.8+ via your package manager:
  - **Ubuntu/Debian:** `sudo apt-get install python3 python3-pip python3-venv`
  - **Fedora/RHEL:** `sudo dnf install python3 python3-pip`
  - **Arch:** `sudo pacman -S python python-pip`

## Troubleshooting

### Port Already in Use

If port 8501 is already in use, change it:

```bash
# Windows
set VL_PORT=8502 && python run.py

# macOS/Linux
VL_PORT=8502 python3 run.py
```

### Database Location

The database file (`viruslens.db`) is created automatically in the project root. To use a custom location:

1. Set environment variable: `VL_DB_FILE=/path/to/database.db`
2. Or edit `.streamlit/secrets.toml` (not recommended for cross-platform)

### Import Errors

If you get import errors:

1. Make sure you're in the project root directory
2. Activate your virtual environment
3. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

### Streamlit Not Found

If Streamlit is not found:

```bash
pip install streamlit
```

Or reinstall all requirements:
```bash
pip install -r requirements.txt
```

## Development Mode

For development without hitting API rate limits, set in `.env`:

```env
MOCK_MODE=true
```

## File Structure

```
VirusLens_Full-Final/
├── app/
│   ├── pages/          # Streamlit pages
│   ├── utils/          # Utility functions
│   └── ...
├── main.py             # Main entry point
├── run.py              # Python launcher
├── run.bat             # Windows launcher
├── run.sh              # Unix launcher
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (create this)
└── viruslens.db       # Database (created automatically)
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure Python 3.8+ is installed
4. Check that port 8501 is available

## License

See LICENSE file for details.

