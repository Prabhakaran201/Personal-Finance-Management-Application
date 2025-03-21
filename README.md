# Personal Finance Management Application

This is a command-line application for managing personal finances. The application allows users to register, login, add transactions, update transactions, delete transactions, list transactions, generate financial reports, set budgets, and check budgets.

## Features

- **Register**: Allows a new user to register.
- **Login**: Allows an existing user to login.
- **Add Transaction**: Allows the user to add a new transaction (income or expense).
- **Update Transaction**: Allows the user to update an existing transaction.
- **Delete Transaction**: Allows the user to delete an existing transaction.
- **List Transactions**: Lists all transactions for a specific user.
- **Generate Report**: Generates monthly or yearly financial reports, including total income, expenses, and savings.
- **Set Budget**: Allows the user to set a budget for a specific category and month.
- **Check Budget**: Checks if the user is within the budget for a specific category and month.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Prabhakaran201/Personal-Finance-Management-Application.git
   cd personal-finance-management
   ```

2. Install dependencies:
   ```sh
   pip install tabulate
   tabulate==0.8.9
   ```

3. Create the necessary database tables by running the application and selecting any menu option. The tables will be created automatically.

## Usage

Run the main program using the following command:
```sh
python main.py
```

Follow the on-screen instructions to register, login, and manage your personal finances.

### Menu Options

1. **Register**: Register a new user by providing a username and password.
2. **Login**: Login with an existing username and password.
3. **Add Transaction**: Add a new transaction by providing the user ID, type (income/expense), category, amount, and date.
4. **Update Transaction**: Update an existing transaction by providing the transaction ID and new details.
5. **Delete Transaction**: Delete an existing transaction by providing the transaction ID.
6. **List Transactions**: List all transactions for a specific user.
7. **Generate Report**: Generate a financial report for a specific user and period (monthly/yearly).
8. **Set Budget**: Set a budget for a specific category and month by providing the user ID, category, amount, and month.
9. **Check Budget**: Check if the user is within the budget for a specific category and month by providing the user ID, category, and month.
0. **Exit**: Exit the application.

## Code Structure

- `main.py`: The main entry point of the application. Contains the main menu and handles user input.
- `auth.py`: Contains functions for user registration and login.
- `transactions.py`: Contains functions for managing transactions (add, update, delete, list).
- `reports.py`: Contains functions for generating financial reports.
- `budget.py`: Contains functions for setting and checking budgets.

## Example

Here's an example of how to use the application:

1. **Register a new user**:
   ```sh
   Enter your choice: 1
   Enter username: user1
   Enter password: pass1
   User registered successfully!
   ```

2. **Login with an existing user**:
   ```sh
   Enter your choice: 2
   Enter username: user1
   Enter password: pass1
   Login successful!
   ```

3. **Add a new transaction**:
   ```sh
   Enter your choice: 3
   Enter user ID: 1
   Enter transaction type (income/expense): income
   Enter category: salary
   Enter amount: 5000
   Enter date (YYYY-MM-DD): 2025-03-21
   Transaction added successfully!
   ```

4. **Generate a monthly report**:
   ```sh
   Enter your choice: 7
   Enter user ID: 1
   Enter period (monthly/yearly): monthly
   Financial Report:
   Period        Income        Expenses      Savings
   2025-03       5000.0        0.0           5000.0
   ```

## License

This project is licensed under the MIT License.
