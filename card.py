from graphics import *
import time

def valentineCard():
    winWidth = 600
    winHeight = 500
    win = GraphWin("Example", winWidth, winHeight)


    titianImage = Image(Point(300,250), "Censored-Titian.gif")

    titianImage.draw(win)

##    colorHair =    
    
    face = Polygon(Point(104,188), Point(108,185), Point(112,185), Point(116,185), Point(120,188), Point(123,188), Point(126,189), Point(129,192), Point(134,193), Point(134,188), Point(134,187), Point(134,185), Point(135,184), Point(136,182), Point(138,197), Point(140,185), Point(141,188), Point(141,191), Point(141,194), Point(140,201), Point(143,205), Point(148,211), Point(146,214), Point(148,221), Point(152,225), Point(148,217), Point(151,226), Point(151,231), Point(150,237), Point(144,242), Point(147,240), Point(140,242), Point(136,242), Point(134,241), Point(133,237), Point(133,233), Point(139,224), Point(137,227), Point(134,228), Point(131,229), Point(126,233), Point(120,234), Point(115,233), Point(110,231), Point(108,229), Point(105,227), Point(100,225), Point(100,224), Point(100,221), Point(95,217), Point(92,214), Point(91,212), Point(88,210), Point(88,209), Point(88,205), Point(88,201), Point(91,198), Point(91,196), Point(93,193), Point(97,189), Point(100,187))
    face.setFill("peachpuff")
    face.draw(win)
    body = Polygon(Point(44,269), Point(41,272), Point(35,272), Point(31,276), Point(25,289), Point(29,280), Point(26,284), Point(22,293), Point(22,297), Point(22,304), Point(28,304), Point(35,306), Point(40,306), Point(45,309), Point(52,310), Point(56,310), Point(61,307), Point(65,306), Point(72,303), Point(76,303), Point(80,301), Point(83,300), Point(87,300), Point(90,304), Point(93,308), Point(96,311), Point(98,314), Point(101,317), Point(103,321), Point(106,325), Point(107,321), Point(108,316), Point(110,321), Point(112,324), Point(114,323), Point(115,323), Point(115,319), Point(115,317), Point(113,315), Point(115,317), Point(116,318), Point(119,321), Point(119,325), Point(122,329), Point(125,326), Point(125,322), Point(123,319), Point(123,315), Point(123,313), Point(120,309), Point(119,306), Point(123,310), Point(126,316), Point(127,318), Point(130,320), Point(132,320), Point(133,316), Point(132,311), Point(128,307), Point(125,303), Point(123,301), Point(119,297), Point(112,293), Point(110,291), Point(104,288), Point(100,285), Point(94,282), Point(91,282), Point(87,282), Point(82,281), Point(82,277), Point(77,277), Point(73,279), Point(72,277), Point(114,293), Point(128,301), Point(129,297), Point(133,296), Point(137,301), Point(140,305), Point(144,309), Point(148,314), Point(148,317), Point(148,321), Point(151,326), Point(156,330), Point(160,333), Point(168,336), Point(175,341), Point(183,342), Point(189,345), Point(193,349), Point(199,353), Point(208,357), Point(216,361), Point(223,365), Point(233,369), Point(244,372), Point(252,372), Point(257,375), Point(264,377), Point(273,381), Point(280,381), Point(287,381), Point(295,384), Point(305,384), Point(313,385), Point(321,385), Point(328,385), Point(336,384), Point(342,384), Point(354,381), Point(366,381), Point(372,380), Point(377,377), Point(382,375), Point(388,373), Point(391,371), Point(396,374), Point(397,376), Point(404,382), Point(413,385), Point(423,385), Point(428,385), Point(434,384), Point(440,381), Point(448,385), Point(452,382), Point(454,379), Point(460,379), Point(465,378), Point(468,378), Point(473,378), Point(480,381), Point(487,381), Point(495,383), Point(502,385), Point(511,387), Point(511,393), Point(512,399), Point(520,400), Point(525,400), Point(531,395), Point(536,394), Point(540,392), Point(546,391), Point(555,390), Point(566,388), Point(569,385), Point(576,381), Point(578,377), Point(576,375), Point(570,375), Point(565,377), Point(562,377), Point(555,377), Point(546,377), Point(536,374), Point(531,375), Point(531,373), Point(529,369), Point(529,366), Point(525,364), Point(523,362), Point(519,362), Point(515,360), Point(509,360), Point(504,360), Point(501,358), Point(498,358), Point(489,353), Point(485,351), Point(480,346), Point(470,341), Point(464,340), Point(457,337), Point(450,333), Point(444,332), Point(434,325), Point(428,324), Point(420,321), Point(416,318), Point(411,315), Point(405,315), Point(399,313), Point(393,309), Point(386,307), Point(376,305), Point(372,302), Point(362,297), Point(353,296), Point(345,294), Point(340,292), Point(333,292), Point(328,293), Point(325,293), Point(320,293), Point(315,293), Point(306,292), Point(302,289), Point(298,285), Point(291,281), Point(284,277), Point(280,276), Point(273,273), Point(269,272), Point(266,269), Point(260,269), Point(252,266), Point(248,267), Point(242,267), Point(236,268), Point(234,268), Point(230,265), Point(224,261), Point(220,259), Point(214,257), Point(212,254), Point(211,250), Point(205,244), Point(204,241), Point(204,237), Point(200,237), Point(198,239), Point(195,234), Point(188,232), Point(186,230), Point(182,229), Point(179,229), Point(174,229), Point(170,229), Point(162,229), Point(156,225), Point(150,223), Point(152,229), Point(150,234), Point(148,239), Point(144,241), Point(133,241), Point(128,242), Point(124,242), Point(126,249), Point(126,255), Point(122,260), Point(120,265))
    body.setFill("peachpuff")
    body.draw(win)

    hair = Polygon(Point(130,192), Point(126,189), Point(121,186), Point(114,186), Point(110,185), Point(102,185), Point(98,188), Point(93,191), Point(90,194), Point(87,201), Point(90,212), Point(94,215), Point(98,219), Point(102,223), Point(89,209), Point(107,230), Point(118,232), Point(124,232), Point(130,231), Point(133,235), Point(133,241), Point(126,241), Point(124,240), Point(124,250), Point(124,246), Point(125,256), Point(122,260), Point(121,264), Point(121,268), Point(119,271), Point(117,275), Point(117,275), Point(117,277), Point(117,280), Point(117,287), Point(117,291), Point(114,291), Point(111,291), Point(108,289), Point(106,287), Point(104,284), Point(102,284), Point(102,284), Point(96,284), Point(85,281), Point(81,278), Point(75,278), Point(77,273), Point(81,271), Point(84,271), Point(85,270), Point(85,267), Point(85,265), Point(87,259), Point(87,255), Point(87,252), Point(90,247), Point(93,243), Point(94,241), Point(82,245), Point(89,243), Point(78,246), Point(71,252), Point(67,255), Point(63,259), Point(61,259), Point(56,262), Point(51,264), Point(46,267), Point(42,267), Point(46,261), Point(49,258), Point(54,254), Point(53,251), Point(57,248), Point(61,243), Point(53,245), Point(50,242), Point(60,238), Point(69,235), Point(73,234), Point(77,234), Point(84,233), Point(86,229), Point(86,226), Point(87,220), Point(83,214), Point(82,211), Point(80,208), Point(80,207), Point(80,203), Point(80,201), Point(81,195), Point(81,191), Point(81,191), Point(81,183), Point(84,179), Point(85,176), Point(86,174), Point(90,171), Point(94,167), Point(98,165), Point(100,165), Point(105,165), Point(109,163), Point(115,163), Point(121,163), Point(127,169), Point(129,169), Point(133,173), Point(138,179), Point(138,179), Point(142,181), Point(141,184), Point(146,189), Point(143,194), Point(142,197), Point(141,191), Point(141,187), Point(138,183), Point(135,183), Point(135,187), Point(135,190), Point(133,191))
    hair.setFill("dark goldenrod")
    hair.draw(win)

    censorBarOne = Polygon(Point(131,283), Point(143,301), Point(213,256), Point(202,239))
    censorBarOne.draw(win)

    censorBarTwo = Polygon(Point(259,345), Point(275,360), Point(324,313), Point(310,297))
    censorBarTwo.draw(win)


##def pointFinder():
##    winWidth = 600
##    winHeight = 500
##    win = GraphWin("Example", winWidth, winHeight)
##
##
##    titian = Image(Point(winWidth//2,winHeight//2), "Censored-Titian.gif")
##
##    titian.draw(win)

    numClicks = 1000
    points = []
    for i in range(numClicks):
        pt = win.getMouse()
        pt.draw(win)
        points.append(pt)
        ptX = pt.getX()
        ptY = pt.getY()
        print("Point("+str(ptX) + "," + str(ptY) + ")", end = ", ")

def main():
    

    #pointFinder()
    valentineCard()

main()

    
