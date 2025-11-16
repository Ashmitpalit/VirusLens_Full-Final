# 🔑 How to Set Up Your VirusTotal API Key

## Quick Setup (Choose One Method)

### Method 1: Using .env File (Recommended)

1. **Open the `.env` file** in the project root folder
2. **Replace `your_api_key_here`** with your actual VirusTotal API key:

```env
VIRUSTOTAL_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

3. **Save the file**
4. **Restart the Streamlit server** (press Ctrl+C and run again)

### Method 2: Using Streamlit Secrets

1. **Open the `.streamlit/secrets.toml` file** in the project folder
2. **Replace `your_api_key_here`** with your actual API key:

```toml
VIRUSTOTAL_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
```

3. **Save the file**
4. **Restart the Streamlit server**

---

## 🔐 How to Get Your VirusTotal API Key (FREE)

1. **Go to VirusTotal**: https://www.virustotal.com/gui/join-us
2. **Sign up** for a free account (or log in if you already have one)
3. **Go to your profile** (click your username in top right → Settings)
4. **Find "API Key"** section
5. **Copy your API key**
6. **Paste it** into `.env` or `.streamlit/secrets.toml`

---

## ✅ Verify Setup

After adding your API key:
1. Restart the Streamlit server
2. The warning message should disappear
3. Try scanning a URL to verify it works

---

## 📝 Notes

- **Free tier** allows limited requests per day (usually 500/day)
- **The app will still run** without an API key, but scanning features won't work
- **Keep your API key secret** - don't commit it to version control
- Both `.env` and `.streamlit/secrets.toml` are in `.gitignore` by default

---

## 🆘 Troubleshooting

**Still seeing the error?**
- Make sure you saved the file
- Make sure you restarted the server
- Check for typos in the API key
- Verify the API key is active in your VirusTotal account

