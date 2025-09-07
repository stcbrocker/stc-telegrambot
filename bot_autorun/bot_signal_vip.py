from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel, InputPhoto

# ===== DATA BOT & CHANNEL =====
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'
channel_id = -2511199734  # Channel sinyal

bot_token = '8145061682:AAHCuMOoClePeNDHGCM4UKG0M2CwgFjICSw'

# ===== FILE ID BUY/SELL (InputPhoto) =====
buy_photo = InputPhoto(
    id=6145715588165650680,
    access_hash=6814544577679427979,
    file_reference=b'\x01\x00\x00\x00\x12h\xa8\x87\x17\xe5\xb6\x0b]r\xee7\xdc\xfa\x9c\xa3\xa1[#8V'
)

sell_photo = InputPhoto(
    id=6145715588165650681,  # Ganti dengan hasil get_file_id untuk sell.png
    access_hash=6814544577679427980,  # Ganti sesuai output
    file_reference=b'\x01\x00\x00\x00\x12h\xa8\x87\x17\xe5\xb6\x0b]r\xee7\xdc\xfa\x9c\xa3\xa1[#8W'
)

# ===== INISIALISASI BOT =====
client = TelegramClient('session_signal_vip', api_id, api_hash).start(bot_token=bot_token)

# ===== MONITOR CHANNEL =====
@client.on(events.NewMessage(chats=PeerChannel(channel_id)))
async def handle_signal(event):
    message = event.message.message.lower()

    if 'buy' in message:
        await client.send_file(channel_id, buy_photo, caption="ENTRY BUY")
        print("📤 Gambar BUY terkirim")

    elif 'sell' in message:
        await client.send_file(channel_id, sell_photo, caption="ENTRY SELL")
        print("📤 Gambar SELL terkirim")

# ===== JALANKAN BOT =====
print("🤖 Bot gambar aktif... Menunggu sinyal dari channel...")
client.run_until_disconnected()
