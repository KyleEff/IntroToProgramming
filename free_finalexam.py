# Kyle Free
# ITSE 1302
# Final Exam Advanced Program
# Requirements:
# This program is based on a dice game.  It is played with 3 dice and each player has 3 tokens …
#   typically quarters or dollars. The minimum number of players required to play  is 3.
#   You should program it to accept 3 – 6 players.
# The roll:  You may only roll as many dice as you have tokens, up to a maximum of 3 dice.
#   If you have 3 or more tokens, you must roll 3 dice. If you have 2 tokens, you must roll 2 dice.
#   If you have 1 token, you must roll one die.  If you have no tokens, you are skipped for that turn,
#   but you are still in the game because some one may give one of their tokens to you  on their roll.
# The play:  Player rolls as many dice as they are entitled to.
# •	For each 1 that is rolled, (L) the player gives one of their tokens to the player to their left.
# •	For each 3 that is rolled, (R) the player gives one of their tokens to the player to their right
# •	For each 5 that is rolled, (C) the player gives one of their tokens to the center of the table
# •	For each even number that is rolled, (DOT) the player gets to keep a token
# Play continues around the table with each person rolling the number of dice they are entitled to roll.
# During the play tokens frequently change hands  and occasionally end up in the center resulting in there
#   being fewer and fewer tokens in the hands of the players.
# End of Game:  When only one player is left with at least 1 token, and no other players have any tokens,
#   the player with the token wins all of the tokens in the center.
#
# Your game must mimic this one with the exception that the rolls will be handled using the random library.
# It should accommodate from 3 to 6 people and the output should contain all information shown in the sample
#   output at the bottom of this file.  (The numbers and winners will not be the same, but the information
#   displayed on each player's turn should be based on the sample output.)
#
# Technical Requirements and Associated Grading:  Total of 300 points
# •	40 points: Include a design diagram that:
# o	Has enough information in it that I can predict what your code structure will be
# o	Is NOT a copy of your code pasted into a chart
# •	80 points: You must use parallel arrays to hold the following information and to control the play of the game:
# o	20 points: Player Names
# o	20 points: Player Tokens
# o	20 points: The Player to the current player's Left
# o	20 points: The Player to the current player's Right
# •	50 points: Do not use any list functions, simply access the array values using subscripts
# •	20 points: You must use Random and random.randint to generate the dice values each turn.
# •	10 points: You must use loops and decision statements to play through the game;
# •	20 points: You must use at least 2 functions besides main
# •	30 points: Appropriate comments
# •	50 points: Runs correctly with no errors or bugs
# •	Unless you have spoken to me ahead of time, I want you to follow standard coding practices,
#       not the super-duper python practices.  For those of you that have been using the book
#       instead of my lectures, I will allow you some leeway, but you must discuss it with me
#       by Friday, Dec. 4nd by the latest.
#
# Stuff you need to know:
# •	After Friday, Dec. 4, at 5:30, you can turn your file containing your design, code, and
#       output screens into the regular Final Programming Exam drop box.  I'm pretty sure it
#       will be obvious when I look at your code which direction you decided to take. 😊
# •	You have until Saturday, Dec 5 to let me know if you plan to take the advanced program exam.
#       That should give you enough time to play with the program and have a good idea of whether
#       you want to try it.
# •	My guess is that it will take you 10 – 40 hours to complete based on how much prior
#       programming experience you have.
# •	If after you give it a try, you decide to take the programming exam that the rest of
#       the class is taking along with the final exam quiz … you may take the regular
#       programming exam by Sunday, 11:30 PM to avoid a late penalty.
# •	I suggest you play the game a few times "for real" before trying to program it.
# •	Then I suggest you play the game and follow the movement of the tokens using "arrays" on paper.

import random

print('Welcome to the game!\nThe game requires 3 to 6 people to play.')

try:
    numPlayers = int(input('How many people will be playing?\n'))
except ValueError:
    print('ERROR: Enter a whole integer number.')
    numPlayers = int(input('How many people will be playing?\n'))

playerData = [[str('')] * numPlayers, [int(3)] * numPlayers]
playerRolls = [[int(0)]] * numPlayers
playerPos = [str('')] * 3

player = playerPos[1]
lastPlayer = numPlayers - 1

center = int(0)


