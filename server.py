from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)
DB_FILE = "hash_store.db"

# Function to initialize the database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS hash_records (
                        filename TEXT PRIMARY KEY, 
                        hash_value TEXT,
                        hash_algorithm TEXT)''')
    print("[✔] Database Initialized")

# Route to store hash
@app.route('/store_hash', methods=['POST'])
def store_hash():
    data = request.json
    filename = data.get('filename')
    hash_value = data.get('hash_value')
    hash_algorithm = data.get('hash_algorithm')

    if not filename or not hash_value or not hash_algorithm:
        return jsonify({"error": "Missing required parameters"}), 400

    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT OR REPLACE INTO hash_records VALUES (?, ?, ?)", 
                     (filename, hash_value, hash_algorithm))
    
    return jsonify({"message": "Hash stored successfully"}), 201

# Route to retrieve hash by filename
@app.route('/get_hash/<filename>', methods=['GET'])
def get_hash(filename):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT hash_value, hash_algorithm FROM hash_records WHERE filename=?", (filename,))
        row = cursor.fetchone()
    
    if row:
        return jsonify({"filename": filename, "hash_value": row[0], "hash_algorithm": row[1]})
    else:
        return jsonify({"error": "Hash not found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

