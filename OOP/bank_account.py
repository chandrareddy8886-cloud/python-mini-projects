class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, Add):
        print(f"Ammout diposited  : {Add}")
        self.balance=self.balance+Add
        print(f"Balance : {self.balance}")

    def withdraw(self, draw):
        print(f"Withdrawl amount : {draw}")
        self.balance=self.balance-draw
        print(f"Balance : {self.balance}")

    def show_balance(self):
        print(f"Account Balance : {self.balance}")


acc1 = BankAccount("ravi", 1000)
acc1.show_balance()
acc1.deposit(500)
acc1.withdraw(200)
acc1.show_balance()
