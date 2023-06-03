def add(x, y):
    """
    Adds two numbers.

    Parameters:
        x (float or int): The first number.
        y (float or int): The second number.

    Returns:
        float or int: The sum of x and y.
    """
    return x + y


def subtract(x, y):
    """
    Subtracts two numbers.

    Parameters:
        x (float or int): The first number.
        y (float or int): The second number.

    Returns:
        float or int: The difference between x and y.
    """
    return x - y


def multiply(x, y):
    """
    Multiplies two numbers.

    Parameters:
        x (float or int): The first number.
        y (float or int): The second number.

    Returns:
        float or int: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides two numbers.

    Parameters:
        x (float or int): The numerator.
        y (float or int): The denominator.

    Returns:
        float or int or None: The result of dividing x by y. If division by zero occurs, None is returned.
    """
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None


while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting the program...")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")

            if '.' in num1 or '.' in num2:
                num1 = float(num1)
                num2 = float(num2)
            else:
                num1 = int(num1)
                num2 = int(num2)

            if choice == '1':
                result = add(num1, num2)
                print("Result:", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result:", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result:", result)
            else:
                result = divide(num1, num2)
                if result is not None:
                    print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

    else:
        print("Invalid input. Please try again.")
