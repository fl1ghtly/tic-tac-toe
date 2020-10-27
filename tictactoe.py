import copy

def makeBoard(sizeTuple):
    board = []
    length = []
    for x in range(sizeTuple[0]):
        length.append(None)
    for y in range(sizeTuple[1]):
        new = copy.deepcopy(length)
        board.append(new)
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

def hzWinner(board):
    # Checks each horizontal line for a winner
    for hz in board:
        if hz[0] is not None:
            if hz.count(hz[0]) == len(hz):
                return hz[0]
                
def vtWinner(board):
    for x in range(len(board[0])):
        vt = []
        for y in range(len(board)):
            vt.append(board[y][x])
        if vt[0] is not None:
            if vt.count(vt[0]) == len(vt):
                return vt[0]

def diagWinner(board):
    # Diagonal only works for boards of even size

    # Top Left to Bottom Right
    if len(board) == len(board[0]):
        # If there is nothing in the top left, there cant be a top left diagonal
        if board[0][0] is not None:
            topLeft = []
            for i in range(len(board)):
                topLeft.append(board[i][i])
            # if the amount of tiles matches the length of the list
            # then it is a diagonal win
            if topLeft.count(topLeft[0]) == len(topLeft):
                return topLeft[0]
            else: 
                return False

    # Bottom Left to Top Right
        if board[len(board) - 1][0] is not None:
            bottomLeft = []
            for j in range(len(board)):
                bottomLeft.append(board[len(board) - 1 - j][j])
            if bottomLeft.count(bottomLeft[0]) == len(bottomLeft):
                return bottomLeft[0]
            else: 
                return False

                
# TODO change findWinner and findTie to account for variable size
def findWinner(board):
    hz = hzWinner(board)
    if hz is not None:
        return hz
    vt = vtWinner(board)
    if vt is not None:
        return vt

    diag = diagWinner(board)
    if diag is not False:
        return diag

    # If none are found
    return None

def findTie(board):
    # Looks for available spaces
    for i in range(len(board)):
        for j in range(len(board[0])):
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
    size = (3, 3)
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
