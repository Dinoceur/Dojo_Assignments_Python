class BankAccount:
    bank_name = "Give Austin Your Money Bank"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def yield_interest(self):
        self.balance *= self.int_rate
        return self

    def display_account_info(self):
        print (f'Balance: {self.balance}')

    @classmethod
    def all_balances(cls):
        for x in cls.all_accounts:
            x.display_account_info()

User1 = BankAccount(.10, 100000)
User2 = BankAccount(.05, 1000)

User1.deposit(5000).deposit(1000).withdraw(10000).display_account_info()
User2.deposit(5000).deposit(1000).withdraw(1000).withdraw(1000).display_account_info()

BankAccount.all_balances()