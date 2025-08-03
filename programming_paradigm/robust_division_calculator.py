class safe_divide:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def safe_divide(self, numerator, denominator): 

        self.numerator = float(numerator)
        self.denominator = float(denominator)
        
        try:
            return self.numerator / self.denominator
        except ValueError:
            return print("Error: Please enter numeric values only.")
        except ZeroDivisionError:
            return print("Error: Cannot divide by zero.")
