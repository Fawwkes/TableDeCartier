import random
import sys

import numpy as np
import pygame

BLUE = (100, 99, 81)
BROWN = (210, 105, 30)
YELLOW = (210, 205, 30)
BLACK = (39, 26, 13)
WHITE = (245, 245, 220)
D_BROWN = (1, 1, 1)
RED = (100, 25, 25)
L_GRAY = (100, 82, 82)
D_GRAY = (66, 66, 100)


# board[0] - buffer
# board[1] -> board[24] - actual board
# board[25] buffer
# board[26], board[27] prison
# board[28], board[29] taken out pieces
# board[30] - sum of dices
# board[31], board[32] - dices
# board[33] - piece selected
# board[35] - error signal


def show_board(board):
    for i in range(24, 12, -1):
        print(board[i], end="  ")

    print("    ", end=" ")
    print(board[27], end=" ")
    print(" ", end=" ")
    print(board[29], end=" ")
    print("\n")

    for i in range(1, 13, 1):
        print(board[i], end="  ")

    print("    ", end=" ")
    print(board[26], end=" ")
    print(" ", end=" ")
    print(board[28], end=" ")
    print("\n")


def click_select(x, y):
    global positionx
    positionx = 36
    if y > 300:
        if x < 325:
            positionx = (x - 25) / 50 + 1

        if x > 375:
            positionx = (x - 75) / 50 + 1

        # else:
        #     positionx = 38

    elif y < 300:
        if x < 325:
            if 25 < x < 75:
                positionx = 24

            if 75 < x < 125:
                positionx = 23

            if 125 < x < 175:
                positionx = 22

            if 175 < x < 225:
                positionx = 21

            if 225 < x < 275:
                positionx = 20

            if 275 < x < 325:
                positionx = 19

        if x > 375:
            if 375 < x < 425:
                positionx = 18
            if 425 < x < 475:
                positionx = 17
            if 475 < x < 525:
                positionx = 16
            if 525 < x < 575:
                positionx = 15
            if 575 < x < 625:
                positionx = 14
            if 625 < x < 675:
                positionx = 13
            # else:
            #     positionx = 38
    # else:
    #     positionx = 38
    return positionx


def check_selection(array_position, player):
    if player == 1:
        if array_position is None or board[array_position] is None or board[
            array_position] < 0 or array_position < 1 or array_position > 24:
            # other player's piece; make them select another piece
            print("Piece selection unavailable; Player 1 selects a different piece to move:")
            board[33] = 0

        else:
            board[33] = array_position

    elif player == 2:
        if array_position is None or board[array_position] is None or board[
            array_position] > 0 or array_position < 1 or array_position > 24:
            # other player's piece; make them select another piece
            print("Piece selection unavailable; Player 2 selects a different piece to move:")
            board[33] = 0
        else:
            board[33] = array_position


def check_move(player, d1, d2, player_selection, player_move):
    if reverse % 2 == 0:
        if player == 1:
            if player_selection + d1 != player_move and player_selection + d2 != player_move:
                print("(1)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 1 selects again where to move the piece:"))
                # check_move(1, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0

            elif board[player_move] < -1:
                print("(2)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 1 selects again where to move the piece:"))
                # check_move(1, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0

            else:
                move(1, player_selection, player_move)
                board[35] = 0

        elif player == 2:
            if player_selection - d1 != player_move and player_selection - d2 != player_move:
                print("(1)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 2 selects again where to move the piece:"))
                # check_move(2, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0

            elif board[player_move] > 1:
                print("(2)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 1 selects again where to move the piece:"))
                # check_move(2, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0
            else:
                move(2, player_selection, player_move)
                board[35] = 0
    else:
        if player == 1:
            if player_selection - d1 != player_move and player_selection - d2 != player_move:
                print("(1)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 2 selects again where to move the piece:"))
                # check_move(2, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0

            elif board[player_move] < -1:
                print("(2)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 1 selects again where to move the piece:"))
                # check_move(2, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0
            else:
                move(1, player_selection, player_move)
                board[35] = 0

        elif player == 2:
            if player_selection + d1 != player_move and player_selection + d2 != player_move:
                print("(1)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 1 selects again where to move the piece:"))
                # check_move(1, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0

            elif board[player_move] > 1:
                print("(2)Move unavailable; Please select destination again:")
                # new_move = int(input("Player 1 selects again where to move the piece:"))
                # check_move(1, d1, d2, player_selection, new_move)
                board[35] = 1
                board[33] = 0
            else:
                move(2, player_selection, player_move)
                board[35] = 0


