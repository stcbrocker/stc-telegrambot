import os
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel

# ===== DATA BOT & CHANNEL =====
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'
channel_id = -2511199734  # ID channel sinyal
bot_token = '8145061682:AAHCuMOoClePeNDHGCM4UKG0M2CwgFjICSw'

# ===== PATH FILE WEBP =====
buy_file = os.path.expanduser('~/storage/downloads/buy.webp')
sell_file = os.path.expanduser('~/storage/downloads/sell.webp')

# ===== INISIALISASI BOT =====
client = TelegramClient('session_bot', api_id, api_hash).start(bot_token=bot_token)

# ===== MONITOR CHANNEL =====
@client.on(events.NewMessage(chats=PeerChannel(channel_id)))
async def handle_signal(event):
    message = event.message.message.lower()
    
    if 'buy' in message:
        print("📥 Detected: BUY")
        await client.send_file(channel_id, file=buy_file)
    elif 'sell' in message:
        print("📥 Detected: SELL")
        await client.send_file(channel_id, file=sell_file)

print("🤖 Bot WebP aktif... Menunggu sinyal dari channel...")
client.run_until_disconnected()
