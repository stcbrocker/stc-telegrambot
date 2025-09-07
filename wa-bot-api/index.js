const { create, Client } = require('@open-wa/wa-automate');
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
app.use(bodyParser.json());

let client;

// Membuat instance bot WhatsApp
create({
    sessionId: "WA-BOT",
    multiDevice: true, // untuk WhatsApp multi-device
    authTimeout: 60,   // waktu tunggu scan QR dalam detik
    blockCrashLogs: true,
    disableSpins: true,
    headless: true,
    qrTimeout: 0       // QR code tidak kadaluarsa
}).then(c => {
    client = c;
    console.log("Bot WA siap!");
    
    // Event reconnect otomatis jika koneksi terputus
    client.onStateChanged((state) => {
        console.log("Status koneksi:", state);
        if(state === 'CONFLICT' || state === 'UNPAIRED') {
            console.log("Reconnect...");
            client.forceRefocus();
        }
    });
});

// Endpoint API kirim gambar
app.post('/send-image', async (req, res) => {
    try {
        const { number, imagePath, caption } = req.body;
        if (!number || !imagePath) return res.status(400).send("number dan imagePath wajib diisi");

        // Kirim gambar
        await client.sendImage(number + '@c.us', imagePath, caption || '');
        res.send("Gambar berhasil dikirim!");
    } catch (err) {
        console.error(err);
        res.status(500).send("Gagal mengirim gambar");
    }
});

// Jalankan server
app.listen(3000, () => console.log("API WhatsApp berjalan di http://localhost:3000"));
