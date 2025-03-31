import hashlib
import requests

SERVER_URL = "http://localhost:5000"
FILE_TO_HASH = "sample.AppImage" # replace with actual file name to monitor

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

# Generate hash
hash_value = calculate_sha512(FILE_TO_HASH)
if hash_value:
    data = {
        "filename": FILE_TO_HASH,
        "hash_value": hash_value,
        "hash_algorithm": "SHA-512"
    }
    response = requests.post(f"{SERVER_URL}/store_hash", json=data)
    print(response.json())

