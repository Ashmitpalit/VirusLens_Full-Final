# ⚙️ Streamlit Cloud Settings Guide

## What You Need to Check/Change:

### 1. Main File Path (Most Important!) ⚠️

In the **"General"** tab, look for **"Main file path"** setting:
- ✅ Should be: `main.py` (root level)
- ❌ Should NOT be: `app/main.py`

If it's wrong, change it to `main.py` and click **"Save changes"**

---

### 2. Python Version ⚠️

Currently showing: **Python 3.13**

**Recommended:** Change to **Python 3.11** or **3.10**

**Why?** Python 3.13 is very new and some packages might not support it yet.

**How to change:**
1. In the dropdown, select **"3.11"** or **"3.10"**
2. Click **"Save changes"**

**Note:** I've created `runtime.txt` with `python-3.11.0` - this will tell Streamlit Cloud to use Python 3.11 when you push to GitHub.

---

### 3. App URL ✅

Your app URL is: `viruslens---cyber-threat-analyzer-fyctspuqepbdldd7n8btne.streamlit.app`

You can customize this if you want (shorter name), or leave it as is.

---

### 4. Secrets (API Keys) 🔑

1. Click on **"Secrets"** in the left menu (in the pop-up)
2. Make sure your API keys are in TOML format:

```
VIRUSTOTAL_API_KEY = "a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3"

OTX_API_KEY = "6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15"

URLSCAN_API_KEY = "019a6c59-7c00-752c-a20e-c33e8221f28e"

MOCK_MODE = "false"
```

**Important:** Use TOML format (with spaces around `=` and quotes around values)

---

## Quick Fix Checklist:

1. ✅ Check **Main file path** = `main.py` (not `app/main.py`)
2. ✅ Change **Python version** to **3.11** or **3.10** (not 3.13)
3. ✅ Check **Secrets** tab - API keys in TOML format
4. ✅ Click **"Save changes"** button
5. ✅ Wait for app to redeploy (1-2 minutes)

---

## After Making Changes:

1. The app will automatically redeploy
2. Check the deployment logs if there are still errors
3. Your app should work at: `viruslens---cyber-threat-analyzer-fyctspuqepbdldd7n8btne.streamlit.app`

---

## If "Save changes" Button is Greyed Out:

1. Make a change first (like selecting different Python version)
2. The button will become active
3. Click it to save

---

**Need help?** The most common issues are:
- Wrong main file path (`app/main.py` instead of `main.py`)
- Python version too new (3.13 not supported by all packages)
- Secrets in wrong format (needs TOML format with quotes)

