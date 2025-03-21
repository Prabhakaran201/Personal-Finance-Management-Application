import sqlite3

def create_transaction_table():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(user_id, type, category, amount, date):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (user_id, type, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, type, category, amount, date))
    conn.commit()
    conn.close()

def update_transaction(id, type, category, amount, date):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE transactions
        SET type = ?, category = ?, amount = ?, date = ?
        WHERE id = ?
    ''', (type, category, amount, date, id))
    conn.commit()
    conn.close()

def delete_transaction(id):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM transactions
        WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

def list_transactions(user_id):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, user_id, type, category, amount, date
        FROM transactions
        WHERE user_id = ?
    ''', (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions