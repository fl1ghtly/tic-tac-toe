import copy

def makeBoard(sizeTuple):
    board = []
    length = []
    for x in range(sizeTuple[0]):
        length.append(None)
    for y in range(sizeTuple[1]):
        board.append(length)
    return board

def render(board):
    pos = 0
    # TODO fix misalignment
    for y in range(len(board)):
        line = "|"
        for x in range(len(board[0])):
            pos += 1
            if board[y][x] is None:
                line += " " + str(pos) + " |"
            else:
                line += " " + str(board[y][x]) + " |"
        print(line)
    return

def possMoves(board, size):
    # Converts from integer positions to the index values usable by
    # the board list
    possDic = {}
    i = 1
    for y in range(len(board)):
        for x in range(len(board[0])):
            possDic.update({i:[y, x]})
            i += 1
    return possDic

def getMove(board, size):
    dictMoves = possMoves(board, size)

    # Ensures that the value given is compatible with the board
    while True:
        try:
            ans = int(input("Where do you want to play:\n"))
            if ans > (size[0] * size[1]) or ans < 0:
                print("Your number does not meet the board size. Please try again.")
            else:
                return dictMoves.get(ans)   
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

# TODO change findWinner and findTie to account for variable size
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
    # (x size, y size)
    size = (4, 4)
    board = makeBoard(size)
    flip = chooseSide()

    while True:
        move = getMove(board, size)
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
