def tictactoe():
    board = initializeBoard()
    last = 'O'

    while (True):
        if last == 'O':
            last = playX(board)
        else:
            last = playO(board)

        if win(board) or isFilled(board):
            printGrid(board)
            break

    if win(board):
        print(f"{last} player won")
    else:
        print("It's a tie. Good game!")


def printGrid(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            print(f"| {board[row][column]} ", end = "")
        print("|\n-------------")



def initializeBoard():
    board = []

    for i in range(3):
        board.append([' ' for x in range(3)])

    return board



def playX(board):
    printGrid(board)

    rowX = int(input("Enter a row (0, 1, or 2) for player X: "))
    columnX = int(input("Enter a column (0, 1, or 2) for player X: "))

    if fillable(board, rowX, columnX):
        board[rowX][columnX] = 'X'
    else:
        print("Space is occupied. Try again")
        playX(board)

    return 'X'


def playO(board):
    printGrid(board)

    rowO = int(input("Enter a row (0, 1, or 2) for player O: "))
    columnO = int(input("Enter a column (0, 1, or 2) for player O: "))

    if fillable(board, rowO, columnO):
        board[rowO][columnO] = 'O'
    else:
        print("Space is occupied. Try again")
        playO(board)

    return 'O'


def fillable(board, row, column):
    return board[row][column] == ' '


def verticalWin(board):
    for i in range(len(board[0])):
        if board[0][i] != ' ' and board[0][i] == board[1][i] \
            and board[0][i] == board[2][i]:
            return True
        
    return False


def horizontalWin(board):
    for i in range(len(board)):
        if board[i][0] != ' ' and board[i][0] == board[i][1] \
            and board[i][0] == board[i][2]:
            return True
        
    return False



def leftDiagonalWin(board):
    return board[0][0] != ' ' and board[0][0] == board[1][1] \
        and board[0][0] == board[2][2]


def rightDiagonalWin(board):
    return board[0][2] != ' ' and board[0][2] == board[1][1] \
        and board[0][2] == board[2][0]

    
def isFilled(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                return False
        
    return True


def win(board):
    return verticalWin(board) or horizontalWin(board) or \
        leftDiagonalWin(board) or rightDiagonalWin(board)
        

def main():
    tictactoe()


main()