# 📋 Step-by-Step: Start VirusLens From Scratch

## Complete Checklist ✅

### Pre-Setup (5 minutes)

- [ ] **Step 1:** Verify Python 3.8+ is installed
  ```bash
  python3 --version
  ```
  ✅ You should see: `Python 3.x.x`

- [ ] **Step 2:** Navigate to project folder
  ```bash
  cd /Users/ashmitpalit/VirusLens_Full-Final
  ```
  ✅ You should be in the project directory

---

### Automated Setup (Choose ONE method)

#### 🚀 Method A: Quick Start Script (EASIEST)

**On macOS/Linux:**
```bash
./quick_start.sh
```

**On Windows:**
```cmd
quick_start.bat
```

**Done!** The script will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create .env file template
- ✅ Start the server

Then open: http://localhost:8501

---

#### 🔧 Method B: Manual Setup (Learn Each Step)

**Step 3: Create Virtual Environment (Recommended)**
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
✅ You should see `(venv)` in your terminal prompt

**Step 4: Install Dependencies**
```bash
pip install -r requirements.txt
```
✅ Wait for installation to complete (1-2 minutes)

**Step 5: Create .env File (Optional but Recommended)**
```bash
# Create the file
touch .env    # macOS/Linux
# or
type nul > .env    # Windows
```

**Edit .env and add:**
```env
VIRUSTOTAL_API_KEY=your_actual_api_key_here
```

✅ Save the file

**Step 6: Run the Application**
```bash
python3 -m streamlit run main.py
```
✅ Server should start and show: `Local URL: http://localhost:8501`

**Step 7: Open in Browser**
- Open your web browser
- Go to: `http://localhost:8501`
✅ You should see the VirusLens homepage!

---

## 🎯 What Each Step Does

| Step | Purpose | Time |
|------|---------|------|
| 1. Check Python | Verify Python is installed | 10 sec |
| 2. Navigate | Get to project folder | 5 sec |
| 3. Virtual Env | Isolate dependencies | 30 sec |
| 4. Install Deps | Get all required packages | 1-2 min |
| 5. Create .env | Store API keys | 1 min |
| 6. Run App | Start the server | 10 sec |
| 7. Open Browser | Access the app | 5 sec |

**Total Time: ~3-5 minutes**

---

## 🔍 Verification Checklist

After setup, verify:

- [ ] Python is installed and accessible
- [ ] Virtual environment is created (if using)
- [ ] Virtual environment is activated (if using)
- [ ] All packages installed successfully (no errors)
- [ ] .env file exists (optional)
- [ ] Server starts without errors
- [ ] Browser can access http://localhost:8501
- [ ] Homepage loads correctly
- [ ] Navigation sidebar is visible

---

## 🆘 Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| Python not found | Install Python 3.8+ from python.org |
| pip not found | Use `python3 -m pip` instead |
| Port 8501 in use | Kill existing process or use port 8502 |
| Import errors | Activate venv and reinstall: `pip install -r requirements.txt --force-reinstall` |
| Permission denied | On Linux/Mac: `chmod +x quick_start.sh` |
| ModuleNotFoundError | Install missing package: `pip install <package-name>` |

---

## 📞 Need Help?

1. Check `START_HERE.md` for detailed explanations
2. Check `SETUP.md` for platform-specific notes
3. Check terminal output for error messages
4. Verify you're in the correct directory
5. Make sure Python 3.8+ is installed

---

## 🎉 Success!

If you can access http://localhost:8501 and see the VirusLens interface, you're all set!

**Next Steps:**
1. Get a VirusTotal API key for scanning features
2. Try scanning a URL
3. Explore the History page
4. Generate a PDF report

