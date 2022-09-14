from sys import float_repr_style
from art import logo

print(logo)
firstNumber = float(input("Enter the first number: "))
print("+\n-\n*\n/\n**")
operation = input("Enter the operation: ")
lastNumber = float(input("Enter the last number: "))

def add(firstNumber, lastNumber):
    """Sum of two numbers"""
    return firstNumber + lastNumber

def subtract(firstNumber, lastNumber):
    """Subtract of two numbers"""
    return firstNumber - lastNumber

def multiply(firstNumber, lastNumber):
    """Multiply of two numbers"""
    return firstNumber * lastNumber

def divide(firstNumber, lastNumber):
    """Divide of two numbers"""
    return firstNumber / lastNumber

def exponent(firstNumber, lastNumber):
    """Exponent of two numbers"""
    return firstNumber ** lastNumber

def resolve(firstNumber, lastNumber):
    if operation == "+":
        result = add(firstNumber, lastNumber)

    if operation == "-":
        result = subtract(firstNumber, lastNumber)

    if operation == "*":
        result = multiply(firstNumber, lastNumber)

    if operation == "/":
        result = divide(firstNumber, lastNumber)

    if operation == "**":
        result = exponent(firstNumber, lastNumber)
    
    return result

result = float(resolve(firstNumber, lastNumber))
print(result)

print(f"\nType 'y' to continue calculating with {result}, or type 'n' to exit: ")
choice = input("Enter your choice: \n")

while choice == "y" or choice == "Y":
    operation = input("Enter the operation: ")
    lastNumber = float(input("Enter the last number: "))

    result = float(resolve(result, lastNumber))
    print(result)
    
    print(f"\nType 'y' to continue calculating with {result}, or type 'n' to exit: ")
    choice = input("Enter your choice: \n")
