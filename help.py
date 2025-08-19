import time

def help():
    choice = None
    penalty = 2
    print("\nYou asked for help. About what topic ?")
    while (choice == None):
        choice = input("\n0 - Quit help page \n1 - What is this : kqbnrp \n2 - Example of chessboard \n>>> ")
        if (choice == '0'):
            print("Bye !")
            return
        elif (choice == '1'):
            print("\nThis is for you're piece. \nk : King \nq : Queen \nb : Bishop \nn : Knight \nr : Rook \np : Pawn")
            print("X represent empty square. \nlowercase is for white, the other is for black")
            choice = None
        elif (choice == '2'):
            print("\nThis is the basic starting position : rnbkqbnrppppppppXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPRNBKQBNR")
            print("White start at the bottom of chessboard. The white king's ('k') position is (0 ; 5). In a grid it's look like that : ")
            print("r n b q k b n r")
            print("p p p p p p p p")
            print("X X X X X X X X")
            print("X X X X X X X X")
            print("X X X X X X X X")
            print("X X X X X X X X")
            print("P P P P P P P P")
            print("R N B Q K B N R")
            print("Here, one might think that you are playing the Blacks.")
            choice = None
        else :
            print(f"Nah, this is not a choice. {penalty} second penalty for you ! :)")
            time.sleep(penalty)
            choice = None
            penalty *= 2