def move(player, player_selection, player_move):
    if reverse % 2 == 0:
        if player == 1:
            if board[player_move] >= 0:
                board[player_selection] -= 1
                board[player_move] = board[player_move] + 1

            elif board[player_move] == -1:
                take_out(1, player_move)
                board[player_selection] -= 1

            if board[31] == board[30] - (player_move - player_selection):
                board[32] = 0
            elif board[32] == board[30] - (player_move - player_selection):
                board[31] = 0
            board[30] = board[30] - (player_move - player_selection)
            board[33] = 0

        elif player == 2:
            if board[player_move] <= 0:
                board[player_selection] += 1
                board[player_move] = board[player_move] - 1

            elif board[player_move] == 1:
                take_out(2, player_move)
                board[player_selection] += 1

            if board[31] == board[30] - (player_selection - player_move):
                board[32] = 0
            elif board[32] == board[30] - (player_selection - player_move):
                board[31] = 0
            board[30] = board[30] - (player_selection - player_move)
            board[33] = 0
    else:
        if player == 1:
            if board[player_move] >= 0:
                board[player_selection] -= 1
                board[player_move] = board[player_move] + 1

            elif board[player_move] == -1:
                take_out(1, player_move)
                board[player_selection] -= 1

            if board[31] == board[30] - (player_selection - player_move):
                board[32] = 0
            elif board[32] == board[30] - (player_selection - player_move):
                board[31] = 0
            board[30] = board[30] - (player_selection - player_move)
            board[33] = 0

        elif player == 2:
            if board[player_move] <= 0:
                board[player_selection] += 1
                board[player_move] = board[player_move] - 1

            elif board[player_move] == 1:
                take_out(2, player_move)
                board[player_selection] += 1

            if board[31] == board[30] - (player_move - player_selection):
                board[32] = 0
            elif board[32] == board[30] - (player_move - player_selection):
                board[31] = 0
            board[30] = board[30] - (player_move - player_selection)
            board[33] = 0


def take_out(player, player_move):
    if player == 1:
        board[player_move] = 1
        board[27] -= 1

    elif player == 2:
        board[player_move] = -1
        board[26] += 1


def remove_pieces (player, value):
    if reverse % 2 == 0:
        if player == 1:
            pieces = 0
            for i in range(19, 25, 1):
                if board[i] > 0:
                    pieces = pieces + board[i]
            if pieces + board[28] == 15:

        if player == 2:
            pieces = 0
            for i in range (1, 7, 1):
                if board[i] < 0:
                    pieces = pieces + board[i]
            if pieces + board[29] == -15:

    else:
        if player == 1:
            pieces = 0
            for i in range(1, 7, 1):
                if board[i] > 0:
                    pieces = pieces + board[i]
            if pieces + board[28] == 15:

        if player == 2:
            pieces = 0
            for i in range(19, 25, 1):
                if board[i] < 0:
                    pieces = pieces + board[i]
            if pieces + board[29] == -15:


