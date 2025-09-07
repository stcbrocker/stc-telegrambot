from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Token bot
TOKEN = "8430920732:AAGhJ4FtduLnfQjS6dUVz8LZWP6JzyEYrWc"

# ID grup
CHAT_ID = -1002813694630

# Link APK direct download
APK_LINK = "https://drive.google.com/uc?export=download&id=1X7GRryVIPHIHQY1omiMnZciPYQAWq8Ix"

def main():
    bot = Bot(token=TOKEN)

    # Buat tombol biru download
    keyboard = [[InlineKeyboardButton("📥 Download APK", url=APK_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Kirim pesan dengan tombol
    msg = bot.send_message(
        chat_id=CHAT_ID,
        text="🔥 STC Autotrade APK tersedia!\nKlik tombol di bawah untuk download APK terbaru:",
        reply_markup=reply_markup
    )

    # Pin pesan biar tetap di atas
    bot.pin_chat_message(chat_id=CHAT_ID, message_id=msg.message_id)

    print("✅ Pesan terkirim & berhasil disematkan!")

if __name__ == "__main__":
    main()
