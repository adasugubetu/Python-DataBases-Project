class Finance:
    def __init__(self):
        self.income = 0
        self.expenses = 0

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, amount):
        self.expenses += amount

    def net_balance(self):
        return self.income - self.expenses