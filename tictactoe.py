import copy

def makeBoard():
    return [[None, None, None], [None, None, None], [None, None, None]]

def render(board):
    # | [0][0] | [0][1] | [0][2] |
    #
    # | [1][0] | [1][1] | [1][2] |
    #
    # | [2][0] | [2][1] | [2][2] |

    print(" | {0} | {1} | {2} |\n".format(board[0][0], board[0][1], \
                                          board[0][2]).replace("None", " "),
          "| {0} | {1} | {2} |\n".format(board[1][0], board[1][1], \
                                         board[1][2]).replace("None", " "),
          "| {0} | {1} | {2} |\n".format(board[2][0], board[2][1], \
                                         board[2][2]).replace("None", " "))
    return

def getMove():
    # Converts from integer positions to the index values usable by
    # the board list
    posMoves = {1:[0, 0], 2:[0, 1], 3:[0, 2],
                4:[1, 0], 5:[1, 1], 6:[1, 2],
                7:[2, 0], 8:[2, 1], 9:[2, 2]}

    # Ensures that the value given is compatible with the board
    while True:
        try:
            ans = int(input("Where do you want to play:\n"))
            if ans > 9 or ans < 0:
                print("Your number does not meet the board size. Please try again.")
            else:
                return posMoves.get(ans)   
        except ValueError:
            print("Invalid Command. Please try again")
    
def doMove(board, pos, side):
    # Done in order to not introduces mutables
    new = copy.deepcopy(board)
    new[pos[0]][pos[1]] = side
    return new

def validMove(board, pos):
    # If there is a character in that location
    # the given index will return a character
    # that is not 'None'
    if board[pos[0]][pos[1]] is not None:  
        return False
    else:
        return True

def chooseSide():
    while True:
        side = str(input("Choose your side, X or O: ").upper())
        if side == "X":
            return True
        elif side == "O":
            return False
        else:
            print("Invalid Side")

def findWinner(board):
    # Checks horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            # Chosen board index to return is arbitrary since
            # all of them should return the same character
            return board[i][0]

    # Checks vertical
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]

    # Checks diagonal
    # Top Left to Bottom Right Diag
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    # Bottom Left to Top Right Diag
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    
    # If none are found
    return None

def findTie(board):
    # Looks for available spaces
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return False

    # Determines if there is already a winner
    winner = findWinner(board)
    if winner:
        return False
    else:
        return True


# __name__ == "__main__" allows for unit testing to occur properly
if __name__ == "__main__":
    board = makeBoard()
    flip = chooseSide()

    while True:
        move = getMove()
        if not validMove(board, move):
            print("You picked an invalid spot!")
        else:
            if flip:       
                board = doMove(board, move, "X")
                flip = False
            else:
                board = doMove(board, move, "O")
                flip = True
            render(board)

            winner = findWinner(board)
            tie = findTie(board)
            if winner is not None and not tie:
                print("{} is the winner!".format(winner))
                break
            elif tie:
                print("No one wins!")
                break
