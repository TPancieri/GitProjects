import typing

def add(number1, number2) -> typing.Union[int, float]:
    return number1 + number2

def subtract(number1, number2) -> typing.Union[int, float]:
    return number1 - number2

def multiply(number1, number2) -> typing.Union[int, float]:
    return number1 * number2

def divide(number1, number2) -> typing.Union[int, float]:
    if number2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return number1 / number2

def calculate(number1, operator, number2) -> typing.Union[int, float]:
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    if operator not in operations:
        raise ValueError("Invalid operator!")
    return operations[operator](number1, number2)

def main():
    while True:
        try:
            number1 = float(input("What's the first number?"))
            operator = input("What's the operator? (+, -, *, /)")
            number2 = float(input("What's the second number?"))

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
        except ZeroDivisionError as e:
            print(f"Error:  {e}")

if __name__ == "__main__":
    main()
