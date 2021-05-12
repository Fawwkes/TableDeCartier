import numpy as np
import random


def show_board(board):
    for i in range(13, 25, 1):
        print(board[i], end="  ")

    print("    ", end=" ")
    print(board[27], end=" ")
    print(" ", end=" ")
    print(board[29], end=" ")
    print("\n")

    for i in range(12, 0, -1):
        print(board[i], end="  ")

    print("    ", end=" ")
    print(board[26], end=" ")
    print(" ", end=" ")
    print(board[28], end=" ")
    print("\n")


def check_selection(array_position, player):
    if player == 1:
        if board[array_position] < 0 or array_position < 1 or array_position > 24:
            # other player's piece; make them select another piece
            selection_new = int(input("Piece selection unavailable; Player 1 selects a different piece to move:"))
            check_selection(selection_new, 1)

    elif player == 2:
        if board[array_position] > 0 or array_position < 1 or array_position > 24:
            # other player's piece; make them select another piece
            selection_new = int(input("Piece selection unavailable; Player 2 selects a different piece to move:"))
            check_selection(selection_new, 2)


def check_move(player, d1, d2, player_selection, player_move):
    if player == 1:
        if player_selection + d1 != player_move and player_selection + d2 != player_move and player_selection + d2 + d1 != player_move:
            print("(1)Move unavailable; Please select destination again:")
            new_move = int(input("Player 1 selects again where to move the piece:"))
            check_move(1, d1, d2, player_selection, new_move)

        elif board[player_move] < -1:
            print("(2)Move unavailable; Please select destination again:")
            new_move = int(input("Player 1 selects again where to move the piece:"))
            check_move(1, d1, d2, player_selection, new_move)

        else:
            move(1, player_selection, player_move)

    elif player == 2:
        if player_selection - d1 != player_move and player_selection - d2 != player_move and player_selection - d2 - d1 != player_move:
            print("(1)Move unavailable; Please select destination again:")
            new_move = int(input("Player 2 selects again where to move the piece:"))
            check_move(2, d1, d2, player_selection, new_move)

        elif board[player_move] > 1:
            print("(2)Move unavailable; Please select destination again:")
            new_move = int(input("Player 1 selects again where to move the piece:"))
            check_move(2, d1, d2, player_selection, new_move)
        else:
            move(2, player_selection, player_move)


def move(player, player_selection, player_move):
    if player == 1:
        if board[player_move] >= 0:
            board[player_selection] -= 1
            board[player_move] = board[player_move] + 1

        elif board[player_move] == -1:
            take_out(1, player_move)
            board[player_selection] -= 1

        board[30] = board[30] - (player_move - player_selection)

    elif player == 2:
        if board[player_move] <= 0:
            board[player_selection] += 1
            board[player_move] = board[player_move] - 1

        elif board[player_move] == 1:
            take_out(2, player_move)
            board[player_selection] += 1

        board[30] = board[30] - (player_selection - player_move)


def take_out(player, player_move):
    if player == 1:
        board[player_move] = 1
        board[27] -= 1

    elif player == 2:
        board[player_move] = -1
        board[26] += 1


def create_board():
    board = np.zeros((1, 34))
    board = ([0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 3, -3, 0, 0, 0])
    return list(board)


board = create_board()
show_board(board)
game_over = False
turn = 1
double = 0

while not game_over:

    while turn % 2 != 0:
        player: int = 1
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        board[30] = 0
        if dice1 == dice2:
            board[30] = 2 * (dice1 + dice2)
            double += 1
        else:
            board[30] = dice1 + dice2
            double = 0
        print(dice1, dice2, board[30])

        while board[30] > 0:
            while board[26] > 0 and board[30] > 0:
                selection_entry = int(input("Player 1 selects where to enter (1-6):"))
                check_move(1, dice1, dice2, 0, selection_entry)
                board[26] = board[26] - 1
                print(dice1, dice2, board[30])
                show_board(board)

            while board[30] > 0:
                selection1 = int(input("Player 1 selects piece to move:"))
                check_selection(selection1, player)
                move1 = int(input("Player 1 selects where to move the piece:"))
                check_move(1, dice1, dice2, selection1, move1)
                print(dice1, dice2, board[30])
                show_board(board)

            turn += 1

#        if double > 0:
#            turn -= 1

    if board[28] == 15 or board[29] == 15:
        game_over = True
    # ask for player 2 input

    while turn % 2 == 0:
        player: int = 2
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        board[30] = 0
        if dice1 == dice2:
            board[30] = 2 * (dice1 + dice2)
            double += 1
        else:
            board[30] = dice1 + dice2
            double = 0
        print(dice1, dice2, board[30])

        while board[30] > 0:
            while board[27] < 0 and board[30] > 0:
                selection_entry = int(input("Player 2 selects where to enter (19-24):"))
                check_move(2, dice1, dice2, 25, selection_entry)
                board[27] = board[27] + 1
                print(dice1, dice2, board[30])
                show_board(board)

            while board[30] > 0:
                selection2 = int(input("Player 2 selects piece to move:"))
                check_selection(selection1, player)
                move2 = int(input("Player 2 selects where to move the piece:"))
                check_move(2, dice1, dice2, selection1, move1)
                print(dice1, dice2, board[30])
                show_board(board)

            turn += 1

#        if double > 0:
#            turn -= 1

    if board[28] == 15 or board[29] == 15:
        game_over = True
