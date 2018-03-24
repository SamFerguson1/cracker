import time
from graphics import *

def classss():

    #create window
    win = GraphWin("fuck", 500, 300)

    win.setBackground("tan")

    ptA=Point(100,75)
    ptA.draw(win)
    time.sleep(1)
    
    ptA.move(300,80)
    time.sleep(1)
    ptA.move(-300,0)
    time.sleep(1)
    ptA.move(0,-80)

    ball = Circle(ptA, 40)
    ball.draw(win)
    ball.setFill("pink")
    ball.setOutline("green")
    ball.setWidth(.000001)
        
    
#in the time library which is a part of python's download,
#in the tie library there is a sleep function
#that allows you to pass to it in parameter in seconds
        

    


def main():


    classss()

main()
    
