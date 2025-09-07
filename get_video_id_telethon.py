from telethon import TelegramClient, events

# Data dari my.telegram.org
api_id = 29831238
api_hash = "11211a9254f6d1a13f178047bc6ea29a"

# Nama session file (biar beda dengan bot lama)
client = TelegramClient("video_session_stc", api_id, api_hash)

GROUP_ID = -1192308400  # ID Group kamu

@client.on(events.NewMessage(chats=GROUP_ID))
async def handler(event):
    if event.video:
        file_id = event.video.id
        access_hash = event.video.access_hash
        print(f"🎥 Video File ID: {file_id}")
        print(f"🔑 Access Hash: {access_hash}")

        await event.reply(
            f"📎 Video File ID:\n`{file_id}`\n\n🔑 Access Hash:\n`{access_hash}`",
            parse_mode="markdown"
        )

print("📥 Menunggu video di grup STCautotrade...")
client.start()
client.run_until_disconnected()
