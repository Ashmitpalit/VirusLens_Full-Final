# 🛡️ VirusLens — Cyber Threat Analyzer

A modern, cross-platform web application for analyzing URLs and files for security threats using VirusTotal, URLScan.io, and AlienVault OTX.

## ✨ Features

- 🔍 **URL Scanning** - Analyze URLs for threats
- 📁 **File Scanning** - Upload and scan files by hash
- 📊 **Scan History** - View all your past scans
- 📄 **PDF Reports** - Generate professional PDF reports
- ⚡ **Bulk Operations** - Perform multiple scans at once
- 💾 **Local Database** - All scans saved locally in SQLite
- 🎨 **Modern UI** - Beautiful, minimalist Gen Z design

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   cd VirusLens_Full-Final
   ```

2. **Create virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys** (create `.env` file)
   ```env
   VIRUSTOTAL_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   # Windows
   run.bat
   
   # macOS/Linux
   chmod +x run.sh
   ./run.sh
   
   # Or use Python directly
   python -m streamlit run main.py
   ```

6. **Open in browser**
   ```
   http://localhost:8501
   ```

## 📖 Detailed Setup

See [SETUP.md](SETUP.md) for detailed cross-platform installation instructions.

## 🖥️ Cross-Platform Support

VirusLens works on:
- ✅ **Windows** (10/11)
- ✅ **macOS** (10.14+)
- ✅ **Linux** (Ubuntu, Fedora, Arch, etc.)

All file paths are handled automatically using Python's `pathlib` for cross-platform compatibility.

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
VIRUSTOTAL_API_KEY=your_api_key_here

# Optional
URLSCAN_API_KEY=your_urlscan_key
OTX_API_KEY=your_otx_key
VL_DB_FILE=./viruslens.db
VL_PORT=8501
VL_ADDRESS=localhost
```

### Streamlit Configuration

Edit `.streamlit/config.toml` to customize:
- Server address and port
- SSL certificates (optional)
- Other Streamlit settings

## 📁 Project Structure

```
VirusLens_Full-Final/
├── app/
│   ├── pages/          # Streamlit pages (Scan, History, Reports, etc.)
│   ├── utils/          # Utility functions and UI theme
│   ├── services/       # API integrations (VirusTotal, URLScan, OTX)
│   └── ...
├── main.py             # Main entry point
├── scan.py             # Database and scan functions
├── run.py              # Python launcher
├── run.bat             # Windows launcher
├── run.sh              # Unix launcher
├── requirements.txt    # Python dependencies
└── viruslens.db       # SQLite database (auto-created)
```

## 🎯 Usage

1. **Scan a URL**: Enter a URL and click "Scan URL"
2. **Scan a File**: Upload a file and click "Scan File"
3. **View History**: Check the History page for all past scans
4. **Generate Reports**: Select a scan and generate a PDF report

## 🛠️ Development

### Running in Mock Mode

To avoid hitting API rate limits during development:

```env
MOCK_MODE=true
```

### Database Location

The database is automatically created at:
- Project root: `./viruslens.db`
- Or custom location via `VL_DB_FILE` environment variable

## 📝 Requirements

- Python 3.8+
- See `requirements.txt` for full dependency list

## 🤝 Contributing

Contributions are welcome! Please ensure code is cross-platform compatible.

## 📄 License

See LICENSE file for details.

## 🆘 Troubleshooting

See [SETUP.md](SETUP.md) for detailed troubleshooting guide.

Common issues:
- **Port in use**: Change `VL_PORT` in `.env` or use `--server.port` flag
- **Import errors**: Ensure virtual environment is activated and dependencies installed
- **Database errors**: Check file permissions in project directory

## 🌟 Features in Detail

### Modern UI
- Glassmorphism design
- Smooth animations
- Gradient accents
- Responsive layout
- Dark theme

### Security
- Local database storage
- API key management
- Secure file handling
- Input validation

### Performance
- Efficient database queries
- Async-ready architecture
- Optimized PDF generation

---

**Made with ❤️ for cybersecurity professionals**
