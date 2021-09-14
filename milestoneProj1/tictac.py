import random
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board(board):
    print(board[0: 3])
    print(board[3: 6])
    print(board[6:])


def player_input():

    correctInput = False
    playerTwoMarker = ''

    while correctInput == False:
        playerOneMarker = input("Please type in and select 'x' or 'o' \n")
        if playerOneMarker == 'x' or playerOneMarker == 'o':
            if playerOneMarker == 'x':
                playerTwoMarker = 'o'
            else:
                playerTwoMarker = 'x'
            print(f'player One is has selected "{playerOneMarker}"')
            print(f'player Two is will now use "{playerTwoMarker}"')
            correctInput = True
        else:
            print("you have not selected your market yet")
    return (playerOneMarker, playerTwoMarker)


def place_marker(board, marker, position):
    board[position-1] = marker
    print('\n' * 100)
    display_board(board)
    # check right after placing marker
    if win_check(board, marker):
        if(playerOneMarker == marker):
            print('player one wins!')
        elif(playerTwoMarker == marker):
            print('player two wins!')


def win_check(board, marker):
    if board[0] == board[1] == board[2] == marker:
        return True
    elif board[3] == board[4] == board[5] == marker:
        return True
    elif board[6] == board[7] == board[8] == marker:
        return True
    elif board[0] == board[3] == board[6] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[0] == board[4] == board[8] == marker:
        return True
    elif board[2] == board[4] == board[6] == marker:
        return True
    else:
        return False


def choose_first():
    randomNum = random.randrange(1, 3)
    if randomNum == 1:
        return 'playerOne'
    else:
        return 'playerTwo'


def space_check(board, position):
    if board[position-1] != playerOneMarker and board[position-1] != playerTwoMarker:
        return True
    else:
        return False


def full_board_check(board):
    for space in board:
        if space != playerOneMarker or space != playerTwoMarker:
            return False
    return True


def player_choice(board):
    spaceStatus = False
    while spaceStatus == False:
        playerChoice = int(
            input('Enter the position for your next marker: '))
        if space_check(board, playerChoice) == False:
            print('The position you chose is not available, please select another one')
        elif space_check(board, playerChoice):
            spaceStatus = True
    return playerChoice


def replay():
    global board
    replay = input('Do you want to play again?: \'y\' or \'n\' ')
    if replay == 'y':
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        display_board(board)
        return True
    else:
        return False


# Game starts here
print('Welcome to Tic Tac Toe!')

playerOneMarker, playerTwoMarker = player_input()
display_board(board)
game_on = True
firstPlayer = choose_first()
if firstPlayer == 'playerOne':
    print('player One starts first')
else:
    print('player Two starts first')

while game_on:
    # if win_check(board, playerOneMarker):
    #     print('player one wins!')
    #     if replay() == False:
    #         break
    # if win_check(board, playerTwoMarker):
    #     print('player two wins!')
    #     if replay() == False:
    #         break

    if firstPlayer == 'playerOne':
        place_marker(board, playerOneMarker, player_choice(board))
        if win_check(board, playerOneMarker):
            if replay():
                continue
            else:
                break
        place_marker(board, playerTwoMarker, player_choice(board))
        if win_check(board, playerTwoMarker):
            if replay():
                continue
            else:
                break
    else:
        place_marker(board, playerTwoMarker, player_choice(board))
        if win_check(board, playerTwoMarker):
            if replay():
                continue
            else:
                break
        place_marker(board, playerOneMarker, player_choice(board))
        if win_check(board, playerOneMarker):
            if replay():
                continue
            else:
                break
    if full_board_check(board) == True:
        print('DRAW')
        if replay() == False:
            break
        else:
            continue
