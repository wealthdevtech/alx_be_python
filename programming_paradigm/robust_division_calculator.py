class safe_divide:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def safe_divide(self, numerator, denominator): 

        self.numerator = float(numerator)
        self.denominator = float(denominator)
        
        try:
            return (f"The result of the division is {self.numerator / self.denominator}")
        except ValueError:
            return ("Error: Please enter numeric values only.")
        except ZeroDivisionError:
            return ("Error: Cannot divide by zero.")
