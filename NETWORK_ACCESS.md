# 🌐 Network Access Guide

Access VirusLens from any device on your local network!

## 🚀 Quick Start (Network Mode)

### Option 1: Use Network Launcher (Recommended)

**Windows:**
```cmd
run.bat --network
```

**macOS/Linux:**
```bash
./run.sh --network
```

**All Platforms (Python):**
```bash
python run_network.py
```

### Option 2: Use Environment Variable

**Windows:**
```cmd
set VL_ADDRESS=0.0.0.0
python run.py
```

**macOS/Linux:**
```bash
VL_ADDRESS=0.0.0.0 python3 run.py
```

### Option 3: Direct Streamlit Command

```bash
streamlit run main.py --server.address 0.0.0.0 --server.port 8501
```

## 📱 Accessing from Other Devices

Once the server is running in network mode, you'll see output like:

```
🌐 Network IP: 192.168.1.100
🔗 Access from other devices: http://192.168.1.100:8501
💻 Local access: http://localhost:8501
```

### From Your Phone/Tablet/Other Computer:

1. **Make sure you're on the same Wi-Fi network**
2. **Open a web browser**
3. **Enter the network URL** shown in the terminal:
   ```
   http://192.168.1.100:8501
   ```
   (Replace with your actual IP address)

## 🔍 Finding Your Network IP

### Automatic Detection

The network launcher automatically detects your IP. If you need to find it manually:

**Windows:**
```cmd
ipconfig
```
Look for "IPv4 Address" under your active network adapter.

**macOS/Linux:**
```bash
ifconfig
# or
ip addr show
# or
hostname -I
```

**Python (all platforms):**
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
s.close()
print(ip)
```

## 🔒 Security Notes

### Local Network Only

By default, the server is only accessible on your local network. This means:
- ✅ Safe for home/office networks
- ✅ Not accessible from the internet
- ✅ Only devices on the same Wi-Fi can access

### Firewall Configuration

You may need to allow the port through your firewall:

**Windows:**
1. Open Windows Defender Firewall
2. Click "Allow an app through firewall"
3. Add Python or allow port 8501

**macOS:**
1. System Preferences → Security & Privacy → Firewall
2. Click "Firewall Options"
3. Allow Python or add port 8501

**Linux:**
```bash
# Ubuntu/Debian
sudo ufw allow 8501

# Fedora/RHEL
sudo firewall-cmd --add-port=8501/tcp --permanent
sudo firewall-cmd --reload
```

## 🌍 Internet Access (Advanced)

⚠️ **Warning**: Exposing the server to the internet requires proper security measures.

### Using Port Forwarding

1. Configure your router to forward port 8501 to your computer's IP
2. Find your public IP: https://whatismyipaddress.com
3. Access from anywhere: `http://YOUR_PUBLIC_IP:8501`

### Using a Tunnel Service

For secure internet access, use a tunnel service:

**ngrok:**
```bash
ngrok http 8501
```

**Cloudflare Tunnel:**
```bash
cloudflared tunnel --url http://localhost:8501
```

## 🔧 Configuration

### Change Port

If port 8501 is in use:

**Windows:**
```cmd
set VL_PORT=8502
run.bat --network
```

**macOS/Linux:**
```bash
VL_PORT=8502 ./run.sh --network
```

### Change Address

Edit `.streamlit/config.toml`:
```toml
[server]
address = "0.0.0.0"  # All interfaces
# or
address = "192.168.1.100"  # Specific IP
port = 8501
```

## 🐛 Troubleshooting

### Can't Access from Other Devices

1. **Check firewall**: Make sure port 8501 is allowed
2. **Verify network**: Ensure devices are on the same network
3. **Check IP address**: Make sure you're using the correct network IP
4. **Try localhost first**: Test with `http://localhost:8501` on the host machine

### Connection Refused

- Server might not be running in network mode
- Check if `--server.address 0.0.0.0` is set
- Verify the server is actually running

### Port Already in Use

Change the port:
```bash
VL_PORT=8502 python run_network.py
```

## 📋 Quick Reference

| Command | Description |
|---------|-------------|
| `run.bat --network` | Windows network mode |
| `./run.sh --network` | Unix network mode |
| `python run_network.py` | Python network launcher |
| `VL_ADDRESS=0.0.0.0 python run.py` | Environment variable method |

## ✅ Testing Network Access

1. Start server in network mode
2. Note the network IP shown
3. On another device, open browser
4. Navigate to `http://NETWORK_IP:8501`
5. You should see the VirusLens interface!

---

**Enjoy accessing VirusLens from anywhere on your network!** 🎉

