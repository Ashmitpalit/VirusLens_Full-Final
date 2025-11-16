# 🚀 VirusLens - Complete Setup Guide (From Scratch)

This guide will walk you through setting up and running VirusLens from scratch.

---

## Step 1: Check Prerequisites ✅

### Verify Python Installation

**On macOS/Linux:**
```bash
python3 --version
```

**On Windows:**
```cmd
python --version
```

**Required:** Python 3.8 or higher (3.10+ recommended)

**If Python is not installed:**
- **macOS:** `brew install python3`
- **Linux (Ubuntu/Debian):** `sudo apt-get install python3 python3-pip python3-venv`
- **Windows:** Download from [python.org](https://www.python.org/downloads/)

---

## Step 2: Navigate to Project Directory 📁

```bash
cd /Users/ashmitpalit/VirusLens_Full-Final
```

Or wherever you have the project folder located.

---

## Step 3: Create Virtual Environment (Recommended) 🎯

**Why?** Keeps your project dependencies isolated from other projects.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**You'll know it's activated when you see `(venv)` in your terminal prompt.**

**To deactivate later:** Just type `deactivate`

---

## Step 4: Install Dependencies 📦

```bash
pip install -r requirements.txt
```

**On some systems, you may need:**
```bash
pip3 install -r requirements.txt
```

**This installs:**
- Streamlit (web framework)
- Pandas (data handling)
- Requests (API calls)
- ReportLab (PDF generation)
- And other required packages

**Expected time:** 1-2 minutes depending on your internet speed.

---

## Step 5: Configure API Keys (Optional but Recommended) 🔑

The app can work without API keys, but scanning features require a VirusTotal API key.

### Create `.env` file:

**On macOS/Linux:**
```bash
touch .env
```

**On Windows:**
```cmd
type nul > .env
```

### Edit the `.env` file and add:

```env
# VirusTotal API Key (Get free key from https://www.virustotal.com/gui/join-us)
VIRUSTOTAL_API_KEY=your_api_key_here

# Optional: URLScan.io API Key
# URLSCAN_API_KEY=your_urlscan_key_here

# Optional: AlienVault OTX API Key  
# OTX_API_KEY=your_otx_key_here
```

**How to get a VirusTotal API key:**
1. Go to https://www.virustotal.com/gui/join-us
2. Sign up for a free account
3. Go to your account settings
4. Copy your API key
5. Paste it in the `.env` file

**Note:** Without an API key, some features may not work. The app will show warnings but still run.

---

## Step 6: Run the Application 🏃

### Option A: Using the Run Script (Easiest)

**On macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

**On Windows:**
```cmd
run.bat
```

### Option B: Using Python Directly

**On macOS/Linux:**
```bash
python3 -m streamlit run main.py
```

**On Windows:**
```cmd
python -m streamlit run main.py
```

### Option C: Using the Python Run Script

```bash
python3 run.py
```

**Or with custom port:**
```bash
VL_PORT=8502 python3 run.py
```

---

## Step 7: Access the Application 🌐

Once the server starts, you'll see output like:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

**Open your web browser and go to:**
```
http://localhost:8501
```

The VirusLens interface should load!

---

## Step 8: Verify Everything Works ✅

1. **Check the homepage loads** - You should see "🛡️ VirusLens" title
2. **Check navigation sidebar** - Should see: Scan, Bulk, History, Reports, About
3. **Try clicking on "Scan"** - Should load the scan page
4. **Check for any error messages** - If you see API key warnings, that's okay for now

---

## Troubleshooting 🔧

### Problem: "Python not found" or "python3: command not found"

**Solution:**
- Make sure Python is installed (Step 1)
- On some systems, try `python` instead of `python3`
- Check your PATH environment variable

### Problem: "pip: command not found"

**Solution:**
```bash
python3 -m pip install -r requirements.txt
```

### Problem: "Port 8501 is already in use"

**Solution 1:** Kill the existing process
```bash
# macOS/Linux
lsof -ti:8501 | xargs kill -9

# Windows (find PID first)
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

**Solution 2:** Use a different port
```bash
VL_PORT=8502 python3 -m streamlit run main.py
```
Then access at `http://localhost:8502`

### Problem: Import errors

**Solution:**
1. Make sure you're in the project root directory
2. Make sure virtual environment is activated (if using one)
3. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

### Problem: ModuleNotFoundError

**Solution:**
```bash
pip install streamlit pandas requests python-dotenv reportlab sqlalchemy tldextract
```

### Problem: Database errors

**Solution:** The database is created automatically. If you see errors:
- Check file permissions in the project directory
- Try deleting `viruslens.db` and let it recreate

---

## Quick Reference Commands 📝

### Start the app:
```bash
python3 -m streamlit run main.py
```

### Stop the app:
Press `Ctrl+C` in the terminal where it's running

### Run on different port:
```bash
python3 -m streamlit run main.py --server.port 8502
```

### Run on network (accessible from other devices):
```bash
python3 -m streamlit run main.py --server.address 0.0.0.0
```

### Check if app is running:
```bash
curl http://localhost:8501
# Or just open browser to http://localhost:8501
```

---

## Project Structure 📂

```
VirusLens_Full-Final/
├── app/
│   ├── pages/          # Streamlit pages (Scan, History, Reports, etc.)
│   ├── utils/          # Utility functions
│   └── services/       # API integrations
├── main.py             # Main entry point ⭐ START HERE
├── run.py              # Python launcher
├── run.sh              # macOS/Linux launcher
├── run.bat             # Windows launcher
├── requirements.txt    # Dependencies
├── .env                # API keys (create this)
└── viruslens.db       # Database (auto-created)
```

---

## Next Steps 🎯

1. **Get API Keys:** Sign up for VirusTotal to enable scanning features
2. **Explore the App:** Try scanning a URL or file
3. **Check History:** View your scan history
4. **Generate Reports:** Create PDF reports of your scans

---

## Need Help? 🆘

- Check `SETUP.md` for detailed platform-specific instructions
- Check `README.md` for feature documentation
- Review error messages in the terminal output

---

**That's it! You should now have VirusLens running.** 🎉

