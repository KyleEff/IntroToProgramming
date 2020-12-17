# Kyle Free
# ITSE 1302
# Receipt Minor Program
# Requirements:
#   Simple Receipt: Write a program that computes the tax and tip on a restaurant bill.
#       The program should ask the user to enter the charge for the meal and whether the
#       service was poor, good or excellent.  The tax should be 8.25 percent of the meal
#       charge and be calculated in a function.  The tip percent should be determined
#       based on the user input, applied to the meal price and should also be
#       calculated in a function. Make sure that the value of the tip is limited to
#       2 digits past the decimal. See sample results for output.  Use constants
#       for tip percentages and tax percentage. Include comments for IPO and functions.
# Technical Requirements:
# •	Values that should be input from user:
#   o   Meal Price
#   o	Level of Service using menu as in Sample Results
# •	Global constants for tax rate, poor service tip rate, good service tip rate and great service tip rate
# •	Tax should be calculated via a function
# •	Tip should be calculated via a function
# •	Results should be limited to 2 places past the decimal and match formatting in sample results

SALES_TAX = 0.0825
POOR = 0.1
GOOD = 0.15
GREAT = 0.2


def main(c):
    # 0 1 - Initialization / Input
    quality = service()
    price = float(input(f'\nEnter the meal price {c}: $'))
    # 2 3 - Process / Output
    print(f"\n{'Service:':>12}{quality[0]:>6} {quality[1]:>3.0%}\n"
          f"Meal Charge:   ${price:6,.2f}\n"
          f"{'Tax:':>12}   ${sales_tax(price):6,.2f}\n"
          f"{'Tip:':>12}   ${tip(price,quality):6,.2f}\n"
          f"{'Total:':>12}   ${price + sales_tax(price) + tip(price,quality):6,.2f}\n")


def service():
    # 0 - Initialization
    level_dict = {1: ("Poor", 0.1), 2: ("Good", 0.15), 3: ("Great", 0.2)}
    print('How was the service?')
    for i in range(1, len(level_dict) + 1):
        print(f"{i}: {level_dict[i][0]} {level_dict[i][1]:.0%}")
    # 1 - Input
    level = int(input('Enter number for value of service: '))
    # 2 3 - Process / Output
    return level_dict[level]


def tip(price, quality): # 0 1 - Initialization / Input
    return price * quality[1] # 2 3 - Process / Output


def sales_tax(price): # 0 1 - Initialization / Input
    return price * SALES_TAX # 2 3 - Process / Output


for c in range(1, 4):
    main(c)
