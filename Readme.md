# Hashing-Based Integrity Verification System

## Overview
This project implements a **hashing-based integrity verification system** using Python and SQL. It ensures file integrity by dynamically generating, storing, and verifying cryptographic hash values. The system monitors files in real time, detecting unauthorized modifications and alerting users if integrity is compromised.

## Features
- **Cryptographic Hashing**: Uses SHA-512 for file integrity verification.
- **SQL Database Integration**: Stores hash values securely with associated hash algorithms.
- **Real-Time Monitoring**: Detects modifications dynamically.
- **Flask API**: Provides endpoints for storing and retrieving hashes.
- **CLI Utility**: Allows manual integrity checks.
- **Cross-Platform Compatibility**: Works on Linux, Windows, and macOS.

## Technologies Used
- **Python** (Flask, Watchdog, SQLite3, hashlib, requests)
- **SQL** (SQLite for hash storage)
- **Flask** (REST API for hash retrieval and storage)
- **Watchdog** (File monitoring)

## Installation
### Prerequisites
Ensure you have Python 3 and `pip` installed.

```bash
pip install flask watchdog requests sqlite3
```

## Usage

### 1. Start the Hashing Server
Run the Flask-based hashing server to handle hash storage and retrieval:
```bash
python server.py
```
**Expected Output:**
```plaintext
[✔] Database Initialized
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.xxx:5000
Press CTRL+C to quit
```

### 2. Generate and Store Hashes
Use the following command to generate and store a hash using SHA-512:
```bash
python generate_hash.py
```
**Expected Output:**
```json
{"message": "Hash stored successfully"}
```

### 3. Monitor File Integrity
Start real-time monitoring for changes in the target file:
```bash
python monitor_integrity.py
```
**Expected Output (if file is unchanged):**
```plaintext
[🔍] Monitoring: firefox-135.0.r20250216192613-x86_64.AppImage
[✔] firefox-135.0.r20250216192613-x86_64.AppImage is safe ✅
```

**If the file is modified:**
```plaintext
[⚠] ALERT: firefox-135.0.r20250216192613-x86_64.AppImage has been modified! ❌
```

### 4. Client-Side Verification
To verify a file's integrity manually:
```bash
python client_verifier.py
```
**Expected Output:**
```plaintext
[✔] firefox-135.0.r20250216192613-x86_64.AppImage integrity verified ✅
```

## API Endpoints
### **Store File Hash**
- **Endpoint:** `POST /store_hash`
- **Payload:** `{ "filename": "file.ext", "hash_value": "<sha512-hash>", "hash_algorithm": "SHA-512" }`
- **Response:** `{ "message": "Hash stored successfully" }`

### **Retrieve Stored Hash**
- **Endpoint:** `GET /get_hash/<filename>`
- **Response:** `{ "filename": "file.ext", "hash_value": "<sha512-hash>", "hash_algorithm": "SHA-512" }`

## Future Enhancements
- Implement a web-based dashboard.
- Extend support for multiple hash algorithms.
- Add email/SMS alerts for integrity violations.
- Optimize hash comparison for large-scale monitoring.

## License
This project is open-source and available under the MIT License.

