import math

def calculator():
    print(" Smart Calculator (with math module)")
    print("Supported operations: +, -, *, /, ^ (power), sqrt, ! (factorial), exit")

    while True:
        op = input("\nEnter operation (+, -, *, /, ^, sqrt, !, exit): ").strip()

        if op == 'exit':
            print(" Goodbye!")
            break

        # For operations that need 2 numbers
        if op in ['+', '-', '*', '/', '^']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if op == '+':
                print("Result:", x + y)
            elif op == '-':
                print("Result:", x - y)
            elif op == '*':
                print("Result:", x * y)
            elif op == '/':
                if y == 0:
                    print(" Error: Division by zero")
                else:
                    print("Result:", x / y)
            elif op == '^':
                print("Result:", math.pow(x, y))

        # For square root
        elif op == 'sqrt':
            try:
                x = float(input("Enter number: "))
                if x < 0:
                    print(" Error: Cannot take square root of negative number")
                else:
                    print("Result:", math.sqrt(x))
            except ValueError:
                print(" Please enter a valid number.")

        # For factorial
        elif op == '!':
            try:
                n = int(input("Enter a non-negative integer: "))
                if n < 0:
                    print(" Error: Factorial of negative number not defined")
                else:
                    print("Result:", math.factorial(n))
            except ValueError:
                print(" Please enter a valid integer.")

        else:
            print(" Invalid operation. Try again.")

# Run it
calculator()


