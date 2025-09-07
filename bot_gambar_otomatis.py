from telethon import TelegramClient, events

# GANTI DENGAN MILIKMU
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'

# GANTI DENGAN ID CHANNELMU, TAMBAH 100
channel_id = -1002511199734

# GANTI DENGAN file_id GAMBAR YANG BENAR
buy_image_id = "AgACAgUAAxkBAAIBFmiO1To5PPgD9ihDSX0pB7B8fY4aAALcxjEbo1F4VNfkXiosgi_NAQADAgADeAADNgQ"
sell_image_id = "AgACAgUAAxkBAAIBGGiO1T9xUGsP4N59A62O2-HTJpIgAALdxjEbo1F4VNqWcLs_1Tt1AQADAgADeAADNgQ"

# Inisialisasi client
client = TelegramClient('bot_gambar_otomatis', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_id))
async def handle_new_message(event):
    print("✅ Mendeteksi ada pesan baru...")
    text = event.raw_text.strip()
    print(f"📥 Isi pesan: {text}")

    if 'ENTRY BUY' in text.upper():
        print("📸 Mengirim gambar BUY...")
        await client.send_file(channel_id, file=buy_image_id, caption="BUY NOW")

    elif 'ENTRY SELL' in text.upper():
        print("📸 Mengirim gambar SELL...")
        await client.send_file(channel_id, file=sell_image_id, caption="SELL NOW")

print("🤖 Bot aktif... Menunggu sinyal dari channel...")
client.start()
client.run_until_disconnected()
