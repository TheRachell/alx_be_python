def main(): 
    try: 

        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
        operation = input("choose the operation (+, -, *, /): ")
    
        match operation:
            case "+":
                result = num1 + num2 
                print(f"the result is {result}")
            case "-":
                result = num1 - num2 
                print(f"the result is {result}")
            case "*":
                result = num1 * num2 
                print(f"the result is {result}")
            case "/":
                if num2 == 0:
                    print("cannot divide by zero.")
                else: 
                    result = num1 / num2
                    print(f"the result is {result}.")
            case _:
                print("invalid operation. please choose one of +, -, *, /")
    except ValueError:
        print("invalid input. please enter numeric values")

main()
    