def draw_circles(board1):
    for i in range(1, 7, 1):
        if board[i] > 0:
            pieces = board[i]
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, WHITE, [i * 50, 600 - j * 50], 25)
        if board[i] < 0:
            pieces = abs(board[i])
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, D_BROWN, [i * 50, 600 - j * 50], 25)
        if i == board[33] and board[board[33]] > 0:
            pygame.draw.circle(screen, L_GRAY, [i * 50, 600 - board[board[33]] * 50], 25)
        if i == board[33] and board[board[33]] < 0:
            pygame.draw.circle(screen, D_GRAY, [i * 50, 600 - abs(board[board[33]]) * 50], 25)
    for i in range(7, 13, 1):
        if board[i] > 0:
            pieces = board[i]
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, WHITE, [i * 50 + 50, 600 - j * 50], 25)
        if board[i] < 0:
            pieces = abs(board[i])
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, D_BROWN, [i * 50 + 50, 600 - j * 50], 25)
        if i == board[33] and board[board[33]] > 0:
            pygame.draw.circle(screen, L_GRAY, [i * 50 + 50, 600 - board[board[33]] * 50], 25)
        if i == board[33] and board[board[33]] < 0:
            pygame.draw.circle(screen, D_GRAY, [i * 50 + 50, 600 - abs(board[board[33]]) * 50], 25)
    for i in range(13, 19, 1):
        if board[i] > 0:
            pieces = board[i]
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, WHITE, [int(((i - 19 + 2 * abs(i - 19)) * 50)) + 350, 50 * j], 25)
        if board[i] < 0:
            pieces = abs(board[i])
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, D_BROWN, [int(((i - 19 + 2 * abs(i - 19)) * 50)) + 350, 50 * j], 25)
        if i == board[33] and board[board[33]] > 0:
            pygame.draw.circle(screen, L_GRAY, [int(((i - 19 + 2 * abs(i - 19)) * 50)) + 350, 50 * board[board[33]]],
                               25)
        if i == board[33] and board[board[33]] < 0:
            pygame.draw.circle(screen, D_GRAY,
                               [int(((i - 19 + 2 * abs(i - 19)) * 50)) + 350, 50 * abs(board[board[33]])], 25)
    for i in range(19, 25, 1):
        if board[i] > 0:
            pieces = board[i]
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, WHITE, [int(((i - 25 + 2 * abs(i - 25)) * 50)), 50 * j], 25)
        if board[i] < 0:
            pieces = abs(board[i])
            for j in range(1, pieces + 1, 1):
                pygame.draw.circle(screen, D_BROWN, [int(((i - 25 + 2 * abs(i - 25)) * 50)), 50 * j], 25)
        if i == board[33] and board[board[33]] > 0:
            pygame.draw.circle(screen, L_GRAY, [int(((i - 25 + 2 * abs(i - 25)) * 50)), 50 * board[board[33]]],
                               25)
        if i == board[33] and board[board[33]] < 0:
            pygame.draw.circle(screen, D_GRAY, [int(((i - 25 + 2 * abs(i - 25)) * 50)), 50 * abs(board[board[33]])],
                               25)

    if board[26] > 0:
        pygame.draw.circle(screen, WHITE, [350, 350], 25)
        label = myfont.render(str(board[26]), 1, D_BROWN)
        screen.blit(label, (342, 338))
    if board[27] < 0:
        pygame.draw.circle(screen, D_BROWN, [350, 250], 25)
        label = myfont.render(str(abs(board[27])), 1, WHITE)
        screen.blit(label, (342, 230))


def draw_board(board1):
    pygame.draw.rect(screen, BLACK, (0, 0, width, height))
    pygame.draw.rect(screen, BLUE, (25, 25, 300, 550))
    pygame.draw.rect(screen, BLUE, (375, 25, 300, 550))
    for i in range(0, 5, 2):
        pygame.draw.polygon(screen, YELLOW, [(i * 50 + 25, 25), (i * 50 + 75, 25), (i * 50 + 50, 250)])
    for i in range(1, 7, 2):
        pygame.draw.polygon(screen, BROWN, [(i * 50 + 25, 25), (i * 50 + 75, 25), (i * 50 + 50, 250)])
    for i in range(0, 5, 2):
        pygame.draw.polygon(screen, YELLOW, [(i * 50 + 375, 25), (i * 50 + 425, 25), (i * 50 + 400, 250)])
    for i in range(1, 7, 2):
        pygame.draw.polygon(screen, BROWN, [(i * 50 + 375, 25), (i * 50 + 425, 25), (i * 50 + 400, 250)])
    for i in range(0, 5, 2):
        pygame.draw.polygon(screen, BROWN, [(i * 50 + 25, 575), (i * 50 + 75, 575), (i * 50 + 50, 350)])
    for i in range(1, 7, 2):
        pygame.draw.polygon(screen, YELLOW, [(i * 50 + 25, 575), (i * 50 + 75, 575), (i * 50 + 50, 350)])
    for i in range(0, 5, 2):
        pygame.draw.polygon(screen, BROWN, [(i * 50 + 375, 575), (i * 50 + 425, 575), (i * 50 + 400, 350)])
    for i in range(1, 7, 2):
        pygame.draw.polygon(screen, YELLOW, [(i * 50 + 375, 575), (i * 50 + 425, 575), (i * 50 + 400, 350)])
    draw_circles(board)
    label = myfont2.render(str(board[31]) + "," + str(board[32]), 1, WHITE)
    screen.blit(label, (325, 400))
    label = myfont2.render(str(board[30]), 1, WHITE)
    screen.blit(label, (345, 440))
    if turn % 2 != 0:
        label = myfont2.render("Player 1's turn", 1, WHITE)
        screen.blit(label, (238, 0))
    else:
        label = myfont2.render("Player 2's turn", 1, WHITE)
        screen.blit(label, (238, 0))
    pygame.display.update()


def create_board():
    board = np.zeros((1, 40))
    board = (
        [0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 3, -3, 0, 0, 0, 0, 0,
         0,
         0, 0, 0, 0])
    return list(board)


board = create_board()
show_board(board)
game_over = False
turn = 1
double = 0
reverse = 0

