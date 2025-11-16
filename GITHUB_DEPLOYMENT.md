# 🚀 Deploy VirusLens Using GitHub + Streamlit Cloud

Yes! You can host your VirusLens app using GitHub with Streamlit Cloud (free and easy).

---

## Step-by-Step: GitHub + Streamlit Cloud Deployment

### Step 1: Push Your Code to GitHub

#### 1.1 Create a GitHub Repository
1. Go to https://github.com
2. Sign in (or create an account)
3. Click the **"+"** icon → **"New repository"**
4. Repository name: `VirusLens` (or any name you like)
5. Description: "Cyber Threat Analyzer"
6. Choose **Public** or **Private**
7. **DO NOT** check "Add README" (you already have files)
8. Click **"Create repository"**

#### 1.2 Push Your Code to GitHub

**Option A: Using GitHub Desktop (Easiest)**
1. Download GitHub Desktop: https://desktop.github.com
2. Install and sign in
3. File → Add Local Repository
4. Select your VirusLens_Full-Final folder
5. Click "Publish repository"
6. Done!

**Option B: Using Git Command Line**

Open Command Prompt/Terminal in your project folder:

```cmd
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - VirusLens"

# Add GitHub repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/VirusLens.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** If you haven't configured Git:
```cmd
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### Step 2: Deploy on Streamlit Cloud

#### 2.1 Sign Up for Streamlit Cloud
1. Go to: https://share.streamlit.io/
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit Cloud to access your GitHub account

#### 2.2 Deploy Your App
1. Click **"New app"** button
2. Fill in the form:
   - **Repository:** Select your `VirusLens` repository
   - **Branch:** Select `main` (or `master`)
   - **Main file path:** `main.py`
   - **App URL:** Will be auto-generated (e.g., `viruslens.streamlit.app`)
3. Click **"Deploy"**

Streamlit will start building your app. Wait 1-2 minutes.

---

### Step 3: Configure API Keys (Secrets)

#### 3.1 Add Secrets to Streamlit Cloud
1. In your deployed app, click the **hamburger menu** (☰) → **"Settings"**
2. Click **"Secrets"** in the left sidebar
3. Paste this into the secrets editor:

```
VIRUSTOTAL_API_KEY=a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3
OTX_API_KEY=6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15
URLSCAN_API_KEY=019a6c59-7c00-752c-a20e-c33e8221f28e
MOCK_MODE=false
```

4. Click **"Save"**
5. Your app will automatically restart with the new secrets

---

### Step 4: Access Your Live App! 🎉

Your app is now live at:
```
https://your-app-name.streamlit.app
```

**Example:** `https://viruslens.streamlit.app`

---

## What Happens Next?

### Automatic Updates
- Every time you push code to GitHub, Streamlit Cloud automatically redeploys your app
- Just commit and push changes, and your live app updates in 1-2 minutes

### To Update Your App:
```cmd
# Make changes to your code
git add .
git commit -m "Update description"
git push
# Streamlit Cloud automatically redeploys!
```

---

## Important Notes

### ⚠️ Don't Commit Sensitive Files

Make sure `.env` is in `.gitignore`:

1. Create/edit `.gitignore` file in your project root:
```
.env
venv/
__pycache__/
*.pyc
*.db
.DS_Store
```

2. Commit the `.gitignore`:
```cmd
git add .gitignore
git commit -m "Add .gitignore"
git push
```

### ✅ Use Streamlit Secrets (Not .env File)
- `.env` file won't work on Streamlit Cloud
- Use **Secrets** in Streamlit Cloud settings (Step 3 above)
- Secrets are encrypted and secure

---

## Troubleshooting

### Problem: "App failed to load"
**Solution:**
- Check that `main.py` is in the root of your repository
- Verify all dependencies are in `requirements.txt`
- Check the deployment logs in Streamlit Cloud

### Problem: "API key not found"
**Solution:**
- Make sure you added secrets correctly in Streamlit Cloud Settings
- Secret names must match exactly: `VIRUSTOTAL_API_KEY` (all caps)
- Restart the app after adding secrets

### Problem: "Module not found"
**Solution:**
- Ensure all packages are in `requirements.txt`
- Check that your file structure matches what's expected

---

## Benefits of GitHub + Streamlit Cloud

✅ **Free** - No cost
✅ **HTTPS** - Automatic SSL certificates
✅ **Auto-deploy** - Updates on every git push
✅ **Easy** - Simple setup process
✅ **Custom domain** - Available (paid feature)
✅ **No server management** - Fully managed
✅ **Global CDN** - Fast loading worldwide

---

## Alternative: GitHub + Other Hosting Services

If you want alternatives to Streamlit Cloud:

### Railway.app
- Connect GitHub → Auto-deploy
- Free tier available
- Supports Docker

### Render.com
- Connect GitHub repository
- Free tier available
- Auto-deploy on push

### Heroku
- Connect GitHub
- Paid plans ($5+/month)
- Easy deployment

---

## Summary

1. **Push code to GitHub** → Create repo and push files
2. **Connect to Streamlit Cloud** → Sign in and deploy
3. **Add API keys** → Use Secrets in settings
4. **Your app is live!** → Access via `your-app.streamlit.app`

**That's it!** Your app is now hosted and accessible worldwide! 🌍

---

## Quick Commands Reference

```cmd
# Initial setup (one time)
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/VirusLens.git
git push -u origin main

# Future updates
git add .
git commit -m "Your update message"
git push
```

---

**Need help?** Check Streamlit Cloud docs: https://docs.streamlit.io/streamlit-community-cloud

