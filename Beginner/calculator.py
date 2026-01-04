#  user's input

num_1 = int(input("Enter a number: "))

num_2 = int(input("Enter a number: "))

operator = input("Enter an operator: ")


def calculate(num_1, num_2, operator):

# valid operators: + - * /

    if operator == "+":

        add(num_1, num_2)

    elif operator == "-":

        subtract(num_1, num_2)

    elif operator == "*":

        multiply(num_1, num_2)

    elif operator == "//":

        divide(num_1, num_2)

    else:
        print("Invalid operator")

# calculation

def add(num_1, num_2):

    print(f"Result: {num_1 + num_2}")

def subtract(num_1, num_2):

    print(f"Result: {num_1 - num_2}")

def multiply(num_1, num_2):

    print(f"Result: {num_1 * num_2}")

def divide(num_1, num_2):

    if num_2 == 0:

        print("Error: Division by zero")

    else:

        print(f"Result: {num_1 // num_2}")

calculate(num_1, num_2, operator)
