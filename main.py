import numpy as np
import random

def create_board():
    board = np.zeros((1,30))
    board = ([0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 3, -3, 0, 0])
    return board

board = create_board()
game_over = False
turn = 0



while not game_over:
    #ask for player 1 input
    if turn % 2 == 0:

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(dice1 , dice2)
        selection = input("Player 1 selects piece to move:")


        turn += 1

    #ask for player 2 input

    if turn % 2 != 0:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(dice1 , dice2)
        selection = input("Player 2 selects piece to move:")


        turn += 1