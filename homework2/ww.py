class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Додано {amount}. Новий баланс: {self.balance}"
        return "Сума для поповнення повинна бути більше 0."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Недостатньо коштів для зняття."
        if amount <= 0:
            return "Сума для зняття повинна бути більше 0."
        self.balance -= amount
        return f"Знято {amount}. Новий баланс: {self.balance}"
