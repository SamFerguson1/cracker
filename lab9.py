"""

lab9.py

Name 1:Tatyana Darien
Name 2: Sam Ferguson

The tests for each function are in your main. For this assignment you will
not need to alter the main, but you will need to write the functions that
the main calls. The lab9.doc explains what each function should accept as
parameters and return.

Also, for each function write the input, output, and purpose of each function
before you move into coding them.

For example:

# input: takes two floats
# output: the sum of the two floats
# purpose: add two floats together and return the output
def add(num1, num2):
    return num1 + num2
    
"""
def buildBoard():
#input:nothing
#output: a list of numbers 1-9
#purpose: create a list of numbers 1-9
    numList = []
    #makes the list of 1-9
    for i in range(9):
        numList.append(i+1)
    return numList

def displayBoard(list):
#input: a list of numbers
#output: displays the board
#purpose: create the board
    topList = list[:3]
    middleList = list[3:6]
    bottomList = list[6:9]
    for el in topList:
        print(el, end = "|")
    print()
    print("------")
    for el in middleList:
        print(el, end = "|")
    print()
    print("------")
    for el in bottomList:
        print(el, end = "|")
    print()
        
def isLegal(board, spot):
#input: a board list and a spot to check
#output: boolean value determined by legality
#purpose: to check whether the point is legal
    boardVal = spot-1

    if int(spot) < 10 and int(spot) > 0:
        if board[boardVal] != "x" and board[boardVal] != "o":
            return True
        else:
            return False
    else:
        return False
def fillSpot(board, spot, char):
#input: board list, spot, x or o
#output: print new list
#purpose: rewrites the board state


    legality = isLegal(board, spot)
    #if its a legal move then replace the board list spot where "spot"
    #is located and then print the board state
    if legality == True:
        board[spot-1] = char
        

def isGameWon(board):
#input: board list
#output: winning: t/f
#purpose: to test if the game is still goin' on.
    winningX = ["x", "x", "x"]
    winningO = ["o", "o", "o"]
    topList = board[:3]
    middleList = board[3:6]
    bottomList = board[6:9]
    #checks for horizontal
    if topList == winningX or middleList == winningX or bottomList == winningX or topList == winningO or middleList == winningO or bottomList == winningO:
        return True
    

    #checks for vertical win
    for i in range(len(board)//3):
        testList =[]
        for j in range(3):
            testList.append(board[(j*3) +i])
        if testList == winningO or testList == winningX:
           return True


    #check for diagonal win
    diagonalOne = []
    for i in range(3):
        diagonalOne.append(board[i*4])
    
    diagonalTwo = []
    for i in range(3):
        diagonalTwo.append(board[i*2 +2])
    
    if diagonalTwo == winningO or diagonalTwo == winningX or diagonalOne == winningO or diagonalOne ==winningX:
        return True
    else:
        return False

    

def isGameOver(board,numPlays):
#inputs: board list to check win and number of plays
#outputs: boolean value t/f if the game is over
#purpose: check to see if the game can continue
    winningValue = isGameWon(board)
    if winningValue == True:
        return True
    elif numPlays >= 9:
        return True
    else:
        return False
        
        



def main():
    # Test buildBoard() -> list
    board = buildBoard()
    print("The board:", board)
    print()

    # Test displayBoard(list) -> void
    displayBoard(board)
    print()

    # Test isLegal(board, spot) -> boolean
    sampleBoard = ['x', 2, 'o', 4, 'x', 6, 'o', 8, 9]
    inBoundsTest = isLegal(sampleBoard, 2)
    outBoundsTest = isLegal(sampleBoard, 10)
    spotTakenTestX = isLegal(sampleBoard, 1)
    spotTakenTestO = isLegal(sampleBoard, 3)
    print("The in bounds test is", inBoundsTest, "and should be True.")
    print("The out bounds test is", outBoundsTest, "and should be False.")
    print("The spot taken text x is", spotTakenTestX, "and should be False.")
    print("The spot taken test o is", spotTakenTestO, "and should be False.")
    print()

    # Test fillSpot(board, spot, char) -> void
    sampleBoard = ['x', 2, 'o', 4, 'x', 6, 'o', 8, 9]
    print("Sample board before fill:", sampleBoard)
    fillSpot(sampleBoard, 2, 'x')
    print("Sample board after fill x on spot 2:", sampleBoard)
    fillSpot(sampleBoard, 4, 'o')
    print("Sample board after fill o on spot 4:", sampleBoard)
    fillSpot(sampleBoard, 1, 'o')
    print("Sample board after fail fill o on spot 1:", sampleBoard)
    print()

    # Test isGameWon(board) -> boolean
    gameWonBoardHorizontal = ['o', 'o', 'o', 4, 5, 6, 7, 8, 9]
    gameWonBoardDiagonal = ['o', 2, 3, 4, 'o', 6, 7, 8, 'o']
    gameNotWonBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Game won should be True and is:", isGameWon(gameWonBoardHorizontal))
    print("Game won should be True and is:", isGameWon(gameWonBoardDiagonal))
    print("Game won should be False and is:", isGameWon(gameNotWonBoard))
    print()

    # Test isGameOver(board, numPlays) -> boolean
    gameWonBoard = ['o', 'o', 'o', 4, 5, 6, 7, 8, 9]
    gameOverBoard = ['x', 'o', 'x', 'x', 'o', 'x', 'o', 'x', 'o']
    gameNotOverBoard = ['o', 2, 3, 4, 5, 6, 7, 8, 'x']
    gameIsOverWin = isGameOver(gameWonBoard, 3)
    gameIsOverPlays = isGameOver(gameOverBoard, 9)
    gameNotOver = isGameOver(gameNotOverBoard, 2)
    print("Game is over should be True and is:", gameIsOverWin)
    print("Game is over should be True and is:", gameIsOverPlays)
    print("Game is over should be False and is:", gameNotOver)
    print()

    

    
main()
