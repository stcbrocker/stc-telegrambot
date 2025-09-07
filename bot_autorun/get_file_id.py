from telethon import TelegramClient, events

api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'
bot_token = '8145061682:AAHCuMOoClePeNDHGCM4UKG0M2CwgFjICSw'

client = TelegramClient('session_get_file', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    if event.message.media:
        print("✅ File ID:", event.message.media)
        print("Message:", event.message)
        await client.disconnect()  # stop setelah dapat file_id

print("🤖 Kirim gambar ke bot sekarang...")
client.run_until_disconnected()
