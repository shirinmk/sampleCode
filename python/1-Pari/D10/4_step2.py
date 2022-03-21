# Calculator
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
    "/": divide
}
continue_mode = True


num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
while continue_mode:
    # Here we select "+"
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    user_choice = input("do you want to continue:")
    if user_choice == "no":
        continue_mode = False
    else:
        # here is point to adjust
        num1 = result
