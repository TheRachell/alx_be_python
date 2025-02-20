def safe_divide(numerator, denominator):
    try: 
        num = float(numerator)
        den = float(denominator)

        if den == 0 :
            ZeroDivisionError
            return "Error: cannot divide by zero"
        return f"The result of the division is {num/den}"
    
    except ValueError:
        return "Error: please enter numeric values only."