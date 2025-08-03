def safe_divide(numerator, denominator): 
        try: 
            num = float(numerator)
            denom = float(denominator)
            return f"The result of the division is {num / denom}"
        except ValueError:
            return "Error: Please enter numeric values only."
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        
