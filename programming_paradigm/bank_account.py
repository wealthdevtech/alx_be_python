class BankAccount:
    
    def __init__(self, account_balance=0):
        self.account_balance = account_balance;
        
    def deposit(amount):
        account_balance += amount
        #print(f"Deposited: ${amount}")
        
    def withdraw(amount):
        if amount < account_balance:
            return False
        elif amount >= account_balance: 
            account_balance -= amount;
            #print(f"Withdrew: ${amount}")
            
    def display_balance():
        return True#print(f"Current balance: ${account_balance}")