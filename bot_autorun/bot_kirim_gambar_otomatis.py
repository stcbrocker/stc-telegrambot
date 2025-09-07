from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
from telebot import TeleBot

# ===== DATA BOT & CHANNEL =====
api_id = 29831238
api_hash = '11211a9254f6d1a13f178047bc6ea29a'
channel_id = -2511199734  # ID channel sinyal

bot_token = '7459685781:AAGli2g3hUlUfok9Qtzw6Flb8SE_-6Uxo-Q'
buy_image_id = 'AgACAgUAAxkBAAIBFmiO1To5PPgD9ihDSX0pB7B8fY4aAALcxjEbo1F4VNfkXiosgi_NAQADAgADeAADNgQ'
sell_image_id = 'AgACAgUAAxkBAAIBGGiO1T9xUGsP4N59A62O2-HTJpIgAALdxjEbo1F4VNqWcLs_1Tt1AQADAgADeAADNgQ'

# ===== INISIALISASI BOT =====
client = TelegramClient('session_bot', api_id, api_hash)
bot = TeleBot(bot_token)

# ===== MONITOR CHANNEL =====
@client.on(events.NewMessage(chats=PeerChannel(channel_id)))
async def handle_signal(event):
    message = event.message.message.lower()

    if 'entry buy' in message:
        print("📥 Detected: ENTRY BUY")
        bot.send_photo(chat_id=channel_id, photo=buy_image_id)

    elif 'entry sell' in message:
        print("📥 Detected: ENTRY SELL")
        bot.send_photo(chat_id=channel_id, photo=sell_image_id)

# ===== JALANKAN BOT =====
print("🤖 Bot gambar aktif... Menunggu sinyal dari channel...")
client.start(bot_token=bot_token)
client.run_until_disconnected()
