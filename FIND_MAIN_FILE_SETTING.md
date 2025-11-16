# 🔍 How to Find/Set Main File Path in Streamlit Cloud

## Why You Can't Find It:

The **"Main file path"** setting might not be visible if:
1. It's already set correctly (`main.py` by default)
2. It's only shown during app creation
3. It needs to be checked in a different way

---

## How to Check/Change Main File Path:

### Method 1: Check During Deployment

If you create a **NEW** app, you'll see "Main file path" during setup:
- Default is usually `main.py` if it exists in root

### Method 2: Check App Status/Logs

1. Go to your Streamlit Cloud dashboard
2. Click on your app
3. Click **"Manage app"** button (bottom right or in menu)
4. Look at the deployment info - it should show what file is being run

### Method 3: Check Your Repository Structure

Streamlit Cloud automatically looks for `main.py` in the root. Make sure:
- ✅ `main.py` exists in the root folder
- ❌ NOT `app/main.py` (that's wrong)

---

## What to Do:

### If Main File Path Can't Be Found in Settings:

1. **Make sure `main.py` exists in root:**
   - Check that `main.py` is in the root of your GitHub repository
   - NOT inside the `app/` folder

2. **The default should work:**
   - Streamlit Cloud automatically uses `main.py` in the root
   - If your repo has `main.py` in root, it should work

3. **If you have the wrong file:**
   - You might need to delete and recreate the app
   - Or rename/delete `app/main.py` to avoid conflicts

---

## Quick Fix Steps:

### Option 1: Delete and Recreate App (If Wrong File is Used)

1. Go to Streamlit Cloud dashboard
2. Click on your app
3. Click **"Settings"** → **"Delete app"**
4. Create new app
5. During creation, it will ask for "Main file path"
6. Enter: `main.py`
7. Deploy!

### Option 2: Verify Root main.py Exists

Make sure your repository has `main.py` in the root (same level as `app/` folder):

```
VirusLens/
├── main.py          ← This should be the main file
├── app/
│   ├── main.py      ← This is conflicting (delete or rename)
│   └── ...
├── requirements.txt
└── ...
```

### Option 3: Delete Conflicting app/main.py

If `app/main.py` is causing the issue:

1. **Rename or delete it:**
   ```cmd
   # In your local project
   # Option A: Delete it
   rm app/main.py
   
   # Option B: Rename it
   mv app/main.py app/main_old.py
   ```

2. **Push to GitHub:**
   ```cmd
   git add .
   git commit -m "Remove conflicting app/main.py"
   git push
   ```

3. **Streamlit Cloud will redeploy with root main.py**

---

## How to Verify What's Being Used:

1. Look at deployment logs in Streamlit Cloud
2. The error message will show which file it tried to run
3. If it shows `app/main.py`, that's the problem
4. If it shows `main.py`, that's correct

---

## Summary:

- **Main file path** might not be visible if already set
- **Default** is `main.py` in root (should work automatically)
- **Problem** might be conflicting `app/main.py` file
- **Solution**: Delete/rename `app/main.py` and push to GitHub

The most likely issue: You have both `main.py` (root) AND `app/main.py`, and Streamlit Cloud might be picking the wrong one. Delete `app/main.py` and it should work!

