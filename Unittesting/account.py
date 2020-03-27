class Account:

    def __init__(self, account_number: int, opening_date: str,
                 interest_rate: float, opening_balance: float):

        self.account_number = account_number
        self.opening_date = opening_date
        self.interest_rate = interest_rate
        self.opening_balance = opening_balance
        self.current_balance = opening_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        self.current_balance = self.current_balance - amount

    def transfer(self, amount, account_number):
        self.current_balance -= amount
        account_number.current_balance += amount


