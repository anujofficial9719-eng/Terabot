# 🚀 Terabox Downloader Bot

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)

**Terabox Downloader Bot** is a fully automated Telegram bot for downloading Terabox files and folders directly to Telegram. Supports bulk downloads, folder links, auto login, and premium plan management.

---

## 🗂 Features

### Core
- 🔐 Auto login & cookie management (`ndus` cookie handled automatically)
- ⚡ Fast downloads using `aria2` with multiple connections
- 📂 Folder & multiple file link support
- ⏱ No waiting queue
- 🌐 Bulk link processing
- 🆓 Unlimited downloads
- 📤 Auto upload to Telegram
- 💾 Temporary storage in `/downloads`  
- 🧹 Automatic cleanup after upload
- ⚠️ Maximum 2GB per file (configurable in `bot.py`)

### Plans System
- **Categories:** Regular, Creator  
- **Regular Plans:**
  - 🎟 Bronze — 12 Days ₹19
  - 🥈 Silver — 30 Days ₹39
  - 🥇 Silver Plus — 45 Days ₹59
  - 🏅 Gold — 60 Days ₹79
  - 👑 Platinum — 90 Days ₹99
  - 💎 Diamond — 150 Days ₹149
  - 🚀 Ultimate — 200 Days ₹199

- **Creator Plans (Extra Features):**
  - Access to `/settings`  
  - Custom dump channel  
  - Auto-forward downloads to your channel  
  - Includes all Regular Plan features  
- Plans range from Creator Bronze ₹39 to Creator Ultimate ₹499

---

## 🛠 Requirements

- Python 3.11+
- Install dependencies:
```bash
pip install -r requirements.txt

pyrogram==2.0.106
tgcrypto==1.2.5
requests==2.31.0
flask==2.3.3
aria2p==0.11.3
aiohttp==3.9.5
beautifulsoup4==4.12.3
selenium==4.11.2
webdriver-manager==4.10.1

⚙ Setup

git clone https://github.com/anujofficial9719-eng/Terabot.git
cd Terabot

comfig.py

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
TB_EMAIL = "your_email"
TB_PASSWORD = "your_password"
DOWNLOAD_DIR = "downloads/"

📁 Folder Structure

terabot/
│
├── bot.py           # Telegram bot logic
├── api.py           # Flask API
├── extractor.py     # Terabox link resolver
├── downloader.py    # Aria2 download engine
├── login.py         # Auto login & cookie
├── config.py        # Configuration
├── requirements.txt # Dependencies
├── start.sh         # Startup script
├── README.md        # Documentation
├── cookies.txt      # Auto-generated cookie
├── downloads/       # Temporary storage
├── logs/            # Logs (bot.log, api.log)
└── .env             # Optional environment variables

💡 Usage
Add the bot to Telegram
Send Terabox file/folder link
Bot automatically:
Logs in (if needed)
Resolves link
Downloads via Aria2
Uploads files to Telegram
Use /plans to view plan categories and individual plan details.
🔒 Security
Auto cookie management (manual edits not required)
Recommended: store credentials in .env
Max file size: 2GB per upload (adjustable)
📜 License
MIT License — Free for personal use. Commercial use requires permission.
💬 Support
For issues, feedback, or collaboration, contact:
Telegram: @anujedits76⁠�
