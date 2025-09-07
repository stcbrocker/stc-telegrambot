import telebot

TOKEN = "7459685781:AAGli2g3hUlUfok9Qtzw6Flb8SE_-6Uxo-Q"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['video'])
def get_file_id(message):
    file_id = message.video.file_id
    print("📎 File ID:", file_id)
    bot.reply_to(message, f"📎 File ID: `{file_id}`", parse_mode="Markdown")

print("📥 Menunggu video...")
bot.infinity_polling()
