# 🚀 VirusLens Hosting Guide

Complete guide to host VirusLens on various platforms.

---

## Option 1: Streamlit Cloud (Easiest & Free) ⭐ Recommended

**Best for:** Quick deployment, free tier, zero maintenance

### Step-by-Step:

1. **Push your code to GitHub**
   - Create a GitHub repository
   - Push your VirusLens code to GitHub

2. **Sign up for Streamlit Cloud**
   - Go to: https://share.streamlit.io/
   - Sign in with your GitHub account

3. **Deploy**
   - Click "New app"
   - Select your GitHub repository
   - Select branch: `main`
   - Main file path: `main.py`
   - Click "Deploy"

4. **Configure Secrets (API Keys)**
   - In your deployed app, click "Settings" → "Secrets"
   - Add your API keys:
     ```
     VIRUSTOTAL_API_KEY=a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3
     OTX_API_KEY=6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15
     URLSCAN_API_KEY=019a6c59-7c00-752c-a20e-c33e8221f28e
     ```
   - Save and the app will restart automatically

5. **Access your app**
   - Your app will be live at: `https://your-app-name.streamlit.app`
   - Free, automatic HTTPS, custom domain support available

**Pros:** Free, easy, auto-deploys on git push, HTTPS included
**Cons:** Limited customization, Streamlit branding

---

## Option 2: Docker + VPS/Cloud (Full Control)

**Best for:** Production deployment, custom domain, full control

### Using Docker with VPS (DigitalOcean, AWS, etc.)

#### Step 1: Fix Dockerfile
First, update the Dockerfile (it references wrong path):

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
EXPOSE 8501
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Step 2: Create .dockerignore
```
venv/
__pycache__/
*.pyc
*.db
.env
.git/
```

#### Step 3: Build Docker Image
```bash
docker build -t viruslens .
```

#### Step 4: Run Container
```bash
docker run -d \
  -p 8501:8501 \
  -e VIRUSTOTAL_API_KEY=your_key \
  -e OTX_API_KEY=your_key \
  -e URLSCAN_API_KEY=your_key \
  --name viruslens \
  viruslens
```

#### Step 5: Deploy to VPS

**DigitalOcean Droplet:**
1. Create a Droplet (Ubuntu 22.04)
2. SSH into your server
3. Install Docker: `curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh`
4. Upload your code (or clone from GitHub)
5. Build and run as above

**AWS EC2:**
1. Launch EC2 instance (Ubuntu)
2. Configure security group (allow port 8501)
3. SSH into instance
4. Install Docker and deploy

**Access:** `http://your-server-ip:8501`

#### Step 6: Add Nginx Reverse Proxy (Optional, for HTTPS)

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Use Let's Encrypt for free SSL:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

---

## Option 3: Heroku

**Best for:** Easy deployment, free tier (limited hours)

### Step 1: Create Procfile
Create `Procfile` in project root:
```
web: streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
```

### Step 2: Create runtime.txt (Optional)
```
python-3.11.0
```

### Step 3: Install Heroku CLI
- Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 4: Deploy
```bash
heroku login
heroku create your-app-name
heroku config:set VIRUSTOTAL_API_KEY=your_key
heroku config:set OTX_API_KEY=your_key
heroku config:set URLSCAN_API_KEY=your_key
git push heroku main
heroku open
```

**Note:** Heroku free tier ended, paid plans start at $5/month

---

## Option 4: Railway.app

**Best for:** Easy Docker deployment, free tier

### Steps:
1. Sign up at https://railway.app
2. Create new project
3. Connect GitHub repository
4. Railway auto-detects Dockerfile
5. Add environment variables (API keys) in settings
6. Deploy!

---

## Option 5: Render.com

**Best for:** Free tier, easy deployment

### Steps:
1. Sign up at https://render.com
2. Create new Web Service
3. Connect GitHub repository
4. Build command: `pip install -r requirements.txt`
5. Start command: `streamlit run main.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variables
7. Deploy!

---

## Option 6: Google Cloud Run

**Best for:** Serverless, pay-per-use

### Steps:
1. Install gcloud CLI
2. Build container:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR-PROJECT/viruslens
   ```
3. Deploy:
   ```bash
   gcloud run deploy viruslens \
     --image gcr.io/YOUR-PROJECT/viruslens \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars VIRUSTOTAL_API_KEY=your_key,OTX_API_KEY=your_key,URLSCAN_API_KEY=your_key
   ```

---

## Option 7: AWS Elastic Beanstalk

**Best for:** AWS ecosystem integration

### Steps:
1. Install AWS CLI and EB CLI
2. Initialize:
   ```bash
   eb init -p python-3.11 viruslens
   ```
3. Create environment:
   ```bash
   eb create viruslens-env
   ```
4. Set environment variables:
   ```bash
   eb setenv VIRUSTOTAL_API_KEY=your_key OTX_API_KEY=your_key URLSCAN_API_KEY=your_key
   ```
5. Deploy:
   ```bash
   eb deploy
   ```

---

## Quick Comparison

| Platform | Cost | Difficulty | Best For |
|----------|------|------------|----------|
| **Streamlit Cloud** | Free | ⭐ Easy | Quick deployment |
| **Railway** | Free tier | ⭐⭐ Easy | Docker deployment |
| **Render** | Free tier | ⭐⭐ Easy | Simple hosting |
| **Heroku** | $5+/month | ⭐⭐ Easy | Legacy support |
| **VPS (DigitalOcean)** | $4+/month | ⭐⭐⭐ Medium | Full control |
| **AWS/GCP** | Pay-per-use | ⭐⭐⭐⭐ Hard | Enterprise |

---

## Recommended Setup for Production

1. **Use Streamlit Cloud** for quick deployment (free)
2. **Or use DigitalOcean + Docker + Nginx** for full control (~$6/month)

---

## Important Notes

1. **Never commit API keys to GitHub** - Use environment variables or secrets
2. **Enable HTTPS** for production (Streamlit Cloud includes this)
3. **Use a reverse proxy** (Nginx) for custom domains and SSL
4. **Monitor resource usage** - Streamlit apps can be memory-intensive
5. **Set up backups** for your database file

---

## Troubleshooting

### Port binding issues:
- Use `0.0.0.0` as server address, not `localhost`
- Check firewall rules allow port 8501

### API keys not working:
- Verify environment variables are set correctly
- Restart the server after setting env vars

### Memory issues:
- Upgrade to larger instance/server
- Optimize Streamlit caching

---

**Need help?** Check platform-specific documentation or contact support.

