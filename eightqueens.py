def makeBoard(size):
    #initate a clean board
    board = []
    for i in range(size):
        row = ['o' for i in range(size)]
        board.append(row)
    return (board)

def displayBoard(boardState):
    for item in boardState:
        print (item)

def placeQueen(boardState, row, col, n):
    #rule out invalid rows and columns
    for i in range((len(boardState[row]))):
        boardState[i][col] = str(n)
        boardState[row][i] = str(n)

    #rule out invalid diagonal spaces
    while i >= 0 and i <= len(boardState)

    #place the nth Queen in the row and column of the current board state
    boardState[row][col] = 'Q' + str(n)


    #return new board state
    return (boardState)

# def eightQueens():
#     board = makeBoard()
#     rowCount = 0
#     colCount = 0
#
#     for row in board:
#         count += 1
#         if 'Q' not in row:
#             print ('No queen in row', count )
#             for item in row:
#                 colCount += 1
#                 if item
#
#     displayBoard(board)


game = makeBoard(8)
temp = placeQueen(game, 3, 5, 3)
displayBoard(temp)
