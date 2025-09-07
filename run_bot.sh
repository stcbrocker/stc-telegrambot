#!/data/data/com.termux/files/usr/bin/bash
# Script untuk menjalankan bot dan auto-restart jika mati

while true
do
    python3 bot_tombol_smart.py
    echo "⚠️ Bot mati atau jaringan putus, restart dalam 5 detik..."
    sleep 5
done
