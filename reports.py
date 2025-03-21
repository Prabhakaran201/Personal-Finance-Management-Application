import sqlite3
from tabulate import tabulate

def generate_report(user_id, period):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    
    if period == 'monthly':
        cursor.execute('''
            SELECT strftime('%Y-%m', date) AS period,
                   SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS income,
                   SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS expense
            FROM transactions
            WHERE user_id = ?
            GROUP BY strftime('%Y-%m', date)
            ORDER BY period
        ''', (user_id,))
    elif period == 'yearly':
        cursor.execute('''
            SELECT strftime('%Y', date) AS period,
                   SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS income,
                   SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS expense
            FROM transactions
            WHERE user_id = ?
            GROUP BY strftime('%Y', date)
            ORDER BY period
        ''', (user_id,))
    else:
        return []
    
    report = cursor.fetchall()
    
    cursor.execute('''
        SELECT
            SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS total_income,
            SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expense
        FROM transactions
        WHERE user_id = ?
    ''', (user_id,))
    
    totals = cursor.fetchone()
    conn.close()
    
    if totals:
        report.append(('Total', totals[0], totals[1]))
    
    return report

def print_report(report):
    headers = ["Period", "Income", "Expense"]
    table = []
    for row in report:
        table.append([row[0], row[1], row[2]])
    print("\nReport:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == '__main__':
    # Example usage
    user_id = 2
    period = 'monthly'
    report = generate_report(user_id, period)
    print_report(report)

    period = 'yearly'
    report = generate_report(user_id, period)
    print_report(report)