# 🚀 Audio-to-Image Service Deployment Guide

## 📋 Overview

This guide will help you deploy the complete audio-to-image service with:
- **Frontend**: Beautiful web interface for audio upload
- **Backend**: Node.js API server
- **Python Service**: AI-powered audio processing and image generation
- **Replicate Integration**: Real transcription and image generation

## 🛠️ Prerequisites

- **Node.js** (v16 or higher)
- **Python** (3.8 or higher)
- **Replicate API Key** (with credit)
- **DigitalOcean Droplet** (or other VPS)

## 📦 Installation

### 1. Clone and Setup

```bash
git clone <your-repo>
cd a2i
```

### 2. Python Service Setup

```bash
cd python_service

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
echo "REPLICATE_API_KEY=your_replicate_api_key_here" > .env

# Test the service
python app.py
```

### 3. Backend Setup

```bash
cd backend

# Install Node.js dependencies
npm install

# Build TypeScript
npm run build

# Test the backend
npm run dev
```

### 4. Frontend Setup

The frontend is already included in the `frontend/` directory and will be served by the backend.

## 🌐 Local Development

### Start Python Service
```bash
cd python_service
python app.py
# Service runs on http://localhost:5001
```

### Start Backend (with frontend)
```bash
cd backend
npm run dev
# Full application runs on http://localhost:3001
```

### Test the Complete Pipeline
1. Open http://localhost:3001 in your browser
2. Upload an audio file
3. Watch the magic happen! 🎵🎨

## 🚀 Production Deployment

### Option 1: DigitalOcean Droplet

#### 1. Create Droplet
- **Image**: Ubuntu 22.04 LTS
- **Size**: Basic (1GB RAM, 1 CPU) - minimum
- **Region**: Choose closest to your users

#### 2. Initial Server Setup
```bash
# SSH into your droplet
ssh root@your-droplet-ip

# Create user
adduser a2i
usermod -aG sudo a2i

# Switch to user
su - a2i
```

#### 3. Install Dependencies
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Python
sudo apt install python3 python3-pip python3-venv -y

# Install PM2 for process management
sudo npm install -g pm2

# Install Nginx
sudo apt install nginx -y
```

#### 4. Deploy Application
```bash
# Clone your repository
git clone <your-repo>
cd a2i

# Setup Python service
cd python_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env file
echo "REPLICATE_API_KEY=your_replicate_api_key_here" > .env

# Setup backend
cd ../backend
npm install
npm run build

# Create ecosystem file for PM2
cat > ecosystem.config.js << EOF
module.exports = {
  apps: [
    {
      name: 'a2i-python',
      cwd: '/home/a2i/a2i/python_service',
      script: 'python',
      args: 'app.py',
      env: {
        PORT: 5001
      }
    },
    {
      name: 'a2i-backend',
      cwd: '/home/a2i/a2i/backend',
      script: 'dist/index.js',
      env: {
        PORT: 3001,
        PYTHON_SERVICE_URL: 'http://localhost:5001'
      }
    }
  ]
};
EOF

# Start services with PM2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

#### 5. Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/a2i
```

Add this configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/a2i /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 6. Setup SSL (Optional but Recommended)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d your-domain.com
```

### Option 2: Docker Deployment

#### 1. Create Dockerfile for Python Service
```dockerfile
# python_service/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5001

CMD ["python", "app.py"]
```

#### 2. Create Dockerfile for Backend
```dockerfile
# backend/Dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 3001
CMD ["node", "dist/index.js"]
```

#### 3. Create docker-compose.yml
```yaml
version: '3.8'
services:
  python-service:
    build: ./python_service
    ports:
      - "5001:5001"
    environment:
      - REPLICATE_API_KEY=${REPLICATE_API_KEY}
    volumes:
      - ./python_service/uploads:/app/uploads

  backend:
    build: ./backend
    ports:
      - "3001:3001"
    environment:
      - PYTHON_SERVICE_URL=http://python-service:5001
    depends_on:
      - python-service
    volumes:
      - ./backend/uploads:/app/uploads

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./frontend:/usr/share/nginx/html
    depends_on:
      - backend
```

## 🔧 Environment Variables

### Python Service (.env)
```env
REPLICATE_API_KEY=your_replicate_api_key_here
```

### Backend (.env)
```env
PORT=3001
PYTHON_SERVICE_URL=http://localhost:5001
```

## 📊 Monitoring

### PM2 Commands
```bash
# View logs
pm2 logs

# Monitor processes
pm2 monit

# Restart services
pm2 restart all

# View status
pm2 status
```

### Nginx Logs
```bash
# Access logs
sudo tail -f /var/log/nginx/access.log

# Error logs
sudo tail -f /var/log/nginx/error.log
```

## 🔒 Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **Firewall**: Configure UFW firewall
3. **SSL**: Always use HTTPS in production
4. **Updates**: Keep system and dependencies updated
5. **Backups**: Regular backups of configuration and data

## 🚨 Troubleshooting

### Common Issues

1. **Python Service Not Starting**
   - Check if port 5001 is available
   - Verify REPLICATE_API_KEY is set
   - Check Python dependencies

2. **Backend Connection Issues**
   - Verify PYTHON_SERVICE_URL is correct
   - Check if Python service is running
   - Review CORS configuration

3. **Image Generation Fails**
   - Check Replicate API key and credit
   - Verify audio file format
   - Review Python service logs

### Log Locations
- **PM2**: `pm2 logs`
- **Nginx**: `/var/log/nginx/`
- **System**: `/var/log/syslog`

## 🎉 Success!

Your audio-to-image service is now deployed and ready to transform music into beautiful artwork! 🎵🎨

Visit your domain to start creating AI-generated art from audio files. 