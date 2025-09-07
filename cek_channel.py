from telethon.sync import TelegramClient

api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'

client = TelegramClient('cek_channel', api_id, api_hash)

with client:
    for dialog in client.iter_dialogs():
        print(f"{dialog.name} : {dialog.id}")
