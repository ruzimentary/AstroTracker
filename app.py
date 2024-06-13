from flask import Flask, render_template, request, redirect, url_for, flash
from database.connection import get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    """ Establishes a database connection and returns the connection object. """
    connection = sqlite3.connect('database/astro_tracker.db')
    connection.row_factory = sqlite3.Row  
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, location FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('list_users.html', users=users)

@app.route('/add_user', methods=('GET', 'POST'))
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        location = request.form['location']
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, location) VALUES (?, ?, ?)", (username, email, location))
            conn.commit()
            flash('User added successfully!', 'success')
        except sqlite3.IntegrityError as e:
            flash(f"Error adding user: {e}", 'danger')
        finally:
            conn.close()
        return redirect(url_for('list_users'))
    return render_template('add_user.html')

# Add routes for other functionalities similarly

if __name__ == '__main__':
    app.run(debug=True)
