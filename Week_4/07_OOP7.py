class Account:

    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self):
        value = True
        while value:
            choice = input("Do you want to withdraw money")
            if choice == "y":
                amount = int(input("Enter amount"))
                if amount < self.balance:
                    self.balance -= amount
                else:
                    print("Invalid balance")
            else:
                value = False

    def information(self):
        print(self.name, "Account Number:", self.no, "Balance:", self.balance)


account1 = Account("John Cook", 123456, 20000)
account1.information()
account1.deposit(2000)
account1.information()
account1.deposit(4000)
account1.withdraw()
account1.information()

account2 = Account("Liz Osvaldo", 2345172, 30000)
account2.deposit(3000)
account2.information()
