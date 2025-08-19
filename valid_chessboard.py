"""
Just checking max 2 king and max 16 pions
"""
def good_amount_of_this(chessboard):
    i = 0
    black_king = 0
    white_king = 0
    black_pions = 0
    white_pions = 0

    while (i < 64):
        if (chessboard[i] == 'k' or chessboard[i] == 'K'):
            if (chessboard[i].isupper()):
                black_king += 1
            else :
                white_king += 1
        elif (chessboard[i] == 'p'):
            black_pions += 1
        elif (chessboard[i] == 'P'):
            white_pions += 1
        i += 1
    if (black_king != 1 or white_king != 1):
        print("For playing chess, we need one king for everyone")
        return (0)
    elif (black_pions > 8 or white_pions > 8):
        print("Too many pions for a team.")
        return (0)
    return (1)

"""
This function check if there is the good amount of piece
in each team and if there is no strange character
"""
def good_piece(chessboard, actual_piece):
    i = 0

    if (actual_piece.isupper()):
        pieces = ['K', 'Q', 'R', 'N', 'B', 'P']
    else :
        pieces = ['k', 'q', 'r', 'n', 'b', 'p']
    while (i < 6):
        if (actual_piece == pieces[i]):
            return (1)
        i += 1
    print(f"'{actual_piece}' is an invalid character on the board.\nPlease try with a good chessboard")
    return(0)

"""
Check if the chessboard is OK
if this function find :
    - more or less than 3 kings
    - more than 8 pions
    - more or less than 64 squares
This is return 0
else 1
"""
def nice_chessboard(chessboard):
    i = 0
    error = 0
    black_amount = 0
    white_amount = 0

    if (len(chessboard) != 64):
        print("More or less than 64 square")
        return (0)
    while (i < 64 and error == 0):
        if (chessboard[i] != 'X'):
            if (good_piece(chessboard, chessboard[i])):
                if (chessboard[i].islower()):
                    white_amount += 1
                else :
                    black_amount += 1
            else :
                error = 1
        if (black_amount > 16 or white_amount > 16):
            print("Too many piece for black or white.")
            error = 1
        i +=1
    if ((black_amount == 0 or white_amount == 0)):
        print("You try to play without a team. Please at least a king")
        error = 1
    if (not good_amount_of_this(chessboard)):
        error = 1
    if (error != 0):
        return (0)
    return (1)