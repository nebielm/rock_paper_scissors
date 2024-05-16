class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


my_account = BankAccount(872372, 100000)

my_account.deposit(100000)

my_account.withdraw(20)

print(my_account.balance)



class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def substract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def devide(self, num1, num2):
        return num1 / num2

print(Calculator.add(3, 4))
