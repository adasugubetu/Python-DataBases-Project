class NotEnoughBudgetException(Exception):
    pass


class Budget():
    def __init__(self, amount):
        self.amount = amount
        self.spent = 0

    def allocate(self, cost):
        if cost > self.remaining_budget():
            raise NotEnoughBudgetException("Not enough budget to allocate.")
        self.spent += cost

    def initial_budget(self):
        return self.amount

    def remaining_budget(self):
        return self.amount - self.spent