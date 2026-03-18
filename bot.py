import asyncio
import requests
import os
from pyrogram import Client, filters
from config import *
from downloader import download

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text)
async def main(client, message):
    url = message.text.strip()

    msg = await message.reply("🔍 Processing link...")

    res = requests.get(f"http://127.0.0.1:5000/api?url={url}").json()

    if res["status"] != "success":
        return await msg.edit("❌ Invalid link")

    files = res["files"]

    await msg.edit(f"📂 Found {len(files)} files")

    for f in files:
        name = f["name"]
        link = f["link"]

        await msg.edit(f"⬇️ Downloading: {name}")

        path = download(link)

        await msg.edit(f"⬆️ Uploading: {name}")

        sent = await client.send_document(
            message.chat.id,
            document=path,
            caption=f"📄 {name}"
        )

        os.remove(path)

        await asyncio.sleep(2)

    await msg.delete()

app.run()
