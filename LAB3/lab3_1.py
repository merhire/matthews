class BankAccount:
    accounts_count = 0
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        BankAccount.accounts_count += 1
    def deposit(self, amount):
        self.balance += amount
    def out(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
    def check_balance(self):
        print(self.balance)
        
print(BankAccount.accounts_count)
account = BankAccount("12345", 500)
print(BankAccount.accounts_count)
account.check_balance()
account.deposit(200)
account.check_balance()
account.out(100)
account.check_balance()