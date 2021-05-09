"""
TODO: Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.
The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players.
2. The two players alternate turns.
3. On a given turn, a player may take either 1 or 2 stone from the center pile.
4. The two players continue until the center pile has run out of stones.
"""

import random

def main():
    stones = 20
    player_turn = 1 # 1 for Player 1, 2 for Player 2
    print("There are " + str(stones) + " stones left")
    while stones > 0:
        amount = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))
        # amount = int(input(""))
        # print("")
        while amount != 1 and amount != 2:
            amount = int(input("Please enter 1 or 2: "))
        stones -= amount

        if player_turn == 1:
            player_turn += 1
        else:
            player_turn -= 1
        print("")
        if stones != 0:
            print("There are " + str(stones) + " stones left")
        
    if player_turn == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    # print("Game over")


if __name__ == '__main__':
    main()
