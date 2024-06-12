import sqlite3
import os

def ensure_directory_exists():
    """
    Ensures that the 'database' directory exists.
    """
    os.makedirs('database', exist_ok=True)

def get_connection():
    """
    Establishes a connection to the SQLite database.
    Ensures the directory exists before trying to connect.
    Returns a connection object.
    """
    ensure_directory_exists()
    return sqlite3.connect('database/database.db')

def create_tables():
    """
    Creates necessary database tables if they do not exist.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE,
            location TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS celestial_objects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            constellation TEXT,
            right_ascension REAL,
            declination REAL,
            magnitude REAL,
            description TEXT
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            celestial_object_id INTEGER,
            date TIMESTAMP,
            notes TEXT,
            equipment_used TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (celestial_object_id) REFERENCES celestial_objects(id)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            visibility_location TEXT,
            start_date TIMESTAMP,
            end_date TIMESTAMP
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_conditions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            observation_id INTEGER,
            date TIMESTAMP,
            condition TEXT,
            temperature REAL,
            humidity REAL,
            FOREIGN KEY (observation_id) REFERENCES observations(id)
        );
        ''')
        conn.commit()
    finally:
        conn.close()

def add_user(username, email, location):
    """
    Adds a new user to the database.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, location) VALUES (?, ?, ?)', (username, email, location))
        conn.commit()
    finally:
        conn.close()

def add_celestial_object(name, type, constellation, right_ascension, declination, magnitude, description):
    """
    Adds a new celestial object to the database.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO celestial_objects (name, type, constellation, right_ascension, declination, magnitude, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, type, constellation, right_ascension, declination, magnitude, description))
        conn.commit()
    finally:
        conn.close()

if __name__ == '__main__':
    # Create database tables upon script execution
    create_tables()

  