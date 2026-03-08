from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import re
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'lab_security_secret_key'

app.permanent_session_lifetime = timedelta(minutes=5)

def init_db():
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, failed_attempts INTEGER DEFAULT 0)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/signup')
def signup():
    user = request.form['user']
    pw = request.form['pass']
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pw))
        conn.commit()
        return "User created! <a href='/'>Go back</a>"
    except:
        return "User already exists."
    finally:
        conn.close()

@app.route('/login-vulnerable', methods=['POST'])
def login_vulnerable():
    user = request.form['user']
    pw = request.form['pass']
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pw}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    if result:
        session['user'] = result[0]
        return redirect(url_for('dashboard'))
    return "Login Failed."

@app.route('/login-secure', methods=['POST'])
def login_secure():
    user = request.form['user']
    pw = request.form['pass']

    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    if not re.match(password_regex, pw):
        return "Security Error: Password does not meet complexity requirements."

    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
    row = cursor.fetchone()

    if not row:
        return "Invalid Credentials."

    if row[2] >= 3:
        return "Account Locked: Too many failed login attempts."

    if row[1] == pw:
        session.clear()
        session.permanent = True
        session['user'] = row[0]
        cursor.execute("UPDATE users SET failed_attempts = 0 WHERE username = ?", (user,))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    else:
        cursor.execute("UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?", (user,))
        conn.commit()
        conn.close()
        return "Invalid Credentials."

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"<h1>Welcome to the System, {session['user']}</h1><a href='/logout'>Logout</a>"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)