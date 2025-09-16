import speedtest
import time
import pandas as pd
import os
from datetime import datetime
import threading
import sys
import msvcrt  # Windows-only

# ========================
# CONFIGURATION (EDIT HERE)
# ========================
MEASUREMENT_INTERVAL = 10  # seconds between measurements
OUTPUT_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")  # folder for Excel files
# ========================

# --- Global variables ---
measurements = []  # list of tuples: (time_s, download_mbps, upload_mbps, ping_ms)
start_time = time.time()
running = True


# --- Continuous measurement function ---
def measure_speed(interval=MEASUREMENT_INTERVAL):
    global measurements, running
    s = speedtest.Speedtest()
    s.get_servers()
    best_server = s.get_best_server()
    print(f"Using server: {best_server['host']} ({best_server['sponsor']}, {best_server['country']})")

    while running:
        try:
            download_speed = s.download() / 1e6  # Mbps
            upload_speed = s.upload() / 1e6  # Mbps
            ping_ms = s.results.ping  # ms
            elapsed = time.time() - start_time
            measurements.append((
                round(elapsed, 1),
                round(download_speed, 2),
                round(upload_speed, 2),
                round(ping_ms, 1)
            ))
            print(f"t={round(elapsed, 1)}s | Download: {round(download_speed, 2)} Mbps | "
                  f"Upload: {round(upload_speed, 2)} Mbps | Ping: {round(ping_ms, 1)} ms")
        except Exception as e:
            print("Speedtest failed:", e)
        time.sleep(interval)


# --- Save measurements to Excel ---
def save_excel():
    if not measurements:
        print("No measurements yet. Nothing to save.")
        return
    df = pd.DataFrame(measurements, columns=["Time (s)", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])
    filename = f"internet_speed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    df.to_excel(filepath, index=False)
    print(f"Measurements saved to {filepath}")


# --- Keyboard input function using msvcrt ---
def wait_for_input():
    global running
    print("\nPress Enter to save Excel file. Press 's' to stop and quit.\n")
    while running:
        if msvcrt.kbhit():
            key = msvcrt.getwch()  # get a keypress
            if key == '\r':  # Enter
                save_excel()
            elif key.lower() == 's':
                running = False
                break
        time.sleep(0.1)  # small sleep to reduce CPU usage


# --- Start measurement thread ---
measurement_thread = threading.Thread(target=measure_speed, args=(MEASUREMENT_INTERVAL,), daemon=True)
measurement_thread.start()

# --- Main thread waits for keyboard input ---
wait_for_input()

# --- Save Excel before exiting ---
save_excel()
print("Exiting program.")
sys.exit()
