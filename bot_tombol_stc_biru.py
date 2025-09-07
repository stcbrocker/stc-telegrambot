from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, ChatMemberUpdated
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "8023924208:AAFDg90VOw3EfwsBcVjsySrnESEGjjQ09QY"
GROUP_ID = -1002635007930
HUBUNGI_ADMIN = "BANGREI"

# Fungsi sapaan anggota baru + tombol semat
async def welcome_member(update: ChatMemberUpdated, context: ContextTypes.DEFAULT_TYPE):
    new_member = update.new_chat_member.user
    bot = context.bot
    
    # Tombol inline
    keyboard = [
        [InlineKeyboardButton("Daftar Akun", url="https://stcbroker.id")],
        [InlineKeyboardButton("Hubungi Admin", url=f"https://t.me/{HUBUNGI_ADMIN}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Kirim pesan sapaan + tombol
    sent_msg = await bot.send_message(
        chat_id=GROUP_ID,
        text=f"🌹 Selamat datang, {new_member.mention_html()}! Silakan pilih tombol di bawah:",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
    
    # Sematkan pesan sapaan
    await bot.pin_chat_message(GROUP_ID, sent_msg.message_id, disable_notification=True)

# Build aplikasi
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(welcome_member, ChatMemberHandler.CHAT_MEMBER))

print("🔔 Bot siap menyapa anggota baru dengan tombol semat...")
app.run_polling()
