from telethon import TelegramClient
import asyncio

# ===== DATA AKUN =====
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'

client = TelegramClient('session_user', api_id, api_hash)

webp_file = '/data/data/com.termux/files/home/storage/downloads/buy.webp'  # path WebP
chat_target = '@SignalAi_autotradeBot'  # chat bot tujuan

async def main():
    await client.start()
    # Kirim file ke bot
    message = await client.send_file(chat_target, webp_file)
    print("✅ File ID WebP:", message.media)

asyncio.run(main())
