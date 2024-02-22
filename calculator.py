#checks if number is correctly inputed
def input_numbers(num):
    while True:
        try:
            num = eval(input(num))
            return num
        except (NameError, SyntaxError):
            print("Invalid input! Please enter a valid number.")

#checks if operator is correctly inputed
def input_operators(op):
    while True:
        op = input(op)
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid input! Please enter a valid operator (+, -, *, /).")
            continue

# function performs arithmetic operations on two numbers 
def calculating (x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y

# function returns the result of an arithmetic operation, eliminates division by 0
def final_result (x, y, op):
    if op == "/" and y == 0:
        return "Error! Can't be divided by zero"
    else:
        result = calculating (x, y, op)
        return f"\nResult: {x} {op} {y} = {result}"
        
#recieves inputed numbers and operation, prints final result, checks if user wants to use it again
while True:
    x = input_numbers("\nEnter first number: ")
    y = input_numbers("Enter second number: ")
    op = input_operators("Enter operator (+, -, *, /): ")

    print(final_result(x, y, op))

    repeat = input("\nDo you want to use the calculator again? (yes/no): ").lower().strip()
    if repeat != "yes":
        break

     