#!/bin/bash

# Loop terus menerus
while true; do
    # Cek koneksi ke Google
    if ping -c 1 google.com &> /dev/null; then
        # Jika online, jalankan script Python di background
        nohup python3 ~/bot_autorun/bot_kirim_gambar_otomatis.py > ~/bot_autorun/bot.log 2>&1 &
        echo "Bot dijalankan!"
        break
    else
        # Jika belum online, tunggu 10 detik
        echo "Menunggu jaringan..."
        sleep 10
    fi
done
