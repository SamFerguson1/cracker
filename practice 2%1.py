from graphics import *
def February():
    winWidth=800
    winHeight = 500
    win = GraphWin("Hello World",800,500)

    #ball's center at (x,y)

    ptA= Point(100, 125)
    ptB= Point(400, 200)
    ball = Circle(ptA,100)

    ball.draw(win)
    ctrBall = ball.getCenter()
    ctrX = ctrBall.getX()
    ctrY = ctrBall.getY()
    print(ctrBall)

    print("Ball's center at: (" +str(ctrX) + ", " +str(ctrY) + ")")

    winCtr = Point(winWidth//2, winHeight//2)
    
    ovalA= Oval(ctrBall,winCtr)
    ovalA.setFill("yellow")
    ovalA.setOutline("blue")

    ovalA.draw(win)
    centerOval = ovalA.getCenter()
    ovalX = centerOval.getX()
    ovalY = centerOval.getY()
    print("Oval's center at: (" +str(ovalX) + ", " +str(ovalY) + ")")

    points = []
    for i in range(5):
        pt = win.getMouse()
        pt.draw(win)
        points.append(pt)
        ptX = pt.getX()
        ptY = pt.getY()
        print("Point(" +str(ptX)+ "," +str(ptY) +")", end = " ")
    polygonUser = Polygon(points)
    polygonUser.draw(win)



February()
