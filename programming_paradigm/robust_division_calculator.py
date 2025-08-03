class safe_divide:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def safe_divide(self, numerator, denominator): 

        self.numerator = float(self.numerator)
        self.denominator = float(self.denominator)
        
        try:
            return self.numerator / self.denominator
        except ValueError:
            print("Error: Please enter numeric values only.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
