# Lab5.py
# Name 1:
# Name 2: 

from graphics import *


def target():
    winWidth = 500
    winHeight = winWidth
    win = GraphWin("Archery Target", winWidth, winHeight)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()



def triangle():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Draw a Triangle", winWidth, winHeight)


    pointsTriangle = []

    for i in range(3):
        
        trianglePoint = win.getMouse()
        trianglePoint.draw(win)
        pointsTriangle.append(trianglePoint)
    triangle = Polygon(pointsTriangle)
    triangle.draw(win)

    xOne = pointsTriangle[0].getX() 
    xTwo= pointsTriangle[1].getX()
    xThree = pointsTriangle[2].getX()

    yOne = pointsTriangle[0].getY() 
    yTwo = pointsTriangle[1].getY()
    yThree = pointsTriangle[2].getY()

    dxOne = pointsTriangle[0].getX()-pointsTriangle[1].getX()
    dxTwo = pointsTriangle[1].getX() - pointsTriangle[2].getX()
    dxThree = pointsTriangle[2].getX() -pointsTriangle[0].getX()

    dyOne = pointsTriangle[0].getY()-pointsTriangle[1].getY()
    dyTwo = pointsTriangle[1].getY() - pointsTriangle[2].getY()
    dyThree = pointsTriangle[2].getY()- pointsTriangle[0].getY()

    print(dxOne, dxTwo, dxThree, dyOne, dyTwo, dyThree)

    lineOne = (dxOne**2 +dyOne**2)*.5
    lineTwo = (dxTwo**2 +dyTwo**2)*.5
    lineThree = (dxThree**2 +dyThree**2)*.5


    perimeter = lineOne + lineTwo + lineThree
    s = (abs(lineOne) + abs(lineTwo) + abs(lineThree))/2
    area = (s*(s-lineOne)*(s-lineTwo)*(s-lineThree))*.5

    print("P", perimeter, "A", area)











    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()

def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redText.setTextColor("red")

    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")

    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")

    #display rgb text
    redText.draw(win)
    greenText.draw(win)
    blueText.draw(win)
    
    
def main():
    #target()
    triangle()
    #colorShape()

main()





