# 🚀 Terabox Downloader Bot (Advanced)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Library-Pyrogram-yellow?style=for-the-badge&logo=telegram">
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

<p align="center">
<b>A fully automated Telegram bot to download Terabox files/folders, manage plans, and handle premium users with admin control.</b>
</p>

<p align="center">
  <a href="https://t.me/anujedits76">
    <img src="https://img.shields.io/badge/Owner-Anuj%20Kumar-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://github.com/anujofficial9719-eng/Terabot">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github">
  </a>
</p>

---

## 🔗 Quick Links

<p align="center">
  <a href="#-features"><img src="https://img.shields.io/badge/Features-View-blue?style=for-the-badge"></a>
  <a href="#-deployment"><img src="https://img.shields.io/badge/Deployment-Setup-green?style=for-the-badge"></a>
  <a href="#-commands"><img src="https://img.shields.io/badge/Commands-List-orange?style=for-the-badge"></a>
  <a href="#-support"><img src="https://img.shields.io/badge/Support-Telegram-blue?style=for-the-badge&logo=telegram"></a>
</p>

---

# 🗂 Features

### 📦 Core

- 🔐 Auto login & cookie management (TeraBox email/password)  
- ⚡ Fast downloads using `aria2`  
- 📂 Folder & multiple file support  
- ⏱ No waiting queue, unlimited downloads  
- 🌐 Bulk link processing  
- 📤 Auto upload to Telegram  
- 💾 Temporary storage in `/downloads`  
- 🧹 Automatic cleanup after upload  
- ⚠️ Max file size: 2GB (configurable)  

### 🎟 Plans System

- **Regular Plans:** Bronze → Ultimate  
- **Creator Plans:** Bronze → Ultimate  
- Extra Creator features: `/settings`, custom dump channel, auto-forward downloads  

### 👑 Admin Features

- `/add_premium <user_id> <days>` — Grant premium to users  
- `/remove_premium <user_id>` — Remove premium access  
- `/premium_users` — List active premium users  
- Restricted to admin: `@anujedits76` (changeable in `config.py`)  

### 💡 Other Features

- Inline buttons for plan categories & details  
- JSON-based persistent premium storage (`premium_users.json`)  
- Multiple admins supported by updating `ADMINS` list  

---

# 🛠 Deployment

## ✅ Prerequisites

- Python 3.11+  
- Telegram API ID & API HASH  
- Bot token from BotFather  
- TeraBox account credentials  

---

## ⚙️ Environment Variables

| Variable       | Description                            |
| ---------------| -------------------------------------- |
| `API_ID`       | Telegram API ID                        |
| `API_HASH`     | Telegram API Hash                      |
| `BOT_TOKEN`    | Bot token from BotFather               |
| `TB_EMAIL`     | TeraBox login email                     |
| `TB_PASSWORD`  | TeraBox password                        |
| `DOWNLOAD_DIR` | Folder to store temporary downloads     |

---

## 💻 Local Setup

```bash
git clone https://github.com/anujofficial9719-eng/Terabot.git
cd Terabot
pip install -r requirements.txt
python bot.py

🐳 Docker
Bash
docker build -t terabox-bot .
docker run -d --env-file .env terabox-bot
📝 Commands
👤 User Commands
Command
Description
/start
Start the bot
/help
Help message
/plans
View plan categories & features
<TeraBox link>
Send any file/folder link to download
👑 Admin Commands
Command
Description
/add_premium <id> <days>
Grant premium to a user
/remove_premium <id>
Remove premium from a user
/premium_users
List all active premium users
📁 Folder Structure
Plain text
terabot/
│
├── bot.py           # Main Telegram bot
├── downloader.py    # Aria2 download logic
├── config.py        # Config & credentials
├── premium_users.json # Persistent premium storage
├── requirements.txt # Python dependencies
├── downloads/       # Temporary file storage
└── README.md        # Documentation

📞 Support
Telegram: https//t.me/Anujedits76
GitHub: https://github.com/anujofficial9719-eng
