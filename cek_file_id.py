from telethon import TelegramClient, events

# Ganti dengan API dan Token milikmu
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'
bot_token = '8145061682:AAHCuMOoClePeNDHGCM4UKG0M2CwgFjICSw'

client = TelegramClient('session_file_id', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    if event.photo:
        print("📷 Gambar (photo) terdeteksi!")
        print("ID Foto:", event.photo.id)
        print("Access Hash:", event.photo.access_hash)
        print("File Reference:", event.photo.file_reference)
    elif event.document:
        print("📎 Dokumen terdeteksi!")
        try:
            filename = next((attr.file_name for attr in event.document.attributes if hasattr(attr, 'file_name')), 'Tidak diketahui')
            print("Nama File:", filename)
        except:
            pass
        print("ID Dokumen:", event.document.id)
        print("Access Hash:", event.document.access_hash)
        print("File Reference:", event.document.file_reference)

print("🤖 Bot siap menerima gambar... Kirim gambar PNG ke bot (sebagai file atau photo)...")
client.run_until_disconnected()
