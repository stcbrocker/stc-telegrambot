#!/data/data/com.termux/files/usr/bin/bash
# Tunggu 30 detik biar internet stabil setelah restart
sleep 30
cd ~

# Hentikan proses lama kalau ada (biar tidak dobel)
pkill -f bot_video.py
pkill -f bot_tombol_smart.py
pkill -f bot_kirim_gambar_otomatis.py

# Jalankan ulang bot
nohup python3 bot_video.py > bot_video.log 2>&1 &
nohup python3 bot_tombol_smart.py > bot_tombol.log 2>&1 &
nohup python3 bot_kirim_gambar_otomatis.py > bot_gambar.log 2>&1 &
