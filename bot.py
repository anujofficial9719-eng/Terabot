import os
import time
import asyncio
import requests
from pyrogram import Client, filters
from config import *

from downloader import download_file

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def bar(p):
    return "█"*int(p/5) + "░"*(20-int(p/5))

@app.on_message(filters.text)
async def main(client, message):
    url = message.text.strip()

    msg = await message.reply("🔍 Analyzing link...")

    try:
        res = requests.get(API_URL + url).json()
    except:
        return await msg.edit("❌ API error")

    if res["status"] != "success":
        return await msg.edit("❌ Invalid link")

    name = res["filename"]
    size = res["size"]
    dlink = res["download"]

    await msg.edit(f"📂 Processing file...\n{name}")

    start = time.time()
    path = download_file(dlink)

    await msg.edit("⬆️ Uploading...")

    sent = await client.send_document(
        message.chat.id,
        document=path,
        caption=f"""🎬 {name}

📦 Size: {size}
⚡ Done in {int(time.time()-start)} sec

⚠️ Auto delete in 1 hour"""
    )

    os.remove(path)
    await msg.delete()

    await asyncio.sleep(3600)
    await sent.delete()

app.run()
