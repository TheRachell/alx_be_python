FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 

def main():
    try: 
        temperature = input("enter the temperature to convert: ")
        if not temperature.replace('.', '', 1).isdigit() and not temperature.istrip('-').replace('.', '', 1).isdigit():
            raise ValueError("invalid temperature. please enter a numeric value.")
        
        temperature = float(temperature)

        unit = input("is this temperature in celsius or fahrenheit? (C/F): ")
        if unit == 'c':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}C is {converted_temp:.2f}F")
        elif unit == 'f':
           converted_temp = convert_to_celsius(temperature)
           print(f"{temperature}F is {converted_temp:.2f}C")
        else:
            print("invalid unit. please enter 'c' for celsius or 'f' for fahrenheit")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()