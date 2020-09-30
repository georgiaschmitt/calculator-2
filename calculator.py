"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                       power, mod, )
while True:
    equation = input("Enter the equation")
    tokens = equation.split(' ') 
    if "q" in tokens:
        print("You will exit.")
        break

# Replace this with your code
