from unittest import TestCase
from Unittesting.account import Account


class AccountTest(TestCase):

    def setUp(self):
        self.acc1 = Account(1, '01-01-2020', 0.2, 5000)
        self.acc2 = Account(2, '01-02-2020', 0.3, 10000)

    def test_create_account(self):
        self.assertEqual(self.acc1.account_number, 1)
        self.assertEqual(self.acc1.opening_date, '01-01-2020')
        self.assertEqual(self.acc1.interest_rate, 0.2)
        self.assertEqual(self.acc1.opening_balance, 5000)
        self.assertEqual(self.acc1.current_balance, 5000)

        self.assertEqual(self.acc2.account_number, 2)
        self.assertEqual(self.acc2.opening_date, '01-02-2020')
        self.assertEqual(self.acc2.interest_rate, 0.3)
        self.assertEqual(self.acc2.opening_balance, 10000)
        self.assertEqual(self.acc2.current_balance, 10000)

    def test_withdraw(self):
        self.acc1.withdraw(100)
        self.assertEqual(self.acc1.current_balance, 4900)
        self.acc2.withdraw(200)
        self.assertEqual(self.acc2.current_balance, 9800)

    def test_deposit(self):
        self.acc1.deposit(3000)
        self.acc2.deposit(1500)

        self.assertEqual(self.acc1.current_balance, 8000)
        self.assertEqual(self.acc2.current_balance, 11500)

    def test_transfer(self):
        self.acc1.transfer(self.acc2, 100)

        self.assertEqual(self.acc1.current_balance, 4900)
        self.assertEqual(self.acc2.current_balance, 10100)
