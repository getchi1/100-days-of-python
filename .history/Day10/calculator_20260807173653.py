from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# operation = operators["+"](4,5)
# print(operation)
def calculator():
    n1 = float(input("What's the first number?: "))
    should_accumulate = True

    while should_accumulate:
        for key in operators:
            print(key)
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        result = operators[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

        continue_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_with_result == "y":
            n1 = float(result)
        else:
            should_accumulate = False
            print("\n" * 100)
            calculator()

calculator()






