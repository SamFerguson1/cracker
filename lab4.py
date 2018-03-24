## Sam Ferguson
## lab4.py

from graphics import *
import math

def sequence():
    numTerms = eval(input("How many terms do you want to display in the sequence: "))
    for i in range(numTerms):
        term = i + 1 + i % 2
        print(term, end=" ")
    print()
    #yeah i get how this is goin i'm likin it

def pi():

    print("This code approximates the value of pi.")
    numTerms = eval(input("How many series terms to calculate?: "))
    fact = 1
    for i in range(numTerms):
        denominator = i+1+i % 2
        numerator = i+((i+1)%2)+1
        piTerm= numerator / denominator
        fact = fact * piTerm
    piApprox= fact *2
    print("The approximate value of pi is: "+str(piApprox)+".")
def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
#things I have to do
# make the window 400 x 400 DONE
# make the squares draw

    #Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4 - Squares", width, height)

    #number of times user can move circle
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height/1.2)
    instructions = Text(instPt,"Click to draw a new square.")
    instructions.draw(win)

    ptCenter = Point(width/2, height/2)
    #builds a rectangle
    shape = Rectangle(ptCenter, Point(180,180))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #circle
    cloneShape = shape.clone()
    for i in range(numClicks):
        cloneShape = cloneShape.clone()
        p = win.getMouse()
        c = cloneShape.getCenter() #center of circle
        
        #move amount is distance from center of circle to the
        #point where the user clicked
        
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        cloneShape.move(dx, dy)
        cloneShape.draw(win)

    instructions.setText("Click again to quit.")
    win.getMouse()
    win.close()


def fib():

    print("calc fibonacci bruh")

    numSeq = eval(input("What number of the sequence do you want?: "))

    total = 0
    numOne = 0
    numTwo = 1
    for i in range(numSeq):

        temp = numTwo
        numTwo = numOne + numTwo
        numOne = temp
        
        
    print("The number "+ str(numSeq)+" of the sequence is: " +str(numOne))

def displayHouse():

    width = 500
    height = 500
    win = GraphWin("Lab 4 - in 'da house", width, height)

    ptA = Point(100,100)
    ptB = Point(250,10)
    ptC = Point(400,100)
    ptD = Point(100,400)
    ptE = Point(325,400)
    ptF = Point(225,250)
    ptG = Point(120,250)
    ptH = Point(200,300)
    ptI = Point(300,120)
    ptJ = Point(250, 200)

    triangle = Polygon(ptA, ptB, ptC)
    square = Rectangle(ptC, ptD)
    door = Rectangle(ptE, ptF)
    windowOne = Rectangle(ptG, ptH)
    windowTwo= Rectangle(ptI,ptJ)

    triangle.setFill("beige")
    square.setFill("brown")    
    door.setFill("red")
    windowOne.setFill("blue")
    windowTwo.setFill("blue")

    triangle.draw(win)
    square.draw(win)
    door.draw(win)
    windowOne.draw(win)
    windowTwo.draw(win)

def pi2():

#inputs number of terms
#output: the pi approximation
    total = 0
    numTerms = eval(input("How many terms to sum?"))
    for i in range(numTerms):
        total = (-1+2*i%2)
        denominator = 1/(2*1)
        piApprox=4*total
        print(total)
        

def main():
    #sequence()
    #squares()
    #pi()
    #fib()
    #displayHouse()
    pi2()

    
    
main()

 
