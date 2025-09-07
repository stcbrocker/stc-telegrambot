from telethon.sync import TelegramClient, events
import asyncio

# Konfigurasi bot
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'
bot_token = '8145061682:AAHCuMOoClePeNDHGCM4UKG0M2CwgFjICSw'

# Channel sumber sinyal dan channel tujuan kirim gambar
source_channel = -1002511199734  # Channel SINYAL ANALISIS AI AUTOTRADE
target_channel = -1002511199734  # Sama, bisa diganti jika berbeda

# Inisialisasi client bot
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message = event.message.message.lower()
    
    if 'entry buy' in message:
        await client.send_file(
            target_channel,
            file='buy.png',
            caption='ENTRY BUY'
        )
        print("📤 Gambar BUY terkirim")

    elif 'entry sell' in message:
        await client.send_file(
            target_channel,
            file='sell.png',
            caption='ENTRY SELL'
        )
        print("📤 Gambar SELL terkirim")

print("🤖 Bot gambar aktif... Menunggu sinyal dari channel...")
client.run_until_disconnected()