def main():
    rnd = int(1)

    error_catch()
    player_pop()

    # This statement runs on the condition that there is
    #   more than 1 person who has tokens
    while playerData[1].count(0) != lastPlayer:
        print('Starting Round', rnd) # Prints current round
        rnd += 1
        results() # prints starting tokens

        # Each iteration of this loop is for one player's turn
        for turn in range(numPlayers):
            tokens = playerData[1][turn]
            if playerData[1].count(0) == lastPlayer:
                break
            elif tokens != 0:
                roll_dice(turn)
                player_positions(turn)
                play(turn)
                display(turn)

    winner()


def error_catch():
    '''Detects whether the number of players is
        less than 3 or less than 6'''
    global numPlayers
    while numPlayers < 3 or numPlayers > 6:
        if numPlayers < 3:
            print('\nERROR: The number of players that you have entered is less than 3.')
        else:
            print('\nERROR: The number of players that you have entered is more than 6.')
        numPlayers = int(input('How many people will be playing? '))


def player_pop():
    '''Populates an array with player names'''
    for name in range(numPlayers):
        playerData[0][name] = str(input(f"Enter player {name+1}'s name: "))
    print()


def roll_dice(turn):
    '''Rolls the dice for all players, for the entire round, based on
        the number of tokens in possession, and then
        updates the playerData arrays accordingly will the rolls'''
    # "tokens" is being read as a string variable due to the first array
    #   consisting of strings, but is executed as an integer

    tokens = playerData[1][turn]
    if tokens >= 3:
        playerRolls[turn] = [0] * 3
        for roll in range(3):
            playerRolls[turn][roll] = random.randint(1, 6)
    else:
        playerRolls[turn] = [0] * tokens
        for roll in range(tokens):
            playerRolls[turn][roll] = random.randint(1, 6)


def player_positions(p):
    '''Reads which player is currently up, and which players are
        to the left and right of the current player'''
    global player

    player = playerData[0][p]

    if p == 0:
        player_left = playerData[0][-1]
        player_right = playerData[0][p+1]
    elif p == lastPlayer:
        player_left = playerData[0][p-1]
        player_right = playerData[0][0]
    else:
        player_left = playerData[0][p-1]
        player_right = playerData[0][p+1]

    positions = [player_left, player, player_right]

    for pos in range(3):
        playerPos[pos] = positions[pos]


def play(p):
    '''This function runs through the rolls of the round,
        and moves the tokens accordingly, then displays
        the results of the round'''
    global center

    # This loop iterates through the roll of each dice,
    #   and moves the tokens according to which player
    #   is being iterated
    for roll in playerRolls[p]:

        if roll == 1: # token goes to the left player
            playerData[1][p] -= 1 # Current player loses token

            if p == 0: # if first player is up
                playerData[1][-1] += 1 # the last player gets token
            else:
                playerData[1][p-1] += 1 # the left player gets token

        elif roll == 3: # token goes to right player
            playerData[1][p] -= 1 # Current player loses token

            if p == lastPlayer: # if last player is up
                playerData[1][0] += 1 # first player gets token
            else:
                playerData[1][p+1] += 1 # right player gets token

        elif roll == 5: # token to center
            playerData[1][p] -= 1
            center += 1


def display(turn):
    '''Displays the player rolls'''
    global player
    #print(playerRolls[rnd]) # Prints rolls to compare with symbols

    print(f"{player} rolls:", end=' ')
    # This loop iterates through a player's rolls,
    #   then prints a symbol based on the roll
    for roll in playerRolls[turn]:
        if roll == 1:
            print('L', end=' ')
        elif roll == 3:
            print('R', end=' ')
        elif roll == 5:
            print('C', end=' ')
        else:
            print('DOT', end=' ')

    results()


def results():
    '''Prints the tokens in each player's possession,
        and the tokens in the center of the table'''

    print('\nResults:', end='\n')

    # This loop iterates through each player's name,
    #   their tokens, and prints them both
    for tok in range(numPlayers):
        print(f"{playerData[0][tok]+':':10} {playerData[1][tok]} tokens")

    print(f"Center of the table: {center}\n")


def winner():
    '''Iterates through all the players' tokens and displays the winner'''
    print("THE GAME IS OVER!")

    for w in range(numPlayers):
        if playerData[1][w] != 0:
            print(f"{playerData[0][w]} has {playerData[1][w]} tokens while all the other players have none.\n"
                  f"{playerData[0][w]} wins all of the {center} tokens in the center of the table!\n")


main()
