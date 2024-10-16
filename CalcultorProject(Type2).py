import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    print(art.logo)
    num1 = float(input("What's the first number: "))

    game = True
    while game:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the second number: "))

        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        new = input(f"Type 'y' to continue calculating with {result}, or Type 'n' to start a new calculation: ").lower()
        if new == "y":
            num1 = result
        else:
            game = False
            print("\n" * 20)
            calculate()
calculate()



