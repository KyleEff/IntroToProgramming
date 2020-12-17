# Kyle Free
# ITSE 1302
# Calculator Minor Program
# Requirements:
#   Create a simple 4 function calculator
#   	User enters first number
#   	User enters one of four symbols:  +  -  *  /
#   	User enters second number
# Program calculates the answer based on the symbol entered
# Program displays the problem and the answer
# 0 1 - Initialization / Input
VALID = False
while not VALID:
    num1 = float(input('Enter a number: '))
    operator = input('Enter an operator (+ - * /): ')
    num2 = float(input('Enter a second number: '))
# 2 3 - Process / Output
    if operator == '+':
        print(f"{num1} {operator} {num2} = {num1+num2}")
        break
    elif operator == '-':
        print(f"{num1} {operator} {num2} = {num1-num2}")
        break
    elif operator == '*':
        print(f"{num1} {operator} {num2} = {num1*num2}")
        break
    elif operator == '/':
        print(f"{num1} {operator} {num2} = {num1/num2}")
        break
    else:
        print(f"The only operators allowed are '+ - * /'. You entered a {operator}. Please try again.\n")
