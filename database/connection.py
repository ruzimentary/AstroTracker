# database/connection.py
import sqlite3

def get_db_connection(db_path='database/database.db'):
    """ Create and return a database connection. """
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row  # Optional: enables name-based access to columns
    return connection
