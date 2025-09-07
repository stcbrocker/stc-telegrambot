from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import logging

# ====== DATA BOT ======
TOKEN = "7804827343:AAF0_LEnO_DQTvGyevO0idiu-rm3mIpgcfQ"
LINK_VIP = "https://t.me/+czCo8Z66tLpmYThl"
GROUP_ID = -1001192308400  # ID grup target

# Logging untuk debug
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def kirim_tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Pastikan hanya merespons di grup target
    if update.effective_chat.id != GROUP_ID:
        return

    chat_id = update.effective_chat.id

    keyboard = [
        [InlineKeyboardButton("🔵 LIHAT SIGNAL VIP", url=LINK_VIP)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Kirim tombol
    msg = await context.bot.send_message(
        chat_id=chat_id,
        text="Klik tombol biru di bawah untuk melihat signal lengkap 📈",
        reply_markup=reply_markup
    )

    # Sematkan pesan
    await context.bot.pin_chat_message(chat_id=chat_id, message_id=msg.message_id)

    await update.message.reply_text("✅ Tombol sudah dikirim & disematkan ke grup.")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Tangkap hanya pesan yang mengandung kata 'sinyal' (case-insensitive)
    app.add_handler(
        MessageHandler(filters.TEXT & filters.Regex(r'(?i)\bsinyal\b'), kirim_tombol)
    )

    print("🤖 Bot aktif... Tunggu kata 'sinyal' di grup.")
    app.run_polling()
