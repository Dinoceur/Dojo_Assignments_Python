class User:
    def __init__(self, name, email_address, balance):
        self.name = name
        self.email = email_address
        self.balance = balance
    

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print (f'User: {self.name}, Email: {self.email}, Balance: {self.balance}')

    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount
        self.display_user_balance()
        user.display_user_balance()

austin = User("Austin Kim", "austinkim14@gmail.com", 100000)
harold = User("harold Kim", "haroldkim14@gmail.com", 1000)
jessica = User("jessica Kim", "jessicakim14@gmail.com", 1000000)

austin.make_deposit(5000).make_deposit(1000).make_withdraw(10000).display_user_balance()
harold.make_deposit(5000).make_deposit(1000).make_withdraw(1000).make_withdraw(1000).display_user_balance()
jessica.make_deposit(9000).make_withdraw(1000).make_withdraw(1000).make_withdraw(1000).display_user_balance()

austin.transfer_money(1000, harold)