import telebot

TOKEN = '7459685781:AAGli2g3hUlUfok9Qtzw6Flb8SE_-6Uxo-Q'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    file_id = message.photo[-1].file_id
    print("📎 File ID:", file_id)
    bot.send_message(message.chat.id, f"📎 File ID: `{file_id}`", parse_mode="Markdown")

print("📥 Menunggu gambar...")
bot.infinity_polling()
