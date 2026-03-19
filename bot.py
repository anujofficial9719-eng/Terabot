import asyncio
import requests
import os
import json
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from downloader import download

MAX_SIZE = 2 * 1024 * 1024 * 1024  # 2GB limit
PREMIUM_FILE = "premium_users.json"

# Load premium users
if os.path.exists(PREMIUM_FILE):
    with open(PREMIUM_FILE, "r") as f:
        premium_users = {int(k): datetime.fromisoformat(v) for k, v in json.load(f).items()}
else:
    premium_users = {}

def save_premium():
    with open(PREMIUM_FILE, "w") as f:
        json.dump({k: v.isoformat() for k, v in premium_users.items()}, f)

# =========================
# Pyrogram Client
# =========================
app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# =========================
# Start & Plans
# =========================
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Welcome! Send me your TeraBox or Terashare link and I will download it for you!")

@app.on_message(filters.command("plans"))
async def plans_category(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔹 Regular Plan", callback_data="plan_regular")],
        [InlineKeyboardButton("⚡ Creator Plan", callback_data="plan_creator")],
        [InlineKeyboardButton("📜 Regular Plan Details", callback_data="plan_details")],
        [InlineKeyboardButton("📜 Creator Plan Details", callback_data="creator_details")]
    ])
    await message.reply("🗂️ Select a Plan Category for Terabox:", reply_markup=keyboard)

# =========================
# Callback Query (Plans)
# =========================
@app.on_callback_query()
async def plan_callback(client, callback_query):
    data = callback_query.data
    await callback_query.answer()  # stop loading

# =========================
# Main Download Handler
# =========================
@app.on_message(filters.text)
async def main_handler(client, message):
    url = message.text.strip()
    msg = await message.reply("🔍 Processing link...")

    # Terashare detection
    if "terasharelink.com" in url:
        try:
            path = download(url)
            if not path or not os.path.exists(path):
                return await msg.edit("❌ Terashare download failed")
            if os.path.getsize(path) > MAX_SIZE:
                os.remove(path)
                return await msg.edit("⚠️ File too large (2GB+)")
            await client.send_document(message.chat.id, document=path, caption=f"📄 {os.path.basename(path)}")
            os.remove(path)
            return await msg.edit("✅ Terashare file uploaded successfully!")
        except Exception as e:
            return await msg.edit(f"❌ Terashare download error: {e}")

    # TeraBox / API link
    try:
        res = requests.get(f"http://127.0.0.1:5000/api?url={url}", timeout=30).json()
    except:
        return await msg.edit("❌ API Error / Server Down")

    if res.get("status") != "success":
        return await msg.edit("❌ Invalid or unsupported link")

    files = res.get("files", [])
    if not files:
        return await msg.edit("❌ No files found")

    await msg.edit(f"📂 Found {len(files)} file(s)")

    for i, f in enumerate(files, start=1):
        name = f.get("name")
        link = f.get("link")
        try:
            await msg.edit(f"⬇️ [{i}/{len(files)}] Downloading:\n{name}")
            path = download(link)
            if not path or not os.path.exists(path):
                await message.reply(f"❌ Download failed: {name}")
                continue
            if os.path.getsize(path) > MAX_SIZE:
                await message.reply(f"⚠️ File too large (2GB+): {name}")
                os.remove(path)
                continue
            await msg.edit(f"⬆️ [{i}/{len(files)}] Uploading:\n{name}")
            await client.send_document(message.chat.id, document=path, caption=f"📄 {name}")
            os.remove(path)
        except Exception as e:
            await message.reply(f"❌ Failed: {name}")
        await asyncio.sleep(1)

    await msg.edit("✅ All files uploaded successfully!")
    await asyncio.sleep(3)
    await msg.delete()

# =========================
# Admin Commands
# =========================
@app.on_message(filters.command("add_premium") & filters.user(lambda u: u.username in ADMINS))
async def add_premium(client, message):
    try:
        args = message.text.split()
        if len(args) != 3:
            return await message.reply("Usage: /add_premium <user_id> <days>")
        user_id = int(args[1])
        days = int(args[2])
        expiry = datetime.now() + timedelta(days=days)
        premium_users[user_id] = expiry
        save_premium()
        await message.reply(f"✅ Premium access granted to `{user_id}` until {expiry.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

@app.on_message(filters.command("remove_premium") & filters.user(lambda u: u.username in ADMINS))
async def remove_premium(client, message):
    try:
        args = message.text.split()
        if len(args) != 2:
            return await message.reply("Usage: /remove_premium <user_id>")
        user_id = int(args[1])
        if user_id in premium_users:
            del premium_users[user_id]
            save_premium()
            await message.reply(f"✅ Premium access removed for `{user_id}`")
        else:
            await message.reply(f"❌ User `{user_id}` does not have premium access")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

@app.on_message(filters.command("premium_users") & filters.user(lambda u: u.username in ADMINS))
async def list_premium_users(client, message):
    if not premium_users:
        return await message.reply("❌ No premium users found")
    msg = "📜 **Premium Users:**\n"
    for uid, expiry in premium_users.items():
        msg += f"- `{uid}` expires on {expiry.strftime('%Y-%m-%d %H:%M:%S')}\n"
    await message.reply(msg)

# =========================
# Run Bot
# =========================
app.run()
