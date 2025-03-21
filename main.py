from auth import register, login
from transactions import create_transaction_table, add_transaction, update_transaction, delete_transaction, list_transactions
from reports import generate_report, print_report
from budget import create_budget_table, set_budget, check_budget
from tabulate import tabulate
from datetime import datetime

def handle_add_transaction():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    while True:
        type = input("Enter transaction type (income/expense): ").lower()
        if type in ["income", "expense"]:
            break
        else:
            print("Invalid transaction type. Please enter 'income' or 'expense'.")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    add_transaction(user_id, type, category, amount, date)
    print("Transaction added successfully!")

def handle_update_transaction():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    transactions = list_transactions(user_id)
    print("Transactions:")
    print(tabulate(transactions, headers=["ID", "User ID", "Type", "Category", "Amount", "Date"], tablefmt="grid"))
    transaction_ids = [transaction[0] for transaction in transactions]
    while True:
        transaction_id = input("Enter the transaction ID to update or type 'exit' to cancel: ").lower()
        if transaction_id == "exit":
            print("Update cancelled. Returning to main menu.")
            break
        try:
            transaction_id = int(transaction_id)
            if transaction_id in transaction_ids:
                while True:
                    type = input("Enter transaction type (income/expense): ").lower()
                    if type in ["income", "expense"]:
                        break
                    else:
                        print("Invalid transaction type. Please enter 'income' or 'expense'.")
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                update_transaction(transaction_id, type, category, amount, date)
                print("Transaction updated successfully!")
                break
            else:
                print("Invalid transaction ID. Please enter a valid transaction ID from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid transaction ID or 'exit'.")

def handle_delete_transaction():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    transactions = list_transactions(user_id)
    print("Transactions:")
    print(tabulate(transactions, headers=["ID", "User ID", "Type", "Category", "Amount", "Date"], tablefmt="grid"))
    transaction_ids = [transaction[0] for transaction in transactions]
    while True:
        transaction_id = input("Enter the transaction ID to delete or type 'exit' to cancel: ").lower()
        if transaction_id == "exit":
            print("Deletion cancelled. Returning to main menu.")
            break
        try:
            transaction_id = int(transaction_id)
            if transaction_id in transaction_ids:
                delete_transaction(transaction_id)
                print("Transaction deleted successfully!")
                break
            else:
                print("Invalid transaction ID. Please enter a valid transaction ID from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid transaction ID or 'exit'.")

def handle_list_transactions():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    transactions = list_transactions(user_id)
    transaction_ids = [transaction[0] for transaction in transactions]
    if transaction_ids:
        print("You have the following transaction IDs: " + ", ".join(map(str, transaction_ids)) + " or 'all'")
        transaction_id = input("Enter the transaction ID to view details or 'all' to list all transactions: ").lower()
        if transaction_id == "all":
            print("\nAll Transactions:")
            print(tabulate(transactions, headers=["ID", "User ID", "Type", "Category", "Amount", "Date"], tablefmt="grid"))
        else:
            try:
                transaction_id = int(transaction_id)
                selected_transaction = next((transaction for transaction in transactions if transaction[0] == transaction_id), None)
                if selected_transaction:
                    print(f"\nTransaction Details:\nID: {selected_transaction[0]}\nUser ID: {selected_transaction[1]}\nType: {selected_transaction[2]}\nCategory: {selected_transaction[3]}\nAmount: {selected_transaction[4]}\nDate: {selected_transaction[5]}")
                else:
                    print("Invalid transaction ID.")
            except ValueError:
                print("Invalid input. Please enter a valid transaction ID or 'all'.")
    else:
        print("No transactions found for this user.")

def handle_generate_report():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    period = input("Enter period (monthly/yearly): ")
    report = generate_report(user_id, period)
    print_report(report)

def handle_set_budget():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    category = input("Enter category: ")
    amount = float(input("Enter budget amount: "))
    month = input("Enter month (YYYY-MM): ")
    set_budget(user_id, category, amount, month)
    print("Budget set successfully!")

def handle_check_budget():
    while True:
        user_id_input = input("Enter user ID: ")
        try:
            user_id = int(user_id_input)
            break
        except ValueError:
            print("Invalid user ID. Please enter a numeric user ID.")
    category = input("Enter category: ")
    month = input("Enter month (YYYY-MM): ")
    check_budget(user_id, category, month)

def main():
    create_transaction_table()  # Ensure the transactions table is created
    create_budget_table()

    print("Welcome to the Personal Finance Management Application")
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Add Transaction")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. List Transactions")
        print("7. Generate Report")
        print("8. Set Budget")
        print("9. Check Budget")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            handle_add_transaction()
        elif choice == '4':
            handle_update_transaction()
        elif choice == '5':
            handle_delete_transaction()
        elif choice == '6':
            handle_list_transactions()
        elif choice == '7':
            handle_generate_report()
        elif choice == '8':
            handle_set_budget()
        elif choice == '9':
            handle_check_budget()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()