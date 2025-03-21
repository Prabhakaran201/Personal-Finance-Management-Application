import unittest
from auth import create_user, authenticate_user
from transactions import add_transaction, list_transactions
from reports import generate_report
from budget import set_budget, check_budget

class TestFinanceApp(unittest.TestCase):

    def test_user_registration(self):
        create_user('testuser', 'testpass')
        self.assertTrue(authenticate_user('testuser', 'testpass'))

    def test_add_transaction(self):
        add_transaction(1, 'income', 'Salary', 5000, '2025-03-01')
        transactions = list_transactions(1)
        self.assertEqual(len(transactions), 1)

    def test_generate_report(self):
        report = generate_report(1, 'monthly')
        self.assertTrue(len(report) > 0)

    def test_set_budget(self):
        set_budget(1, 'Food', 500)
        check_budget(1, 'Food')
        # Add logic to verify budget check

if __name__ == '__main__':
    unittest.main()