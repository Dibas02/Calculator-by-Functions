def add(num1, num2):
    result = num1+num2
    return result


def subtract(num1, num2):
    result = num1-num2
    return result

def multiply(num1, num2):
    result = num1*num2
    return result

def divide(num1, num2):
    result = num1/num2
    return result

print("Welcome to the calculator!!!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Enter the operation you want to perform")
operation = input('"add" for addition, "subtract" for subtraction, "multiply" for multiplication and "divide" for division: ')

if operation.lower() == "add":
    print(add(num1, num2))

elif operation.lower() == "subtract":
    print(subtract(num1, num2))

elif operation.lower() == "multiply":
    print(multiply(num1, num2))

elif operation.lower() == "divide":
    print(divide(num1, num2))

else:
    print("Your operation is invalid,")