pygame.init()
myfont = pygame.font.SysFont("monospace", 30)
myfont2 = pygame.font.SysFont("monospace", 25)
SQUARESIZE = 100

width = 700
height = 600

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            sys.exit()
            pygame.display.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            if board[30] == 0:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                board[30] = 0
                if dice1 == dice2:
                    board[30] = 2 * (dice1 + dice2)
                    double += 1
                    if double % 2 == 0 and double != 0:
                        reverse += 1
                else:
                    board[30] = dice1 + dice2
                    double = 0
                board[31] = dice1
                board[32] = dice2
                print(board[31], board[32], board[30], double, reverse)
                draw_board(board)
                show_board(board)

            elif turn % 2 == 0:
                player: int = 2
                if board[27] < 0:
                    selection_entry = int(click_select(posx, posy))
                    print(selection_entry)
                    if reverse % 2 == 0:
                        check_move(2, board[31], board[32], 25, selection_entry)
                    else:
                        check_move(2, board[31], board[32], 0, selection_entry)
                    if board[35] == 0:
                        board[27] = board[27] + 1

                    print(board[31], board[32], board[30], double, reverse)
                    draw_board(board)
                    show_board(board)
                    if board[30] < 1:
                        turn = turn + 1
                        board[30] = 0
                        if double > 0:
                            turn = turn + 1

                elif board[33] == 0:
                    # selection
                    selection1 = int(click_select(posx, posy))
                    check_selection(selection1, player)
                    board[33] = selection1

                # elif board[33] != 0 and board[35] == 1:
                #     # selection
                #     selection1 = int(click_select(posx, posy))
                #     check_selection(selection1, player)
                #     board[33] = selection1

                elif board[33] != 0:
                    # move
                    move1 = int(click_select(posx, posy))
                    check_move(2, board[31], board[32], selection1, move1)
                    print(board[31], board[32], board[30], double, reverse)
                    draw_board(board)
                    show_board(board)
                    board[33] = 0
                    if board[30] < 1:
                        turn = turn + 1
                        board[30] = 0
                        if double > 0:
                            turn = turn + 1

            elif turn % 2 != 0:
                player: int = 1
                if board[26] > 0:
                    selection_entry = int(click_select(posx, posy))
                    print(selection_entry)
                    if reverse % 2 == 0:
                        check_move(1, board[31], board[32], 0, selection_entry)
                    else:
                        check_move(1, board[31], board[32], 25, selection_entry)
                    if board[35] == 0:
                        board[26] = board[26] - 1

                    print(board[31], board[32], board[30], double, reverse)
                    draw_board(board)
                    show_board(board)
                    if board[30] < 1:
                        turn = turn + 1
                        board[30] = 0
                        if double > 0:
                            turn = turn + 1
                        print(turn)

                elif board[33] == 0:
                    # selection
                    selection1 = int(click_select(posx, posy))
                    check_selection(selection1, player)

                elif board[33] != 0:
                    # move
                    move1 = int(click_select(posx, posy))
                    check_move(1, board[31], board[32], selection1, move1)
                    print(board[31], board[32], board[30], double, reverse)
                    draw_board(board)
                    show_board(board)
                    if board[30] < 1:
                        turn = turn + 1
                        board[30] = 0
                        if double > 0:
                            turn = turn + 1
                        print(turn)

                # elif board[35] != 0:
                #     #move
                #     move1 = int(click_select(posx, posy))
                #     check_move(1, dice1, dice2, selection1, move1)
                #     print(dice1, dice2, board[30])
                #     draw_board(board)
                #     show_board(board)
                #     if board[30] < 1:
                #         turn = turn + 1
                #         print(turn)

                if board[28] == 15 or board[29] == 15:
                    game_over = True

        if event.type == pygame.MOUSEMOTION:
            draw_board(board)
            posx = event.pos[0]
            posy = event.pos[1]
            if board[33] == 0 and board[30] != 0 and turn % 2 != 0 and board[26] > 0:
                pygame.draw.circle(screen, WHITE, [posx, posy], 25)
            elif board[33] != 0 and board[30] != 0 and turn % 2 != 0 and board[26] == 0:
                pygame.draw.circle(screen, WHITE, [posx, posy], 25)
            elif board[33] == 0 and board[30] != 0 and turn % 2 == 0 and board[27] < 0:
                pygame.draw.circle(screen, D_BROWN, [posx, posy], 25)
            elif board[33] != 0 and board[30] != 0 and turn % 2 == 0 and board[27] == 0:
                pygame.draw.circle(screen, D_BROWN, [posx, posy], 25)
            pygame.display.update()

    if board[28] == 15 or board[29] == 15:
        game_over = True
