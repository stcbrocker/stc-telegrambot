# File: welcome_bot.py
# Bot ini otomatis mengirim tombol Menu ke anggota baru di grup

from telebot import TeleBot, types

# ======= CONFIG =======
TOKEN = "7804827343:AAF0_LEnO_DQTvGyevO0idiu-rm3mIpgcfQ"  # Token @Ai_stockityBOT
GROUP_ID = -1192308400                                    # ID grup RUANG DISKUSI
MENU_URL = "https://stcbroker.id"                         # URL tombol Menu
# ======================

bot = TeleBot(TOKEN)

# Event anggota baru join
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    if message.chat.id == GROUP_ID:
        # Membuat tombol Menu
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Menu", url=MENU_URL))

        # Kirim pesan ke setiap anggota baru
        for member in message.new_chat_members:
            bot.send_message(
                message.chat.id,
                f"Selamat datang, {member.first_name}! Klik tombol di bawah untuk Menu:",
                reply_markup=markup
            )
            print(f"[INFO] Mengirim tombol Menu ke: {member.first_name}")

# Jalankan bot
print("[INFO] Bot @Ai_stockityBOT berjalan...")
bot.polling(none_stop=True)
