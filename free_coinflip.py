# Kyle Free
# ITSE 1302
# Coin Flip Minor Program
# Overview: Create a coin flip game that allows the user to guess whether the coin will
#   be heads or tails.  Save the data associated with the flip.  Repeat for a total of
#   10 guesses/flips.  Display result summary and details at end.

# Technical Requirements:
# •	Participant will guess whether a coin flip will result in Heads or Tails
# •	Computer will "flip" a coin to determine the side it lands using random generator
# o	import random at top of program
# o	result = random.randint(x, x)
# •	The program will display the results:  Guess, Flip, Outcome (Match or No Match)
# •	The program will track the results and, when the game is over, display:
# o	Summary
# o	Detailed result of each turn
# •	Use parallel arrays to collect details from each turn that can be displayed as a table when the game is over
# •	Use running totals of each result detail to display at end


# I have been looking into how arrays are used compared to lists.
#   I will keep in mind that appending is not a function applicable to arrays.
# The program does not require one, but I tried coding an error catcher,
#   it gets stuck in an infinite loop for some unknown reason.
#   Code was left in as comments


import random
guesses = []
flips = []
matches = []


def main():
    # 0 - Initialization
    overview()
    # 12 - Input / Process
    for m in range(10):
        flip_coin(guess())
    # 3 - Output
    summary()
    tally()
    log()


def overview():
    # displays overview of the program / game
    print('Participant will guess whether a ' +
          'coin flip will result in Heads or Tails.\n'
          'Computer will "flip" a coin to determine ' +
          'the side it lands on using a random number generator.\n'
          'The program will display the results of flips, ' +
          'and whether the user guessed the flip correctly.\n'
          'The program will track the results, and when the game ' +
          'is over it will display a summary and detailed results of each turn.')


def guess():
    # ask the player for a guess
    print('\nGuess the coin flip!\nEnter H for heads and T for tails!')
    plyr_guess = input().upper()

    #plyr_guess = 'H'
    #plyr_guess = 'T'
# input validation gets stuck in an infinite loop for some reason
    #while plyr_guess != 'H' or 'T':
    #    print('ERROR: Invalid input.\nEnter H for heads and T for tails!\n')
    #    plyr_guess = input().upper()

    guesses.append(plyr_guess)
    return plyr_guess


def flip_coin(player_guess):
    coin_flip = random.randint(0, 1)

    # assigning H or T to the 0/1 coin flip
    # appens flips list
    if coin_flip == 0:
        flips.append('H')
    else:
        flips.append('T')

    # assigning 0 or 1 to the H/T player guess
    if player_guess == 'H':
        player_guess = 0
    else:
        player_guess = 1

    # compares the guess versus the flip, using 0 or 1
    #   and displaying the results
    if player_guess == coin_flip:
        print('Good guess!')
    else:
        print('Too bad...Maybe next time!')


def summary():
    # checks the list for heads or tails,
    #   adds to counters, displays results
    heads = 0
    tails = 0

    print(f"\nSUMMARY\nCategory    Heads    Tails")

    for g in guesses:
        if g == 'H':
            heads += 1
        else:
            tails += 1
    print(f"Guess\t    {heads:^5}    {tails:^4}")

    heads = 0
    tails = 0
    for f in flips:
        if f == 'H':
            heads += 1
        else:
            tails += 1
    print(f"Coin Flip   {heads:^5}    {tails:^4}")


def tally():
    # tallys matches in the guesses and flips lists,
    #   appends a list and displays results
    correct = 0
    wrong = 0

    for i in range(len(guesses)):
        if guesses[i] == flips[i]:
            correct += 1
            matches.append('Y')
        else:
            wrong += 1
            matches.append('N')

    print(f"\nTIMES WON:  {correct}\nTIMES LOST: {wrong}")


def log():
    # the total log of the program
    print(f"\nLOG\nTurn   Guess   Flip   Match")

    for n in range(len(guesses)):
        print(f"{n+1:^5} {guesses[n]:^7} {flips[n]:^6} {matches[n]:^7}")


main()

