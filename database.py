# database.py
import sqlite3
import os

DB_FILE = "visitor_logs.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visitor_id TEXT,
            event_type TEXT,
            timestamp TEXT,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(visitor_id, event_type, timestamp, image_path):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO logs (visitor_id, event_type, timestamp, image_path)
        VALUES (?, ?, ?, ?)
    ''', (visitor_id, event_type, timestamp, image_path))
    conn.commit()
    conn.close()
