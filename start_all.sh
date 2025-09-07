#!/data/data/com.termux/files/usr/bin/bash

# Mencegah perangkat tidur
termux-wake-lock

# Jalankan bot-video
nohup python3 /data/data/com.termux/files/home/bot_video.py > /data/data/com.termux/files/home/bot_video.log 2>&1 &

# Jalankan bot-tombol-smart
nohup python3 /data/data/com.termux/files/home/bot_tombol_smart.py > /data/data/com.termux/files/home/bot_tombol.log 2>&1 &

# Jalankan bot-kirim-gambar
nohup python3 /data/data/com.termux/files/home/bot_kirim_gambar_otomatis.py > /data/data/com.termux/files/home/bot_gambar.log 2>&1 &
