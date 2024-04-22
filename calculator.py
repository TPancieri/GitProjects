import typing

def calculate(number1, operator, number2) -> typing.Union[int, float]:
    if operator == "+":
        return number1 + number2     
    elif operator == "-":
        return number1 - number2     
    elif operator == "*":
        return number1 * number2     
    elif operator == "/":
        if number2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return number1 / number2     
    else: 
        raise ValueError("Invalid operator!")

def main():
    while True:
        try:
            number1 = int(input("What's the first number?"))
            operator = input("What's the operator?")
            number2 = int(input("What's the second number?"))

            if operator not in "+-*/":
                raise ValueError("Invalid operator!")

            result = calculate(number1, operator, number2)
            print(result)
            
            print("Type y to continue or n to quit")
            choice = input().lower()
            
            if choice == 'y':
                continue
            elif choice == 'n':
                break
            else:
                print("Invalid choice")
        except ValueError as e:
            print(f"Error:  {e}")


if __name__ == "__main__":
    main()