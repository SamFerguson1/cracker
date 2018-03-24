from graphics import *
import math
import time
#input list of string as paramether
#output void vunction of total number of As in string


def numberOfAs(text):
    total = text.count("a") + text.count("A")
    return total

def allAs(textList):

    total = 0
    for text in textList:
        total+= numberOfAs(text)
    print(total)
        
    

#cirArea()
#input:parameter Circle object
#output: returno of the claculated area

def circArea(circ):
    rad = circ.getRadius()
    area = math.pi*rad**2
    return area


#cahgnColor()
#input: Parameters- shape and a color (string)
#Output: void
#purpose: to change the fill and outline of the object to the color
def changeColor(shape, color):
    
    shape.setFill(color)
    shape.setOutline(color)

#input list of values
#output void
#purpose set the value @ position 0 to python
def changeList(listOfValues):

    

    listOfValues = "python"

#input: Patameter: List of numericc grades
#output:none
#purpose:: add 5 points to each grade in the list
def curve(listOfGrades):

    
    for i in range(len(listOfGrades)):
        listOfGrades[i] = listOfGrades[i] +5
        



def main():

    grades = [70,80,90,100]
    curve(grades)
    print(grades)
##    win = GraphWin()
##
##    ball = Circle(Point(50,50), 20)
##    area  = circArea(ball)
##    ball.draw(win)
##    time.sleep(.5)
##    colors = ["red", "blue", "green", "purple"]
##
##    for color in colors:
##        changeColor (ball, color)
##        time.sleep(.5)
##    print(area)
##    allAs(["Bryan", "bradley", "sam, ""andrew earl","adam"])

main()
