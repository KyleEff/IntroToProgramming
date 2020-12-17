# Kyle Free
# ITSE 1302
# Number Facts with Loops and Functions
# Advanced Program
'''
Advanced Program: Number Facts
Worth 80 points

Program Summary:  Write a program that allows the user to enter a number between 1 and 1000.  If the number is invalid, provide an error message and allow the user to try again until he enters a valid value.
Once you have a valid number, use it to determine and print the following information:
*Note that in the list of factor pairs, you should not include duplicates.

•	Number squared
•	Number cubed
•	Number Type:  Even composite number
Odd or Even   Prime (Exactly 2 factors) or Composite (More than 2 factors)
•	Whether the number is a perfect square: No  (6 does not have an integer square root like 4 or 9)
•	Square Root:  (Print this line only if the number is perfect square)
•	List of factors that exclude duplicates and are printed horizontally on a single line
Factors: (1, 12) (2, 6) (3, 4)
(4, 3) (6, 2) (12, 1) should not be included

Technical Requirements:
•	Include the program name, student heading and summary in comments at the beginning of your program
•	Include comments throughout your program to explain the logic
•	Use a function for your input logic that includes error checking
o	Use a condition while loop that will cause the loop to execute if the number entered is not valid
o	The loop should provide feedback indicating that the number entered was invalid, and provide the user the opportunity to enter a different one.
•	Use a loop of your choice to determine list of factors
•	Use at least two other user-defined functions
•	When determining the number characteristics, do not use any python mathematical functions like sqrt
•	Match the sample output as closely as possible
'''


def main():
    num = ask_num() # Input
    print(f"\nFacts about the number {num:,.2f}:")
    p_sq, sqrt = square_sqrt(num) # Squared Value and Root
    cube(num) # Cubed Value
    factors(num) # Factors
    print()
    num_type(num) # Number type
    print(f"Perfect Square: ", end='')
    # prints whether num is a perfect square
    if not p_sq:
        print('No\n')
    else: # if num is perfect square, print the square root
        print(f"Yes\nSquare Root: {sqrt}\n")


def ask_num(): # The program's input function
    num = int(input('Enter a positive integer from 1 to 1000: '))
    while num < 1 or num > 1000: # Input validation
        num = int(input('ERROR: Invalid input.\nTry again: '))
    return num


def square_sqrt(num):
    sq_rt = 0
    perfect_sq = False
    sq = num * num # Number squared
    print(f"Squared Value: {sq:,d}")
    # This loop finds the two numbers that,
    #   when multiplied together, equals num
    for i in range(1, num+1):
        if i * i == num:
            # if true, assigns a perfect square bool to num
            #   and assigns square root based on i
            perfect_sq = True
            sq_rt = i
            break
    # Returns bool and int based on perfect square and square root
    return perfect_sq, sq_rt


def cube(num):
    cubed = num * num * num # The number cubed
    print(f"Cubed Value: {cubed:,d}")


def num_type(num):
    prime = False
    print('Type:', end=' ')

    if num % 2 == 0: # if number is even
        print('Even', end=' ')
    else:
        print('Odd', end=' ')

    if num == 1:
        prime = True
    else:
        for i in range(2, num+1):
            # if number divides by range evenly,
            #   the number is not prime
            if num % i == 0:
                prime = False
                print('composite', end=' ')
                # the loop breaks
                break
            # if number divides by range unevenly, the number is prime
            else:
                prime = True

    if prime:
        print('prime', end=' ')

    print('number')


def factors(num):
    factor_list = []
    for i in range(1, num + 1):
        sec_factor = num // i # second factor in the tuple
        if i * sec_factor == num: # if i times the second factor in the tuple equals num
            factor_list.append((i, sec_factor)) # the list is appended with the full tuple
    print('Factors: ', end='')
    # if the length of the list is not even, 1 is added
    #   to the length and then the length is halved so no duplicates are printed
    if len(factor_list) % 2 != 0:
        for t in range((len(factor_list) + 1) // 2):
            print(factor_list[t], end=' ')
    # the same operation is performed but with an even number
    else:
        for n in range(len(factor_list) // 2):
            print(factor_list[n], end=' ')


# runs the main function twice
for c in range(2):
    main()

