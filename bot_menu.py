from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7804827343:AAF0_LEnO_DQTvGyevO0idiu-rm3mIpgcfQ"
GROUP_ID = -1001192308400  # ID grup kamu

async def menu_handler(update: Update, context: CallbackContext):
    if update.effective_chat.id != GROUP_ID:
        return  # Bukan grup target

    keyboard = [
        [InlineKeyboardButton("🌐 Kunjungi STC Broker", url="https://stcbroker.id")],
        [InlineKeyboardButton("📌 Panduan Trading", url="https://stcbroker.id/panduan")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Selamat datang! Pilih menu di bawah ini:",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
