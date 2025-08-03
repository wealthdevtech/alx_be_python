class safe_divide1:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def safe_divide(self, numerator, denominator): 
        
        try:
            
            self.numerator = float(numerator)
            self.denominator = float(denominator)
        
            self.result = (f"The result of the division is {self.numerator / self.denominator}")
        except ValueError:
            self.result = ("Error: Please enter numeric values only.")
        except ZeroDivisionError:
            self.result = ("Error: Cannot divide by zero.")
        
        return self.result;
