from logo import logo

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("Enter first number: "))
    dummy = True # recursion icin sey
    while dummy:
        operation = input("choose an operation to do: ")
        num2 = float(input("Enter the next number: "))
        function = operations[operation]
        answer = function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")
        bruh = input("type 'y' to continue, or type 'n' to start a new calculation: ")
        if bruh == "y":
            num1 = answer
        else:
            dummy = False
            calculator() # kendi kendini cagiriyoruz. recursion


calculator()
