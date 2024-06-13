# database/seed.py
from .connection import get_db_connection

def seed_data():
    """ Seed the database with initial data. """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Seed users
    cursor.execute("INSERT INTO users (username, email, location) VALUES ('testuser', 'test@example.com', 'Earth')")
    cursor.execute("INSERT INTO users (username, email, location) VALUES ('skywatcher', 'watcher@sky.com', 'Mars')")

    # Seed celestial objects
    cursor.execute("""
        INSERT INTO celestial_objects (name, type, constellation, right_ascension, declination, magnitude, description)
        VALUES ('Mars', 'Planet', 'Aries', 5.233, -0.2, 2.8, 'Red Planet')
    """)
    cursor.execute("""
        INSERT INTO celestial_objects (name, type, constellation, right_ascension, declination, magnitude, description)
        VALUES ('Venus', 'Planet', 'Taurus', 1.233, -1.2, 4.8, 'Bright Planet')
    """)

    # Seed observations
    cursor.execute("""
        INSERT INTO observations (user_id, celestial_object_id, date, notes, equipment_used)
        VALUES (1, 1, '2024-06-15', 'Clear view, good conditions', 'Telescope XT2000')
    """)
    cursor.execute("""
        INSERT INTO observations (user_id, celestial_object_id, date, notes, equipment_used)
        VALUES (2, 2, '2024-06-16', 'Partly cloudy but visible', 'Binoculars B450')
    """)

    # Seed events
    cursor.execute("""
        INSERT INTO events (name, description, visibility_location, start_date, end_date)
        VALUES ('Lunar Eclipse', 'A total lunar eclipse visible in North America', 'North America', '2024-10-14', '2024-10-14')
    """)
    cursor.execute("""
        INSERT INTO events (name, description, visibility_location, start_date, end_date)
        VALUES ('Meteor Shower', 'The Perseids, a spectacular meteor shower', 'Global', '2024-08-12', '2024-08-13')
    """)

    # Seed weather conditions
    cursor.execute("""
        INSERT INTO weather_conditions (observation_id, date, condition, temperature, humidity)
        VALUES (1, '2024-06-15', 'Clear', 15, 50)
    """)
    cursor.execute("""
        INSERT INTO weather_conditions (observation_id, date, condition, temperature, humidity)
        VALUES (2, '2024-06-16', 'Cloudy', 22, 60)
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_data()
