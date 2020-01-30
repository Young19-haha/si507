
# CONSTANTS
PLAYER_NAMES = ["Nobody", "X", "O"] 


# FUNCTIONS
def player_name(player_id):
    '''return the name of a player with a specified ID

    Looks up the name in the PLAYER_NAMES global list

    Parameters
    ----------
    player_id: int
        player's id, which is an index into PLAYER_NAMES

    Returns
    -------
    string
        the player's name

    '''
    return PLAYER_NAMES[player_id]


def display_board(board):
    '''display the current state of the board

    board layout:
    1 | 2 | 3 | 4 | 5 | 6 | 7
    8 | 9 | 10| 11| 12| 13| 14
    15| 16| 17| 18| 19| 20| 21
    22| 23| 24| 25| 26| 27| 28
    29| 30| 31| 32| 33| 34| 35
    36| 37| 38| 39| 40| 41| 42
    43| 44| 45| 46| 47| 48| 49

    Numbers are replaced by players' names once they move. 
    Iterate through the board and choose the right thing
    to display for each cell.

    Parameters
    ----------
    board: list
        the playing board

    Returns
    -------
    None
    '''

    board_to_show = "" # string that will display the board, starts empty
    for i in range(len(board)):
        if board[i] == 0: # 0 means unoccupied
            # displayed numbers are one greater than the board index
            board_to_show += str(i + 1) # display cell number
        else:
            board_to_show += player_name(board[i]) # display player's mark
        if (i + 1) % 7 == 0: # every 3 cells, start a new row
            board_to_show += "\n"
        else:
            if i < 9 or board[i] != 0:
                board_to_show += " | " # within a row, divide the cells
            else:
                board_to_show += "| "
    print()
    print(board_to_show)


def make_move(player, board):
    '''allows a player to make a move in the game

    displays who's move it is (X or O)
    prompts the user to enter a number 1-9
    validates input, repeats until valid input is entered
    checks move is valid (space is unoccupied), repeats until valid move
    is entered

    Parameters
    ----------
    player: int
        the id of the player to move (1 = X, 2 = O)

    board: list
        the board upon which to move
        the board is modified in place when a valid move is entered
    '''
    # TODO: Implement function
    # pass
    while True:
        try:
            move = input(f"{player_name(player)}'s move: ")
            # if int(move):
            if int(move) >= 1 and int(move) <= 49:
                if board[int(move)-1] != 0:
                    print("That space is occupied, try another.")
                else:
                    try:
                        if board[int(move) + 6] != 0:
                            break
                        else:
                            print("The stone should be pilled from the bottom.")
                    except IndexError:
                        break
                    
            else:
                print("Enter a number between 1 and 49.")
        except ValueError:
            print("Entera number between 1 and 49.")
    board[int(move)-1] = player
    # print(board)


def check_win_vertical(board):
    # TODO: write docstring
    """check whether any vertical line has same 4 elements from bottom

    Parameters
    ----------
    board: list
        the board after each move
    
    Returns
    -------
    int
        the player ID

    """
    # TODO: implement function
    for i in range(len(board)):
        try:
            if (board[i] != 0 and 
                board[i] == board[i-7] and 
                board[i] == board[i-7-7] and
                board[i] == board[i-7-7-7] ):
                return board[i]
        except IndexError:
            break


    # if (board[42] != 0 and 
    #     board[42] == board[42-7] and 
    #     board[42] == board[42-7-7] and
    #     board[42] == board[42-7-7-7] ):
    #     return board[42]
    # if (board[43] != 0 and 
    #     board[43] == board[43-7] and 
    #     board[43] == board[43-7-7] and
    #     board[43] == board[43-7-7-7] ):
    #     return board[43]
    # if (board[44] != 0 and 
    #     board[44] == board[44-7] and 
    #     board[44] == board[44-7-7] and
    #     board[44] == board[44-7-7-7] ):
    #     return board[44]
    # if (board[45] != 0 and 
    #     board[45] == board[45-7] and 
    #     board[45] == board[45-7-7] and
    #     board[45] == board[45-7-7-7] ):
    #     return board[45]
    # if (board[46] != 0 and 
    #     board[46] == board[46-7] and 
    #     board[46] == board[46-7-7] and
    #     board[46] == board[46-7-7-7] ):
    #     return board[46]
    # if (board[47] != 0 and 
    #     board[47] == board[47-7] and 
    #     board[47] == board[47-7-7] and
    #     board[47] == board[47-7-7-7] ):
    #     return board[47]
    # if (board[48] != 0 and 
    #     board[48] == board[48-7] and 
    #     board[48] == board[48-7-7] and
    #     board[48] == board[48-7-7-7] ):
    #     return board[48]
    return 0


def check_win_diagonal(board):
    # TODO: write docstring
    """check either diagonal line has same elements

    Parameters
    ----------
    board: list
        the board after each move
    
    Returns
    -------
    int
        the player ID
    """
    # TODO: implement function
    for i in range(21,25):
        n = 0
        while n < 4:
            if (board[i] != 0 and 
                board[i] == board[i-6] and 
                board[i] == board[i-6-6] and
                board[i] == board[i-6-6-6] ):
                return board[i]
            n += 1
            i += 7
    for i in range(24, 28):
        n = 0
        while n < 4:
            if (board[i] != 0 and 
                board[i] == board[i-8] and 
                board[i] == board[i-8-8] and
                board[i] == board[i-8-8-8] ):
                return board[i]
            n += 1
            i += 7
    return 0


def check_win(board):
    '''checks a board to see if there's a winner

    delegates to functions that check horizontally, vertically, and 
    diagonally to see if there is a winner. Returns the first winner
    found in the case of multiple winners.

    Parameters
    ----------        
    board: list
        the board to check

    Returns
    -------
    int
        the player ID of the winner. 0 means no winner found.
    '''

    winner = check_win_vertical(board)
    if (winner != 0):
        return winner
    
    return check_win_diagonal(board)


def next_player(current_player):
    '''determines who goes next

    given the current player ID, returns the player who should 
    go next

    Parameters
    ----------        
    current_player: int
        the id of the player who's turn it is now

    Returns
    -------
    int
        the id of the player to go next
    '''
    # TODO: Implement function
    if current_player == 1:
        return 2
    else:
        return 1 

# MAIN PROGRAM (INDENT LEVEL 0)
def main():
    # GLOBAL VARIABLES
    board = [0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0]

    player = 1          # X goes first
    moves_left = 49      # number of moves so far 
    winner = 0          # "Nobody" is winning to start

    while(moves_left > 0 and winner == 0):
        display_board(board)
        make_move(player, board)
        winner = check_win(board)
        player = next_player(player)
        moves_left -= 1

    print(f"\nGame over! {player_name(winner)} wins!")

if __name__ == "__main__":
    main()