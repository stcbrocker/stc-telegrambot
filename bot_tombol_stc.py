import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import TelegramError, RetryAfter

TOKEN = "8023924208:AAFDg90VOw3EfwsBcVjsySrnESEGjjQ09QY"
GROUP_ID = -1002635007930
HUBUNGI_ADMIN = "BANGREI"

bot = Bot(token=TOKEN)

async def main():
    keyboard = [
        [InlineKeyboardButton("Daftar Akun", url="https://stcbroker.id")],
        [InlineKeyboardButton("Hubungi Admin", url=f"https://t.me/{HUBUNGI_ADMIN}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    for attempt in range(3):  # coba 3x jika timeout
        try:
            sent_message = await bot.send_message(
                chat_id=GROUP_ID,
                text="👋 Halo! Pilih salah satu tombol berikut untuk memulai:",
                reply_markup=reply_markup
            )
            await bot.pin_chat_message(
                chat_id=GROUP_ID,
                message_id=sent_message.message_id,
                disable_notification=True
            )
            print("✅ Pesan terkirim dan disematkan!")
            break
        except RetryAfter as e:
            print(f"⏳ Telegram meminta retry setelah {e.retry_after} detik, menunggu...")
            await asyncio.sleep(e.retry_after)
        except TelegramError as e:
            print("❌ Terjadi kesalahan:", e)
            await asyncio.sleep(5)

asyncio.run(main())
