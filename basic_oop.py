class BanAccount:
    
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance
 
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            return "There is no balance from the withdrawal."
        return self.balance

    def get_balance(self):
        return f"The balance is:{self.withdraw(420)}"
    
bank = BanAccount(141201,2000)
print(bank.get_balance())