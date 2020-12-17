import random
# Step 0:  Initialization
# Short Candy Land
START = int(0)
FINISH = int(18)

print("Enter the name of each person in the order they will play.")
player1Name = input("Enter name of player 1: ")
player2Name = input("Enter name of player 2: ")


def main(player_one, player_two):
    displayInstructions()
    playGame = True
    while playGame:
        # Step 1: Initialize and Input
        # Get player information and place their game piece on START
#        player1Name = input("Enter name of player 1: ")
#        player2Name = input("Enter name of player 2: ")

        p1Position = int(START)
        p2Position = int(START)
        turn = int(0)

        # Step 2: Process
        # Game play continues until one player reaches FINISH space

        while p1Position < FINISH and p2Position < FINISH:
            turn += 1
            print("\n\nStart Turn", turn)
            p1Position = getNextLocation(p1Position, player_one)
            if p1Position < FINISH:
                p2Position = getNextLocation(p2Position, player_two)
            # input("Press ENTER to continue\n")

        # Step 3: Final Output
        endOfGame(player_one, p1Position, player_two, p2Position)
        playGame = bool(input("Would you like to play? Enter Y or N ").upper() == "Y")


def displayInstructions():
    # Instructions
    print("\n\n\t\t\t*** HOW TO PLAY ***")
    print("Each player token is placed on the START space")
    print("On each player's turn, they will roll a die.")
    print("The player will advance toward FINISH based on the number rolled")
    print("To win the game, the player will have to land on the FINISH space")

    input("\n\nPress ENTER to start the game")


def endOfGame(player1Name, p1Position, player2Name, p2Position):
    # End of game process: declare winner
    print("\n\nGame is over!")
    if p1Position == FINISH:  # player 1 won
        print(player1Name, "wins!")
        print("\nThe final results are:")
        print(player1Name, "reached Finish and wins the game!")
        print(player2Name, "is on space", p2Position)
    else:  # player 2 won
        print(player2Name, "wins!")
        print(player2Name, "reached Finish and wins the game!")
        print(player1Name, "is on space", p1Position)


def getNextLocation(currentPosition, playerName):
    # player rolls dice
    # input("  Press ENTER for " + playerName + " to roll dice")
    roll = random.randint(1, 6)

    # Player moves
    newPosition = currentPosition + roll
    newPosition = exact_roll(newPosition, playerName, roll)
    newPosition = secret_squares(newPosition, playerName)

    return newPosition


def exact_roll(player_pos, player_name, roll):
    # creates a condition where if the player rolls higher
    #   than the amount needed to land on the final square,
    #   then the player is knocked back a square
    if player_pos > FINISH:
        player_pos -= roll
        player_pos -= 1
        print(f"\t{player_name} rolls {roll}, which is more than needed to win.\n"
              f"{player_name} is moved back 1 space to square {player_pos}.\n")
    else:
        print("\t", player_name, "rolls", roll, "and moves to", player_pos)
    return player_pos


def secret_squares(player_pos, player_name):
    # first square boost
    if player_pos == 1:
        player_pos += 2
        print(f"{player_name} rolled a 1, and landed on a boost square!\n"
              f"{player_name} is boosted forward 2 spaces to square {player_pos}!\n")
    # if the player lands on square 16,
    #   the player is knocked back 3 spaces
    if player_pos == 17:
        player_pos -= 3
        print(f"{player_name} has landed on a secret square!\n"
              f"{player_name} is knocked back 3 spaces to square {player_pos}.\n")

    # if player lands on square 16,
    #   the player moves forward 2 spaces,
    #   winning the game
    if player_pos == 16:
        player_pos += 2
        print(f"{player_name} has landed on a secret square!\n"
              f"{player_name} is pushed forward 2 spaces to square {player_pos}!\n")
    return player_pos


main(player1Name, player2Name)

