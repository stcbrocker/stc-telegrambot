from telethon.sync import TelegramClient

api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'

with TelegramClient('user_session', api_id, api_hash) as client:
    print("✅ Session berhasil dibuat.")
