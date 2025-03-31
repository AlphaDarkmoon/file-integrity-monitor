import requests
import hashlib
import time

SERVER_URL = "http://localhost:5000"
FILE_TO_MONITOR = "Sample.AppImage" # Replace with file used for hash generation & monitoring.

def calculate_sha512(file_path):
    sha512 = hashlib.sha512()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha512.update(chunk)
        return sha512.hexdigest()
    except FileNotFoundError:
        return None

def fetch_stored_hash(filename):
    response = requests.get(f"{SERVER_URL}/get_hash/{filename}")
    if response.status_code == 200:
        return response.json().get("hash_value")
    else:
        return None

def monitor_integrity():
    print("[🔍] Monitoring:", FILE_TO_MONITOR)
    while True:
        local_hash = calculate_sha512(FILE_TO_MONITOR)
        stored_hash = fetch_stored_hash(FILE_TO_MONITOR)
        if not local_hash or not stored_hash or local_hash != stored_hash:
            print(f"[⚠] ALERT: {FILE_TO_MONITOR} has been modified! ❌")
            break
        print(f"[✔] {FILE_TO_MONITOR} is safe ✅")
        time.sleep(30)

monitor_integrity()

