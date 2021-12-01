class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(.10, 0)
        self.account2 = BankAccount(0, 0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdraw(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print (f'User: {self.name}, Checking Balance: {self.account.balance}')

    #def transfer_money(self, amount, user):
        #self.balance -= amount
        #user.balance += amount
        #self.display_user_balance()
        #user.display_user_balance()

class BankAccount:
    bank_name = "Give Austin Your Money Bank"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    #def deposit(self, amount):
        #self.balance += amount
        #return self

    #def withdraw(self, amount):
        #self.balance -= amount
        #return self

    def yield_interest(self):
        self.balance *= self.int_rate
        return self

    def display_account_info(self):
        print (f'Checking Balance: {self.balance}')

    @classmethod
    def all_balances(cls):
        for x in cls.all_accounts:
            x.display_account_info()



User1 = User("Austin Kim", "austinkim14@gmail.com")
User2 = User("Aileen Wang", "ainiwang14@gmail.com")

User1.make_deposit(5000)
User1.make_deposit(7000)
User1.display_user_balance()

User2.make_deposit(100000)
User2.display_user_balance()