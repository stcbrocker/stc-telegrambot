from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import logging

TOKEN = "7804827343:AAF0_LEnO_DQTvGyevO0idiu-rm3mIpgcfQ"  # token bot kamu

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        print("📌 File ID menu.png:", file_id)
        await update.message.reply_text(f"File ID sudah dicatat ✅\n{file_id}")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, get_file_id))
    print("✅ Bot berjalan... Kirim menu.png ke bot untuk mendapatkan file_id")
    app.run_polling()
