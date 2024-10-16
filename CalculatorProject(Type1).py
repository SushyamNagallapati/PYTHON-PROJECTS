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

def calculator():
    print(art.logo)

    should_accumulate = True
    n1 = int(input("What's the first number: "))

    while should_accumulate:

        print("+\n-\n*\n/")

        pick_an_operation = input("Pick an operation: ")

        n2 = int(input("What's the second number: "))

        for result in operations:
            if pick_an_operation == "+":
                result = operations["+"](n1, n2)
            elif pick_an_operation == "-":
                result = operations["-"](n1, n2)
            elif pick_an_operation == "*":
                result = operations["*"](n1, n2)
            elif pick_an_operation == "/":
                result = operations["/"](n1, n2)

        print(f"{n1} {pick_an_operation} {n2} = {result}")

        continue_or_new = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if continue_or_new == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()


