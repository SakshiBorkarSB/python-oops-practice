class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Rs.{amount} deposited successfully")
            else:
                print("Enter valid deposit amount")
        
    def withdraw(self, amount):
            if amount <= 0:
                print("Enter valid withdrawal amount")
            elif amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Rs.{amount} successfully withdrawn")
        
    def check_balance(self):
            print(f"Current Balance: Rs.{self.balance}")

acc1 = BankAccount(1234, "Sara", 10_000)

acc1.deposit(10_000)
acc1.withdraw(5_000)
acc1.check_balance()
