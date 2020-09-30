"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                       power, mod, )
while True:
    equation = input("Enter the equation ")
    tokens = equation.split(' ') 
    if "q" in tokens:
        print("You will exit.")
        break

    else:
        if tokens[0] == '+':
            result = add(float(tokens[1]), float(tokens[2]))
        if tokens[0] == '-':
            result = subtract(float(tokens[1]), float(tokens[2]))
        if tokens[0] == '*':
            result = multiply(float(tokens[1]), float(tokens[2]))
        if tokens[0] == "/":
            result = divide(float(tokens[1]), float(tokens[2])) 
        if tokens[0] == "square":
            result = square(float(tokens[1]))  
        if tokens[0] == "cube":
            result = cube(float(tokens[1])) 
        if tokens[0] == "**":
            result = power(float(tokens[1]), float(tokens[2]))              
        if tokens[0] == "%":
            result = mod(float(tokens[1]), float(tokens[2]))              
    print(result)
