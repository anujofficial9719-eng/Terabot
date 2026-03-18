import asyncio
import requests
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from downloader import download

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

MAX_SIZE = 2 * 1024 * 1024 * 1024  # 2GB limit

# =========================
# 🗂 Plans Menu
# =========================
@app.on_message(filters.command("plans"))
async def plans(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔹 Regular Plan", callback_data="plan_regular")],
            [InlineKeyboardButton("⚡ Creator Plan", callback_data="plan_creator")]
        ]
    )
    await message.reply(
        "🗂️ Select a Plan Category for Terabox:\n\n"
        "🚀 ALL PLANS INCLUDE:\n"
        "• Multiple Links Downloading\n"
        "• Bulk Link Processing (Fast Speed)\n"
        "• Folder Link Support\n"
        "• No Waiting Queue\n"
        "• Unlimited Downloads\n"
        "• 15+ Download Bots\n"
        "• No Speed Limits\n"
        "• No File Size Restrictions\n"
        "• All Features Unlocked\n\n"
        "🌟 Creator Plan has extra professional features!",
        reply_markup=keyboard
    )

@app.on_callback_query()
async def plan_callback(client, callback_query):
    data = callback_query.data
    if data == "plan_regular":
        await callback_query.message.edit_text(
            "🔹 You selected **Regular Plan**\n\n"
            "Enjoy all standard Terabox downloader features!"
        )
    elif data == "plan_creator":
        await callback_query.message.edit_text(
            "⚡ You selected **Creator Plan**\n\n"
            "🌟 EXCLUSIVE CREATOR FEATURES:\n"
            "• Access to /settings Command\n"
            "• Set Custom Dump Channel\n"
            "• Auto-Forward Downloads to your Channel\n\n"
            "All Regular Plan features included!"
        )

# =========================
# 📂 Main Download Handler
# =========================
@app.on_message(filters.text)
async def main(client, message):
    url = message.text.strip()

    msg = await message.reply("🔍 Processing link...")

    try:
        res = requests.get(
            f"http://127.0.0.1:5000/api?url={url}",
            timeout=30
        ).json()
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

            await client.send_document(
                message.chat.id,
                document=path,
                caption=f"📄 {name}"
            )

            os.remove(path)

        except Exception as e:
            await message.reply(f"❌ Failed: {name}")

        await asyncio.sleep(1)

    await msg.edit("✅ All files uploaded successfully!")
    await asyncio.sleep(3)
    await msg.delete()

# =========================
# 🚀 Run Bot
# =========================
app.run()
