import requests
import hashlib

SERVER_URL = "http://localhost:5000"
FILE_TO_VERIFY = "Sample.AppImage" # Replace with file used for hash generation & monitoring.

# Function to calculate SHA-512 hash
def calculate_sha512(file_path):
    sha512 = hashlib.sha512()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha512.update(chunk)
        return sha512.hexdigest()
    except FileNotFoundError:
        print(f"[✖] Error: {file_path} not found.")
        return None

# Fetch stored hash from server
response = requests.get(f"{SERVER_URL}/get_hash/{FILE_TO_VERIFY}")
if response.status_code == 200:
    stored_hash = response.json().get("hash_value")

    # Calculate local hash
    local_hash = calculate_sha512(FILE_TO_VERIFY)

    if local_hash == stored_hash:
        print(f"[✔] {FILE_TO_VERIFY} integrity verified ✅")
    else:
        print(f"[⚠] ALERT: {FILE_TO_VERIFY} has been modified! ❌")
else:
    print("[✖] Error: Hash not found on server.")

