import sqlite3
import hashlib

def create_user(username, password):
    conn = sqlite3.connect('finance_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT)''')
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Username already exists.")
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('finance_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == hashlib.sha256(password.encode()).hexdigest():
        return True
    return False

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_user(username, password)
    print("User registered successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if authenticate_user(username, password):
        print("Login successful!")
    else:
        print("Invalid credentials!")
