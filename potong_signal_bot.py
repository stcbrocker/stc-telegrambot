import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.base import BaseScheduler

# Patch timezone supaya pakai pytz
original_init = AsyncIOScheduler.__init__

def patched_init(self, *args, **kwargs):
    if 'timezone' not in kwargs or kwargs['timezone'] is None:
        kwargs['timezone'] = pytz.UTC
    return original_init(self, *args, **kwargs)

AsyncIOScheduler.__init__ = patched_init

# Setelah patch, import yang lain
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import re

TELEGRAM_TOKEN = "8496514952:AAETZIDnYAMp4-TSDM0jvs3rbMGCSxM3q8o"

signal_data = ""

async def save_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global signal_data
    if update.message and update.message.text and len(update.message.text) > 50:
        signal_data = update.message.text
        await update.message.reply_text("✅ Sinyal berhasil disimpan.")

def potong_signal(signal_text: str, start: str, end: str) -> str:
    pattern = re.compile(r"(\d{2}\.\d{2})\s([BS])")
    lines = signal_text.splitlines()
    filtered = []
    started = False

    for line in lines:
        m = pattern.match(line)
        if m:
            time = m.group(1)
            if time == start:
                started = True
            if started:
                filtered.append(line)
            if time == end:
                break
    if not filtered:
        return "❌ Tidak ditemukan sinyal pada rentang waktu tersebut."
    return "\n".join(filtered)

async def potong_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global signal_data
    if not signal_data:
        await update.message.reply_text("⚠️ Belum ada data sinyal yang disimpan. Kirim sinyal dulu di grup.")
        return
    if len(context.args) != 2:
        await update.message.reply_text("Format salah! Gunakan: /potong <jam_mulai> <jam_akhir>\nContoh: /potong 06.00 07.30")
        return
    start_time = context.args[0]
    end_time = context.args[1]
    if not re.match(r"^\d{2}\.\d{2}$", start_time) or not re.match(r"^\d{2}\.\d{2}$", end_time):
        await update.message.reply_text("Format jam harus HH.MM, misal 06.00 atau 15.30")
        return
    result = potong_signal(signal_data, start_time, end_time)
    await update.message.reply_text(f"✂️ Potongan sinyal dari {start_time} sampai {end_time}:\n\n{result}")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), save_signal))
    app.add_handler(CommandHandler("potong", potong_command))
    print("Bot berjalan...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
