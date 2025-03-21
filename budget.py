import sqlite3
from datetime import datetime

def create_budget_table():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            month TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def set_budget(user_id, category, amount, month):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # Check if budget for the given user, category, and month already exists
    cursor.execute('''
        SELECT id FROM budgets WHERE user_id = ? AND category = ? AND month = ?
    ''', (user_id, category, month))
    budget = cursor.fetchone()
    if budget:
        # Update the existing budget
        cursor.execute('''
            UPDATE budgets
            SET amount = ?
            WHERE id = ?
        ''', (amount, budget[0]))
    else:
        # Insert a new budget
        cursor.execute('''
            INSERT INTO budgets (user_id, category, amount, month)
            VALUES (?, ?, ?, ?)
        ''', (user_id, category, amount, month))
    conn.commit()
    conn.close()

def check_budget(user_id, category, month):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    
    # Fetch the budget for the specified user, category, and month
    cursor.execute('''
        SELECT amount
        FROM budgets
        WHERE user_id = ? AND category = ? AND month = ?
    ''', (user_id, category, month))
    budget = cursor.fetchone()
    
    if budget:
        budget_amount = budget[0]
        print(f"Budget for {category} in {month}: {budget_amount}")
    else:
        print(f"No budget set for {category} in {month}.")
        conn.close()
        return
    
    # Calculate the total expenses for the specified category and month
    cursor.execute('''
        SELECT SUM(amount)
        FROM transactions
        WHERE user_id = ? AND category = ? AND type = 'expense' AND strftime('%Y-%m', date) = ?
    ''', (user_id, category, month))
    total_expenses = cursor.fetchone()[0] or 0
    
    conn.close()
    
    if total_expenses <= budget_amount:
        print(f"You are within the budget for {category} in {month}.")
    else:
        print(f"You have exceeded the budget for {category} in {month} by {total_expenses - budget_amount}.")

if __name__ == '__main__':
    # Example usage
    create_budget_table()
    set_budget(2, 'coin', 1000, '2022-05')
    check_budget(2, 'coin', '2022-05')