# Kyle Free
# ITSE 1302
# Keyboard Characters Program
# Complex Extension
# Requirements:
# • Program will accept a single character of input from the user.
#       Using a decision structure, determine if the character is a letter, a digit, or a symbol.
#       Print the character entered along with the category
#       (upper case consonant, lower case consonant, upper case vowel, lower case vowel, digit, symbol)
# •	Display the value of each of the variables with appropriate labels

# 0 - Initialization
DONE = False # type "exit" to terminate program
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
while not DONE:
    letter = False
    symbol = False
    digit = False
    vowOrCon = ''
    category = ''
    case = ''
# 1 - Input
    char = input('Enter a character (letter, digit, or symbol): ')
# 2 - Process
# learned new syntax that compares a range of values
    if '0' <= char <= '9':
        digit = True
        category = 'digit'
    elif ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
        letter = True
        if 'A' <= char <= 'Z':
            case = 'upper-case'
        else:
            case = 'lower-case'
        if char.lower() in vowels:
            vowOrCon = 'vowel'
        else:
            vowOrCon = 'consonant'
    else:
        symbol = True
        category = 'symbol'
# 3 - Output
    if char.lower() == 'exit':
        DONE = True
        print('Program terminated.')
    elif letter:
        print(f"User entered the {case} {vowOrCon}: {char}\n")
    elif digit or symbol:
        print(f"User entered the {category}: {char}\n")

# not sure if the next statement can be shortened
#    elif ((' ' <= char <= '/') or (':' <= char <= '@')) or (('[' <= char <= '`') or ('{' <= char <= '~')):
#        symbol = True
#        category = 'symbol'