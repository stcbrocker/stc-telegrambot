import subprocess
import time

bots = [
    ["python3", "bot_video.py"],
    ["python3", "bot_tombol_smart.py"],
    ["python3", "bot_kirim_gambar_otomatis.py"]
]

processes = []

def start_bots():
    global processes
    processes = []
    for bot in bots:
        print(f"Menjalankan: {' '.join(bot)}")
        p = subprocess.Popen(bot)
        processes.append(p)

def monitor_bots():
    while True:
        for i, p in enumerate(processes):
            if p.poll() is not None:
                print(f"{bots[i][1]} berhenti, restart...")
                processes[i] = subprocess.Popen(bots[i])
        time.sleep(5)

if __name__ == "__main__":
    start_bots()
    monitor_bots()
