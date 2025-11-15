# 📱 Mobile Access Guide

Access VirusLens from your phone, tablet, or any mobile device!

## ✅ Yes, You Can Run It on Your Phone!

VirusLens is a web application, so you can access it from **any device with a web browser**, including:
- 📱 **iPhone/iPad** (Safari)
- 🤖 **Android phones/tablets** (Chrome, Firefox, etc.)
- 💻 **Any device with a browser**

## 🚀 Quick Setup

### Step 1: Start Server in Network Mode

On your computer, run:

```bash
# Option 1: Network launcher (shows your IP)
python3 run_network.py

# Option 2: Using script
./run.sh --network

# Option 3: Direct command
streamlit run main.py --server.address 0.0.0.0 --server.port 8501
```

You'll see output like:
```
🌐 Network IP: 192.168.150.85
🔗 Access from other devices: http://192.168.150.85:8501
```

### Step 2: Connect Your Phone

1. **Make sure your phone is on the same Wi-Fi network** as your computer
2. **Open your phone's web browser** (Safari on iPhone, Chrome on Android)
3. **Type the network URL** shown in the terminal:
   ```
   http://192.168.150.85:8501
   ```
   (Replace with your actual IP address)

### Step 3: Access the App!

The VirusLens interface will load on your phone, fully functional!

## 📱 Mobile-Optimized Features

The app is **responsive** and works great on mobile:
- ✅ Touch-friendly interface
- ✅ Responsive layout
- ✅ Mobile-optimized buttons
- ✅ Easy navigation
- ✅ File upload works on mobile
- ✅ All features accessible

## 🔍 Finding Your Network IP

If you need to find your computer's IP address:

**On your computer, run:**
```bash
# macOS/Linux
python3 -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0]); s.close()"

# Windows
ipconfig
# Look for "IPv4 Address" under your active network adapter
```

## 🌐 Common Network IPs

Your IP will typically look like:
- `192.168.1.XXX`
- `192.168.0.XXX`
- `10.0.0.XXX`
- `172.16.XXX.XXX`

## 📋 Quick Reference

| Device | Browser | URL Format |
|--------|---------|------------|
| iPhone | Safari | `http://192.168.150.85:8501` |
| Android | Chrome | `http://192.168.150.85:8501` |
| iPad | Safari | `http://192.168.150.85:8501` |
| Any | Any | `http://YOUR_IP:8501` |

## 🎯 Using on Mobile

### Scanning URLs
1. Tap the URL input field
2. Type or paste the URL
3. Tap "🔍 Scan URL"

### Scanning Files
1. Tap "Upload a file"
2. Choose from:
   - **Photos** (on iPhone/Android)
   - **Files** (file manager)
   - **Camera** (take a photo)
3. Tap "🔍 Scan File"

### Viewing History
- Swipe to scroll through scan history
- Tap any scan to view details

### Generating Reports
- Select a scan
- Tap "📥 Generate Report PDF"
- Download opens in your phone's browser

## 🔒 Security

- ✅ **Local network only** - Only devices on your Wi-Fi can access
- ✅ **Not exposed to internet** - Safe and secure
- ✅ **No data leaves your network** - Everything stays local

## 🐛 Troubleshooting

### Can't Connect from Phone

1. **Check Wi-Fi**: Phone and computer must be on same network
2. **Check IP**: Make sure you're using the correct IP address
3. **Check Firewall**: Allow port 8501 through firewall
4. **Try localhost first**: Test `http://localhost:8501` on computer

### Connection Timeout

- Server might not be running in network mode
- Make sure you used `--network` flag or `0.0.0.0` address
- Check if server is actually running

### Page Won't Load

- Try refreshing the page
- Clear browser cache
- Make sure URL includes `http://` (not `https://`)

## 💡 Pro Tips

1. **Bookmark the URL** on your phone for quick access
2. **Add to Home Screen** (iOS/Android) for app-like experience
3. **Use QR Code** to share the URL easily
4. **Keep server running** while using on mobile

## 📲 Adding to Home Screen

### iPhone/iPad
1. Open the app in Safari
2. Tap the Share button
3. Select "Add to Home Screen"
4. Tap "Add"

### Android
1. Open the app in Chrome
2. Tap the menu (3 dots)
3. Select "Add to Home screen"
4. Tap "Add"

Now you have a VirusLens icon on your home screen!

## ✅ Quick Checklist

- [ ] Server running in network mode (`0.0.0.0`)
- [ ] Phone on same Wi-Fi network
- [ ] Firewall allows port 8501
- [ ] Using correct IP address
- [ ] Browser supports modern web features

---

**Enjoy using VirusLens on your phone!** 📱✨

