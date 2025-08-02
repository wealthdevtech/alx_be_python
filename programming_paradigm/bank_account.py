class BankAccount:
    
    def __init__(self, account_balance=0):
        self.account_balance = account_balance;
        
    def deposit(amount):
        account_balance += amount
        
    def withdraw(amount):
        if amount < account_balance:
            return False
        elif amount >= account_balance: 
            account_balance -= amount;
            
    def display_balance():
        return account_balance
