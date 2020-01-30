from random import randrange
import hw3_ec1



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
            board_to_show += " " # display cell number
        else:
            board_to_show += player_name(board[i]) # display player's mark
        if (i + 1) % 8 == 0: # every 3 cells, start a new row
            board_to_show += "|\n"
        else:
            board_to_show += "| " # within a row, divide the cells
          
    print()
    print(board_to_show)

def put_on_board(num_animal, player_id, board):
    """
    Parameters
    ----------
    num_animal: int
        how many animals do player want to put in board
    player_id: int
        player id
    board: list
        the board
    """
    num = 0
    while num < num_animal:
        index = randrange(len(board))
        if board[index] == 0:
            board[index] = player_id
            num += 1
#####################################################################
#####################################################################
#####################################################################
# constant
PLAYER_NAMES = ['Nobody', 'X', 'O']
# X- cats
# O- dogs

def main():
    board = [0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,]
    display_board(board)
    
    num_cats = input("How many cats do you want to add to the world?\n")
    num_dogs = input("How many dogs do you want to add to the world?\n")

    # randomly put cats on the board
    put_on_board(int(num_cats), 1, board)
    
    # randomly put dogs on the board
    put_on_board(int(num_dogs), 2, board)
    
    display_board(board)

if __name__ == "__main__":
    main()