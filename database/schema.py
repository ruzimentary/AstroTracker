from .connection import get_db_connection

def create_tables():
    """Create tables in the database based on the defined schema."""
    tables = {
        'users': '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE,
                location TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''',
        'celestial_objects': '''
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
        ''',
        'observations': '''
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
        ''',
        'events': '''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                visibility_location TEXT,
                start_date TIMESTAMP,
                end_date TIMESTAMP
            );
        ''',
        'weather_conditions': '''
            CREATE TABLE IF NOT EXISTS weather_conditions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                observation_id INTEGER,
                date TIMESTAMP,
                condition TEXT,
                temperature REAL,
                humidity REAL,
                FOREIGN KEY (observation_id) REFERENCES observations(id)
            );
        '''
    }

    conn = get_db_connection()
    cursor = conn.cursor()
    for table, schema in tables.items():
        cursor.execute(schema)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
