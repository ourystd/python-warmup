class User: ...


class Account:
    def __init__(self, balance: float, owner: User):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount
