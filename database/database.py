# database.py
import sqlite3

def get_connection():
    return sqlite3.connect('astro_tracker.db')

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT UNIQUE,
            location TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    # Repeat for other tables
    conn.commit()
    conn.close()

def add_user(user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, location) VALUES (?, ?, ?)', (user.username, user.email, user.location))
    conn.commit()
    conn.close()

# More functions to interact with other tables
