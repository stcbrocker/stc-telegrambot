from telegram import Bot

TOKEN = "8430920732:AAGhJ4FtduLnfQjS6dUVz8LZWP6JzyEYrWc"
bot = Bot(token=TOKEN)

updates = bot.get_updates()
for update in updates:
    print(update.message.chat.id, update.message.chat.title)
