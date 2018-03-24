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

def whichLetter(board):
    
    numXs = board.count("x")
    numOs = board.count("o")
    if numOs < numXs:
        return "o"
    if numXs == numOs:
        return "x"
    
"""  1|2|X
      4|5|6
      7|8|9   """


def main():

    #build the board
    board = buildBoard()
    #display opening board
    displayBoard(board)
    #works waaay easier if x can just go first
    print("\nx goes first")
    #prompt the user for where to go
    print()
    whereGo = int(input("Which number do you want to fill?: "))    
    #start at x to make the whichLetter() method better
    fillSpot(board, whereGo, "x")     
    #the board now has x int he spot they put
    #display  board
    displayBoard(board)
    #make a counter for number of plays
    numPlays = 1
    #find the initial truth value of game over to accumulate
    overTruthVal = isGameOver(board, numPlays)
    #while loop that runs the game while the game isn't over
    while overTruthVal == False:
        #ask where to go
        whereGo = int(input("Which number do you want to fill?: "))
        #aesthetic print()
        print()
        #check which character to fill
        character = whichLetter(board)
        #fill the spot with the character
        fillSpot(board, whereGo, character)
        #display the board again
        displayBoard(board)
        #increase the number of plays by 1
        numPlays += 1
        #recheck the truth value of gameOver
        overTruthVal = isGameOver(board, numPlays)
        #run again until it's not
    wonTruth = isGameWon(board)
    lastCharacter = whichLetter(board)

    if wonTruth == True and lastCharacter == "x":
        print("o wins the game!")
    if wonTruth == True and lastCharacter == "o":
        print("x wins the game!")
    else:
        print("tie game, what a shame")

main()



                
        
        
