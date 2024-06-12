# database/schema.py
from .connection import get_db_connection

def create_tables():
    """ Create tables in the database based on the defined schema. """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE,
        location TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # Celestial Objects Table
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

    # Observations Table
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

    # Events Table
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

    # Weather Conditions Table
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

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
