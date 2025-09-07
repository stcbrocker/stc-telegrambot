from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path chromium-driver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-data-dir=./profile')  # simpan session WA

driver = webdriver.Chrome(options=options)

# Buka WA Web
driver.get("https://web.whatsapp.com")

print("⚠️ Silahkan scan QR di WA Web. Tunggu hingga login selesai...")

# Tunggu login manual
time.sleep(30)  # bisa ditambah jika perlu
