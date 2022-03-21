# calculator
# mathmatical operations

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# create dictionary keys are operations and values are the name of functipons

operations = {}
operations["*"] = multiply
operations['+'] = add
operations['/'] = divide
operations['-'] = subtract
print(operations)

# ask user to enter two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))
user_operation = input("enter operation: ")
for _ in operations:
    print(_)
for symbol in operations:
    if user_operation == symbol:
        print(operations[symbol])
        # how to pass values in this function?
        result = operations[symbol](num1,
                                    num2)
        print(f"{num1} {symbol} {num2} = {result}")

