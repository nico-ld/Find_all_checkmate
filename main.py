import valid_chessboard as verif
import help

"""
Taking the chessboard to create a grid
"""
def easier_in_grid(chessboard):
    grid = []
    row = []
    i = 0
    j = 0

    while (i < 8):
        row.append(chessboard[j])
        if (len(row) == 8):
            grid.append(row)
            row = []
            i += 1
        j += 1
    return (grid)

def this_is_check(chessgrid, row, column, color):
    i = 0
    j = 0
    ennemies = ['K', 'Q', 'R', 'N', 'B', 'P']
    if (color == "black"):
        while (i < len(ennemies)):
            ennemies[i].lower()
            i += 1
        i = 0

    # Check by pion
    if (color == "white" and row < 7): # If we play white
        if (column > 0 and chessgrid[row + 1][column - 1] == ennemies[5]):
            return (1)
        elif (column < 7 and chessgrid[row + 1][column + 1] == ennemies[5]):
            return (1)
    elif (color == "black" and row > 0): # If we play black
        if (column > 0 and chessgrid[row - 1][column - 1] == ennemies[5]):
            return (1)
        elif (column < 7 and chessgrid[row - 1][column + 1] == ennemies[5]):
            return (1)

    # Check on row or column
    while (i < 8 and j < 8):
        if (chessgrid[i][column] == ennemies[1] or chessgrid[i][column] == ennemies[2]):
            return (1)
        elif (chessgrid[row][j] == ennemies[1] or chessgrid[row][j] == ennemies[2]):
            return (1)
        i += 1
        j += 1
    
    # Check on left diagonal
    i = row
    j = column
    while (i > 0 and j > 0):
        i -= 1
        j -= 1
    while (i < 8 and j < 8):
        if (chessgrid[i][j] == ennemies[1] or chessgrid[i][j] == ennemies[4]):
            return (1)
        i += 1
        j += 1
        
    # Check on right diagonal
    i = row
    j = column
    while (i < 8 and j < 8):
        i += 1
        j += 1
    while (i > 0 and j > 0):
        if (chessgrid[i][j] == ennemies[1] or chessgrid[i][j] == ennemies[4]):
            return (1)
        i -= 1
        j -= 1
    return (0)

def our_piece(chessgrid, color, row, column):
    pieces = ['K', 'Q', 'R', 'N', 'B', 'P']
    i = 0

    if (color == "white"):
        while (i < 6):
            pieces[i].lower()
            i += 1
    if (chessgrid[row][column] in pieces):
        return (1)
    return (0)

def this_is_checkmate(chessgrid, color_to_play):
    i, j, count_of_check = 0, 0, 0
    king_to_mate = 'K'

    if (color_to_play == "black"):
        king_to_mate.lower()

    # Taking position of king to mate
    while (chessgrid[i][j] != king_to_mate):
        if (j == 7):
            i += 1
            j = 0
        j += 1
    
    # Looking for check on all square around
    row = -1
    while (row <= 1):
        column = -1
        if (i + row < 0 or i + row > 7):
            count_of_check += 3
        else :
            while (column <= 1):
                if (j + column < 0 or j + column > 7):
                    count_of_check += 1
                elif (our_piece(chessgrid, color_to_play, i + row, j + column)):
                    count_of_check += 1
                elif (this_is_check(chessgrid, i + row, j + column, color_to_play)):
                    count_of_check += 1
                column += 1
        row += 1

def backtracking(chessgrid, move_for_mate, color_to_play, possibilities):
    i = 0
    row = 0
    column = 0
    pieces = ['K', 'Q', 'R', 'N', 'B', 'P']

    if (color_to_play == "white"):
        while (i < 6):
            pieces[i].lower()
            i += 1
    i = 0
    if (this_is_checkmate(chessgrid, color_to_play)):
        return (1)
    while (i < 6):
        


def main(chessboard):
    color_to_play = None
    move_for_mate = 0
    possibilities = 0

    if (not verif.nice_chessboard(chessboard)):
        return
    while (color_to_play == None):
        color_to_play = input("\nYou're chessboard is Valid !\nWho is playing next move ? (black/white)\n>>> ").lower()
        if (color_to_play.lower() != "white" and color_to_play.lower() != "black"):
            print("Please, choose between white or black.")
            color_to_play = None
    while (move_for_mate == 0):
        try:
            move_for_mate = int(input("\nHow many move for mat ? (1 - 5)\n>>> "))
            if (move_for_mate < 1 or move_for_mate > 5):
                print("Please, choose between 1 and 5")
                move_for_mate = 0
        except ValueError:
            print("Don't write bullshit, only digit is accepted")
            move_for_mate = 0
    chessgrid = easier_in_grid(chessboard)
    possibilities = backtracking(chessgrid, move_for_mate, color_to_play, possibilities)

choice = None

while(choice == None):
    choice = input("\nwhite : kqbnrp\nblack : KQBNRP\nEmpty square : X\nEnter you're chessboard in one line. \n>>> ")
    if (choice == "help"):
        help.help()
        choice = None
    else:
        main(choice)

#rnbkqbnrppppppppXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPRNBKQBNR --> basic starting position