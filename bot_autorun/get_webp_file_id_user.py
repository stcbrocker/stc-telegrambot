import asyncio
from telethon import TelegramClient

# ===== DATA AKUN USER =====
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'

# Path file WebP
buy_webp = '/data/data/com.termux/files/home/storage/downloads/buy.webp'
sell_webp = '/data/data/com.termux/files/home/storage/downloads/sell.webp'

# Target kirim sementara: Saved Messages user
chat_target = 'me'

# Inisialisasi client user
client = TelegramClient('session_user', api_id, api_hash)

async def main():
    await client.start()
    
    # Kirim file buy.webp ke Saved Messages
    buy_msg = await client.send_file(chat_target, buy_webp)
    print("✅ File ID BUY WebP:", buy_msg.media)
    
    # Kirim file sell.webp ke Saved Messages
    sell_msg = await client.send_file(chat_target, sell_webp)
    print("✅ File ID SELL WebP:", sell_msg.media)

    await client.disconnect()

# Jalankan
asyncio.run(main())
