from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Token bot
TOKEN = "7459685781:AAGli2g3hUlUfok9Qtzw6Flb8SE_-6Uxo-Q"

# File ID video dari Telegram (lengkap)
VIDEO_FILE_ID = "BAACAgUAAx0CRxEusAABAgJ5aKrcFxYf8uXVIlsikR6P2SksBtUAAkobAAKQMVhVV7RjmN2Jfbw2BA"

# Kata kunci pertanyaan
KEYWORDS = [
    # Setting / pengaturan
    "setting aplikasi", "setting apknya", "setting apk", "setting bot",
    "setting bot nya", "setting stc autotrade", "setting nya gimana",
    "setting nya gimna", "setting nya gmn",
    "cara setting", "cara nyetting", "gimana settingnya", "gimna settingnya",
    "gmna settingnya", "gmn settingnya",
    "gmna cara setting", "gmna cara settingnya", "gimna cara setting", "gimna cara settingnya",
    "cara setting gmna", "cara setting gimna", "setting gimana", "setting gimna",

    # Cara menggunakan / menjalankan
    "jalaninnya gimana", "jalaninnya gimna", "jalaninnya gmn",
    "jalanin aplikasinya", "jalanin apk nya", "jalanin bot nya", "jalanin stc autotrade",
    "gimana cara jalanin", "gimna cara jalanin", "gmna cara jalanin",
    "cara menggunakan", "cara menggunakan nya", "cara menggunakan stc autotrade",
    "caranya gimana", "caranya gimna", "caranya gmn",
    "cara pakai stc autotrade", "cara pake stc autotrade",
    "cara gunain stc autotrade", "cara pakainya", "cara pakenya",
    "gimana cara pakai stc", "gimna cara pake stc", "gmna cara pake stc",
    "gimana cara gunain stc", "gimna cara gunain stc", "gmna cara gunain stc",
    "stc cara pakai", "stc cara gunain", "stc cara pake", "stc cara pake apknya",

    # Pakai apk/apknya
    "cara pakai apk", "cara pakai apknya", "cara pake apk", "cara pake apknya",
    "pake apknya gimana", "pake apknya gimna", "pake apknya gmn",
    "cara pakai aplikasinya", "cara pake aplikasinya", "cara gunain aplikasinya",
    "gimana cara pakai aplikasinya", "gimna cara pake aplikasinya", "gmna cara pake aplikasinya",
    "cara pakai apknya gmna", "cara pakai apknya gimna", "cara pakai apknya gmn",

    # STC / Bot / Gunain / Gunakannya
    "stc nya", "stcnya", "STCnya", "STC Nya", 
    "botnya", "bot nya", "BOTnya", "BOT nya",
    "gunain", "gunakannya", "gunnain", "gunaknaya"
]

# Fungsi balas pesan
async def reply_with_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()  # Membuat semua teks jadi lowercase
    if any(keyword.lower() in user_message for keyword in KEYWORDS):
        await update.message.reply_video(
            VIDEO_FILE_ID,
            caption="📺 Berikut cara menggunakan aplikasi STC AutoTrade 👇"
        )

# Main
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_with_video))

    print("🤖 Bot berjalan... Tunggu pesan masuk di grup/privat.")
    app.run_polling()

# Jalankan script
if __name__ == "__main__":
    main()
