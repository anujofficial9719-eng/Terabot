import asyncio
import requests
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from downloader import download

# =========================
# 🚀 Pyrogram Bot Initialization
# =========================
app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
MAX_SIZE = 2 * 1024 * 1024 * 1024  # 2GB limit

# =========================
# 🗂 Plans Menu (Category)
# =========================
@app.on_message(filters.command("plans"))
async def plans_category(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔹 Regular Plan", callback_data="plan_regular")],
            [InlineKeyboardButton("⚡ Creator Plan", callback_data="plan_creator")],
            [InlineKeyboardButton("📜 Regular Plan Details", callback_data="plan_details")],
            [InlineKeyboardButton("📜 Creator Plan Details", callback_data="creator_details")]
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

# =========================
# 🎟 Plan Details & Callback
# =========================
@app.on_callback_query()
async def plan_callback(client, callback_query):
    data = callback_query.data

    # ===== Category Plans =====
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

    # ===== Detailed Regular Plans =====
    elif data == "plan_details":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🎟️ Bronze — 12 Days ₹19", callback_data="plan_bronze")],
                [InlineKeyboardButton("🥈 Silver — 30 Days ₹39", callback_data="plan_silver")],
                [InlineKeyboardButton("🥇 Silver Plus — 45 Days ₹59", callback_data="plan_silverplus")],
                [InlineKeyboardButton("🏅 Gold — 60 Days ₹79", callback_data="plan_gold")],
                [InlineKeyboardButton("👑 Platinum — 90 Days ₹99", callback_data="plan_platinum")],
                [InlineKeyboardButton("💎 Diamond — 150 Days ₹149", callback_data="plan_diamond")],
                [InlineKeyboardButton("🚀 Ultimate — 200 Days ₹199", callback_data="plan_ultimate")]
            ]
        )
        await callback_query.message.edit_text(
            "📜 **Available Plans for Terabox — Regular**\n\n"
            "Choose your preferred plan below to see details:",
            reply_markup=keyboard
        )

    # ===== Detailed Creator Plans =====
    elif data == "creator_details":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🎟️ Bronze — 12 Days ₹39", callback_data="creator_bronze")],
                [InlineKeyboardButton("🥈 Silver — 30 Days ₹89", callback_data="creator_silver")],
                [InlineKeyboardButton("🥇 Silver Plus — 45 Days ₹129", callback_data="creator_silverplus")],
                [InlineKeyboardButton("🏅 Gold — 60 Days ₹169", callback_data="creator_gold")],
                [InlineKeyboardButton("👑 Platinum — 90 Days ₹249", callback_data="creator_platinum")],
                [InlineKeyboardButton("💎 Diamond — 150 Days ₹399", callback_data="creator_diamond")],
                [InlineKeyboardButton("🚀 Ultimate — 200 Days ₹499", callback_data="creator_ultimate")]
            ]
        )
        await callback_query.message.edit_text(
            "📜 **Available Plans for Terabox — Creator**\n\n"
            "Choose your preferred plan below to see details:",
            reply_markup=keyboard
        )
    else:
        # Individual plan details
        plan_details = {
            "plan_bronze": "🎟️ **Bronze — 12 Days**\n💰 ₹19 (₹1.58/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "plan_silver": "🥈 **Silver — 30 Days**\n💰 ₹39 (₹1.30/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "plan_silverplus": "🥇 **Silver Plus — 45 Days**\n💰 ₹59 (₹1.31/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "plan_gold": "🏅 **Gold — 60 Days**\n💰 ₹79 (₹1.32/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "plan_platinum": "👑 **Platinum — 90 Days**\n💰 ₹99 (₹1.10/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "plan_diamond": "💎 **Diamond — 150 Days**\n💰 ₹149 (₹0.99/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "plan_ultimate": "🚀 **Ultimate — 200 Days**\n💰 ₹199 (₹0.995/day)\n✅ Multiple Links Downloading\n✅ Bulk Link Processing\n✅ Folder Link Support\n✅ No Waiting Queue\n✅ Unlimited Downloads\n✅ All Features Unlocked",
            "creator_bronze": "🎟️ **Creator Bronze — 12 Days**\n💰 ₹39 (₹3.25/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included",
            "creator_silver": "🥈 **Creator Silver — 30 Days**\n💰 ₹89 (₹2.96/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included",
            "creator_silverplus": "🥇 **Creator Silver Plus — 45 Days**\n💰 ₹129 (₹2.86/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included",
            "creator_gold": "🏅 **Creator Gold — 60 Days**\n💰 ₹169 (₹2.81/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included",
            "creator_platinum": "👑 **Creator Platinum — 90 Days**\n💰 ₹249 (₹2.76/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included",
            "creator_diamond": "💎 **Creator Diamond — 150 Days**\n💰 ₹399 (₹2.66/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included",
            "creator_ultimate": "🚀 **Creator Ultimate — 200 Days**\n💰 ₹499 (₹2.49/day)\n✅ Access /settings & Custom Channel\n✅ Auto-Forward to Channel\n✅ All Regular Features Included"
        }
        if data in plan_details:
            await callback_query.message.edit_text(plan_details[data], disable_web_page_preview=True)

# =========================
# 📂 Main Download Handler
# =========================
@app.on_message(filters.text)
async def main_handler(client, message):
    url = message.text.strip()
    msg = await message.reply("🔍 Processing link...")

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
# 🚀 Run Bot
# =========================
app.run()
