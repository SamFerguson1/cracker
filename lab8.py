# Lab8.py
# Name 1: Patrick McCabe
# Name 2: Sam ferguson
from graphics import *
def squareEach(nums):
    for i in range(len(nums)):
        nums[i]= nums[i]**2
    return nums
def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    return strList
def sumOfSquares(nums):
    toNumbers(nums)
    squareEach(nums)
    total = sumList(nums)
    return total
def moveCircle(shape, newCenter):
    radius = shape.getRadius()
    center = shape.getCenter()
    centerX = center.getX()
    centerY = center.getY()
    newCenterY = newCenter.getY() - centerY
    newCenterX = newCenter.getX() - centerX
    shape.move(newCenterX, newCenterY)
    
def createUsername(fullName):
    fullName = fullName.split()
    firstName = fullName[0]
    lastName = fullName[1]

    username = lastName[:3] + firstName[:2] + str(ord(firstName[-1])-ord("a")+1) +  str(ord(lastName[-1])-ord("a")+1) 
    return username

def usernamesFromFile(inputFileName, outputFileName):

    names = ""
    for line in inputFileName:
        names+= line
    names = names.split("\n")
    print(names)
    for i in range(len(names)):
        print(createUsername(names[i]), file = outputFileName)
        
def insert(string,substring, pos):
    
    newString = string [:pos] + substring + string[pos:]
    return newString
#main() should be the only function executed when you are checked off for this lab
#thus add code to main() to call any functions you write.
def main():
##    squareNums = [2,4,6,8]    
##    squareTotal = squareEach(squareNums)
##    print(squareTotal)
##    sumNums = [2,4,6,8]
##    sumTotal = sumList(sumNums)
##    print(sumTotal)
##    strList = ["2", "4", "6", "8"]
##    strNums = toNumbers(strList)
##    print(strNums)
##    newList = ["2", "4", "6", "8"]
##    total = sumOfSquares(newList)
##    print(total)
##
##    win = GraphWin("f", 500,500)
##    circle = Circle(Point(100,100), 40)
##    circle.draw(win)
##    center = Point(300,300)
##    win.getMouse()
##    moveCircle(circle, center)
##    
##        name = "John Smith"
##        
##        username = createUsername(name)
##        print(username)
##        file = open("names.txt", "r")
##        output = open("usernames.txt", "w")
##        usernamesFromFile(file, output)

    originalString = "thing"
    substring ="steaming"
    num = 3
    print(insert(originalString, substring, num))
    
        
main()

    
