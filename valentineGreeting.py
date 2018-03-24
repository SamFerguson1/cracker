import time
from graphics import*
#name: Sam Ferguson
#valentineGreeting.py

#Problem: Make an animated valentine card
#inputs: One click to close
#outputs: A heart/arrow animation & text
#statement of authenticity
#   The code used in this script is my own



def valentineGreeting():
    #create window
    winWidth = 1000
    winHeight = 800
    win = GraphWin("Happy Valentines", winWidth, winHeight)
    
       
    #background color
    win.setBackground("pink")

    #for some reason you can't move the GraphWin object before
    #it starts animating so i added something to let you adjust GraphWin
    #before the animation begins
    happyVday = Text(Point(500,50), "Click for animation")
    happyVday.setTextColor("crimson")
    happyVday.draw(win)


    #Valentines greeting
    happyVday = Text(Point(500,200), "Happy Valentine's Day")
    happyVday.setSize(36)
    happyVday.setTextColor("crimson")
    happyVday.draw(win)

    #the individual polygons that make up the heart ln33-141
    #construct
    weirdCircleThing = Polygon(Point(454,289), Point(451,288), Point(449,288), Point(446,289), Point(446,291), Point(446,292), Point(447,295), Point(449,298), Point(450,300), Point(453,300), Point(455,301), Point(456,301), Point(457,300), Point(458,298), Point(458,296), Point(458,293), Point(458,292), Point(458,291))
    #setFill
    weirdCircleThing.setFill("blue")
    #draw
    weirdCircleThing.draw(win)
    #repeat
    venaCava = Polygon(Point(447,289), Point(445,290), Point(441,291), Point(440,291), Point(439,291), Point(438,289), Point(436,287), Point(431,287), Point(427,287), Point(424,288), Point(420,289), Point(420,291), Point(420,297), Point(419,305), Point(417,312), Point(416,319), Point(414,328), Point(415,335), Point(414,340), Point(412,345), Point(412,352), Point(412,357), Point(411,363), Point(410,369), Point(410,374), Point(412,379), Point(413,382), Point(414,385), Point(416,383), Point(418,380), Point(419,375), Point(421,372), Point(423,367), Point(424,363), Point(424,359), Point(424,354), Point(425,351), Point(427,344), Point(428,341), Point(429,339), Point(432,337), Point(433,334), Point(434,328), Point(436,325), Point(436,320), Point(439,315), Point(440,312), Point(443,310), Point(446,306), Point(448,306), Point(452,304), Point(449,302), Point(448,299), Point(447,295), Point(448,291))
    venaCava.setFill("medium blue")
    venaCava.draw(win)

    pulmBranchOne = Polygon(Point(415,321), Point(414,324), Point(415,329), Point(414,332), Point(413,337), Point(413,339), Point(412,341), Point(409,342), Point(404,344), Point(402,344), Point(400,344), Point(397,344), Point(396,341), Point(393,337), Point(392,333), Point(391,329), Point(393,328), Point(396,326), Point(400,325), Point(401,324), Point(404,323), Point(405,322), Point(408,322), Point(412,321), Point(415,321), Point(416,322), Point(415,326), Point(414,333))
    pulmBranchOne.setFill("medium blue")
    pulmBranchOne.draw(win)

    pulmBranchTwo = Polygon(Point(412,351), Point(412,354), Point(411,357), Point(411,361), Point(411,364), Point(411,367), Point(412,367), Point(412,369), Point(411,372), Point(408,372), Point(407,373), Point(404,373), Point(401,373), Point(399,371), Point(399,370), Point(397,368), Point(396,366), Point(395,364), Point(394,362), Point(394,360), Point(394,357), Point(395,357), Point(398,356), Point(400,354), Point(401,353), Point(404,352), Point(407,351), Point(410,351), Point(412,351), Point(412,351), Point(412,354), Point(412,358))
    pulmBranchTwo.setFill("medium blue")
    pulmBranchTwo.draw(win)

    pulmBranchThree = Polygon(Point(407,396), Point(405,395), Point(404,395), Point(400,395), Point(397,394), Point(395,394), Point(391,393), Point(390,393), Point(387,393), Point(385,393), Point(382,393), Point(380,394), Point(380,395), Point(378,396), Point(377,399), Point(376,400), Point(376,403), Point(377,405), Point(377,408), Point(379,410), Point(379,410), Point(380,413), Point(380,415), Point(382,416), Point(385,417), Point(389,417), Point(391,417), Point(394,417), Point(395,417), Point(396,417), Point(399,417), Point(400,417), Point(402,417), Point(404,417), Point(404,413), Point(404,411), Point(405,408), Point(406,405), Point(408,401), Point(408,399), Point(408,396))
    pulmBranchThree.setFill("crimson")
    pulmBranchThree.draw(win)

    pulmBranchFour = Polygon(Point(404,417), Point(402,417), Point(400,417), Point(397,417), Point(396,417), Point(392,417), Point(391,417), Point(389,418), Point(387,419), Point(385,420), Point(384,420), Point(383,420), Point(381,420), Point(380,421), Point(380,421), Point(379,422), Point(378,424), Point(377,426), Point(378,428), Point(380,431), Point(380,434), Point(382,436), Point(384,438), Point(385,440), Point(388,441), Point(390,441), Point(390,440), Point(392,439), Point(393,438), Point(394,438), Point(396,438), Point(396,438), Point(398,437), Point(400,437), Point(400,435), Point(400,433), Point(400,431), Point(401,430), Point(401,428), Point(402,426), Point(402,425), Point(403,423), Point(403,421), Point(404,419), Point(404,418), Point(403,417))
    pulmBranchFour.setFill("crimson")
    pulmBranchFour.draw(win)

    venaCavaBottom = Polygon(Point(413,483), Point(412,487), Point(412,489), Point(412,493), Point(411,496), Point(411,499), Point(411,500), Point(411,502), Point(411,505), Point(411,507), Point(411,509), Point(411,511), Point(411,514), Point(410,516), Point(410,518), Point(410,521), Point(412,522), Point(413,523), Point(416,525), Point(418,525), Point(422,527), Point(424,528), Point(425,528), Point(428,529), Point(430,529), Point(431,529), Point(432,529), Point(436,529), Point(438,529), Point(440,529), Point(441,529), Point(444,527), Point(446,527), Point(447,526), Point(448,524), Point(449,522), Point(450,520), Point(450,518), Point(450,517), Point(449,517), Point(447,516), Point(447,516), Point(444,514), Point(443,513), Point(441,512), Point(440,511), Point(440,509), Point(439,509), Point(436,507), Point(436,505), Point(434,505), Point(432,503), Point(431,501), Point(427,499), Point(424,498), Point(423,497), Point(423,495), Point(421,493), Point(420,493), Point(419,489), Point(417,489), Point(416,487), Point(415,485), Point(415,485), Point(414,486), Point(414,488), Point(414,490), Point(414,493), Point(413,497), Point(412,501))
    venaCavaBottom.setFill("medium blue")
    venaCavaBottom.draw(win)

    ventricleThing = Polygon(Point(431,339), Point(430,340), Point(428,341), Point(428,344), Point(426,346), Point(425,350), Point(425,353), Point(425,356), Point(426,361), Point(424,362), Point(423,367), Point(422,370), Point(420,373), Point(419,377), Point(416,381), Point(414,385), Point(412,387), Point(411,390), Point(410,394), Point(410,397), Point(408,400), Point(407,405), Point(405,409), Point(405,412), Point(404,416), Point(403,419), Point(402,421), Point(401,425), Point(400,428), Point(400,432), Point(400,434), Point(400,439), Point(399,444), Point(400,446), Point(399,449), Point(400,454), Point(401,458), Point(401,461), Point(404,463), Point(406,468), Point(408,472), Point(409,466), Point(410,461), Point(412,458), Point(413,454), Point(414,451), Point(416,449), Point(420,445), Point(425,441), Point(429,441), Point(432,434), Point(436,430), Point(442,426), Point(448,420), Point(451,415), Point(454,410), Point(459,406), Point(460,402), Point(462,397), Point(463,390), Point(463,387), Point(463,383), Point(460,382), Point(456,381), Point(452,378), Point(448,375), Point(443,371), Point(440,369), Point(437,366), Point(435,363), Point(433,358), Point(432,354), Point(432,349), Point(431,342))
    ventricleThing.setFill("crimson")
    ventricleThing.draw(win)

    aorta = Polygon(Point(480,366), Point(478,360), Point(478,355), Point(477,351), Point(478,345), Point(480,339), Point(482,333), Point(486,326), Point(487,322), Point(490,319), Point(491,319), Point(494,319), Point(495,319), Point(498,319), Point(501,319), Point(502,317), Point(503,315), Point(506,315), Point(508,314), Point(511,313), Point(515,312), Point(518,312), Point(521,311), Point(523,307), Point(524,301), Point(523,295), Point(522,288), Point(521,284), Point(518,280), Point(516,276), Point(514,272), Point(511,268), Point(509,267), Point(507,263), Point(506,258), Point(505,253), Point(505,240), Point(504,235), Point(498,233), Point(495,233), Point(493,233), Point(492,234), Point(491,237), Point(491,240), Point(490,244), Point(490,249), Point(488,251), Point(487,246), Point(487,239), Point(486,236), Point(479,235), Point(477,235), Point(474,236), Point(474,252), Point(477,261), Point(470,261), Point(464,252), Point(455,247), Point(446,252), Point(446,256), Point(450,262), Point(454,267), Point(458,271), Point(459,277), Point(455,283), Point(455,287), Point(457,290), Point(458,294), Point(458,299), Point(454,303), Point(451,303), Point(447,307), Point(443,315), Point(437,322), Point(434,330), Point(434,339), Point(433,351), Point(437,361), Point(439,368), Point(446,372), Point(454,375), Point(456,377), Point(463,381), Point(468,380), Point(472,379), Point(473,372), Point(479,367))
    aorta.setFill("crimson")
    aorta.draw(win)

    pulmMain = Polygon(Point(491,320), Point(493,320), Point(497,320), Point(501,318), Point(503,317), Point(505,316), Point(507,314), Point(509,313), Point(512,313), Point(513,312), Point(516,312), Point(520,311), Point(523,310), Point(525,310), Point(531,310), Point(536,310), Point(543,311), Point(548,316), Point(547,324), Point(546,333), Point(546,336), Point(542,337), Point(538,338), Point(532,339), Point(528,339), Point(527,340), Point(528,343), Point(528,345), Point(529,351), Point(528,353), Point(527,360), Point(527,363), Point(527,366), Point(524,368), Point(522,369), Point(520,369), Point(518,372), Point(516,375), Point(514,378), Point(514,382), Point(510,384), Point(505,385), Point(501,387), Point(499,384), Point(496,380), Point(493,376), Point(491,374), Point(487,372), Point(484,371), Point(482,369), Point(480,364), Point(479,360), Point(477,355), Point(477,353), Point(477,350), Point(477,345), Point(480,340), Point(481,335), Point(482,331), Point(484,328), Point(484,325), Point(486,322), Point(488,321), Point(491,320), Point(492,320), Point(495,319), Point(498,317), Point(501,317), Point(508,316))
    pulmMain.setFill("medium blue")
    pulmMain.draw(win)

    iGotNothin = Polygon(Point(530,352), Point(529,356), Point(529,359), Point(529,363), Point(527,368), Point(527,372), Point(527,377), Point(527,379), Point(530,382), Point(533,384), Point(535,384), Point(537,386), Point(541,387), Point(543,388), Point(545,389), Point(548,391), Point(551,393), Point(554,394), Point(556,394), Point(559,391), Point(560,388), Point(561,383), Point(562,380), Point(562,378), Point(561,375), Point(559,373), Point(558,371), Point(556,368), Point(554,367), Point(553,365), Point(552,363), Point(549,363), Point(545,359), Point(543,358), Point(541,357), Point(538,355), Point(534,354), Point(532,352), Point(530,352), Point(529,352), Point(529,352), Point(529,355), Point(529,360), Point(528,363))
    iGotNothin.setFill("pale violet red")
    iGotNothin.draw(win)

    pulmBranchFive = Polygon(Point(573,396), Point(575,396), Point(580,395), Point(583,394), Point(585,394), Point(591,393), Point(594,393), Point(595,393), Point(600,393), Point(601,394), Point(604,395), Point(605,396), Point(606,401), Point(606,404), Point(606,406), Point(606,409), Point(605,413), Point(604,413), Point(600,414), Point(595,415), Point(593,416), Point(586,417), Point(586,417), Point(582,417), Point(582,415), Point(581,414), Point(579,412), Point(578,409), Point(576,406), Point(574,404), Point(574,402), Point(573,401), Point(572,400), Point(571,399), Point(571,397), Point(574,396), Point(578,396))
    pulmBranchFive.setFill("crimson")
    pulmBranchFive.draw(win)

    pulmBranchSix = Polygon(Point(584,420), Point(586,420), Point(585,418), Point(587,418), Point(590,418), Point(591,418), Point(593,418), Point(596,418), Point(599,419), Point(600,420), Point(604,421), Point(607,422), Point(607,422), Point(608,426), Point(607,429), Point(606,433), Point(605,437), Point(604,440), Point(604,441), Point(601,441), Point(599,441), Point(597,441), Point(595,441), Point(592,437), Point(591,434), Point(590,431), Point(586,425), Point(584,422), Point(584,421), Point(584,419), Point(584,417))
    pulmBranchSix.setFill("crimson")
    pulmBranchSix.draw(win)

    apex = Polygon(Point(572,400), Point(571,403), Point(569,406), Point(569,410), Point(570,412), Point(570,414), Point(570,415), Point(570,415), Point(569,414), Point(568,413), Point(568,415), Point(569,415), Point(570,418), Point(573,420), Point(574,422), Point(577,424), Point(580,427), Point(578,430), Point(577,431), Point(574,431), Point(570,429), Point(569,429), Point(567,429), Point(567,431), Point(569,433), Point(570,436), Point(570,438), Point(570,442), Point(569,445), Point(567,447), Point(565,447), Point(564,449), Point(565,452), Point(566,453), Point(567,455), Point(568,458), Point(568,461), Point(565,463), Point(562,464), Point(562,465), Point(560,467), Point(559,469), Point(558,473), Point(558,476), Point(558,480), Point(558,483), Point(558,487), Point(558,491), Point(560,495), Point(562,496), Point(565,499), Point(558,500), Point(558,504), Point(561,506), Point(564,509), Point(561,511), Point(561,515), Point(561,519), Point(560,519), Point(559,521), Point(561,523), Point(562,524), Point(563,527), Point(561,529), Point(564,530), Point(566,533), Point(567,534), Point(570,534), Point(573,534), Point(575,534), Point(578,535), Point(582,535), Point(584,535), Point(586,531), Point(588,526), Point(590,523), Point(591,520), Point(592,518), Point(593,513), Point(594,509), Point(595,504), Point(596,501), Point(597,497), Point(598,491), Point(598,487), Point(599,482), Point(599,477), Point(599,463), Point(597,455), Point(596,451), Point(595,445), Point(594,440), Point(592,437), Point(591,434), Point(589,428), Point(584,417), Point(581,413), Point(578,410), Point(576,407), Point(573,403))
    apex.setFill("crimson")
    apex.draw(win)

    pulmBottom = Polygon(Point(467,521), Point(469,522), Point(472,523), Point(472,524), Point(476,526), Point(480,529), Point(485,531), Point(488,532), Point(492,533), Point(496,534), Point(499,535), Point(501,535), Point(503,537), Point(503,540), Point(503,542), Point(504,546), Point(504,552), Point(504,557), Point(504,564), Point(504,566), Point(502,569), Point(499,570), Point(496,572), Point(492,573), Point(488,575), Point(483,576), Point(475,576), Point(470,574), Point(468,572), Point(467,569), Point(466,565), Point(466,561), Point(465,555), Point(465,549), Point(465,542), Point(465,536), Point(465,530), Point(465,527), Point(465,525), Point(468,524), Point(471,523), Point(473,524))
    pulmBottom.setFill("medium blue")
    pulmBottom.draw(win)

    arteryOne = Polygon(Point(568,391), Point(568,393), Point(566,397), Point(563,398), Point(561,401), Point(558,402), Point(557,403), Point(556,403), Point(554,403), Point(552,403), Point(550,403), Point(548,403), Point(545,405), Point(544,407), Point(541,407), Point(539,407), Point(536,406), Point(535,406), Point(538,409), Point(539,410), Point(540,411), Point(542,413), Point(540,417), Point(540,417), Point(544,416), Point(544,413), Point(544,411), Point(546,409), Point(547,406), Point(553,405), Point(556,405), Point(556,407), Point(556,411), Point(556,414), Point(556,417), Point(554,420), Point(553,421), Point(550,423), Point(548,425), Point(547,425), Point(548,428), Point(548,430), Point(550,431), Point(551,428), Point(551,425), Point(552,425), Point(554,425), Point(555,427), Point(555,430), Point(554,432), Point(553,434), Point(554,435), Point(556,433), Point(557,433), Point(559,433), Point(559,433), Point(559,431), Point(559,429), Point(559,427), Point(558,425), Point(558,423), Point(558,420), Point(558,418), Point(559,417), Point(560,416), Point(560,413), Point(560,411), Point(560,409), Point(559,407), Point(559,405), Point(562,405), Point(564,404), Point(565,405), Point(566,409), Point(566,411), Point(568,416), Point(572,423), Point(572,421), Point(572,417), Point(571,412), Point(570,409), Point(568,407), Point(567,405), Point(565,401), Point(566,400), Point(568,397), Point(570,395), Point(571,394), Point(572,391), Point(572,389), Point(570,388), Point(568,388), Point(568,389), Point(568,393))
    arteryOne.setFill("crimson")
    arteryOne.draw(win)

    veinOne = Polygon(Point(527,381), Point(529,385), Point(530,387), Point(533,388), Point(534,389), Point(538,391), Point(541,393), Point(546,396), Point(548,398), Point(550,400), Point(550,405), Point(550,409), Point(549,413), Point(548,417), Point(546,421), Point(544,425), Point(542,428), Point(542,431), Point(545,430), Point(546,428), Point(549,425), Point(550,423), Point(550,419), Point(552,416), Point(553,413), Point(553,411), Point(553,409), Point(554,405), Point(554,403), Point(554,401), Point(554,398), Point(555,397), Point(558,396), Point(561,395), Point(564,394), Point(566,391), Point(568,389), Point(568,385), Point(568,381), Point(566,379), Point(565,379), Point(564,379), Point(562,379), Point(562,380), Point(561,383), Point(561,385), Point(560,388), Point(558,391), Point(555,391), Point(551,393), Point(548,391), Point(546,389), Point(543,387), Point(539,386), Point(535,384), Point(531,383), Point(530,383), Point(530,385), Point(532,386))
    veinOne.setFill("medium blue")
    veinOne.draw(win)

    veinTwo = Polygon(Point(465,389), Point(467,393), Point(467,397), Point(468,400), Point(468,403), Point(472,405), Point(476,408), Point(480,409), Point(485,415), Point(487,417), Point(484,417), Point(481,415), Point(480,413), Point(477,412), Point(476,410), Point(474,410), Point(473,410), Point(471,411), Point(471,413), Point(471,412), Point(469,410), Point(468,409), Point(468,411), Point(470,413), Point(475,414), Point(477,415), Point(478,417), Point(476,417), Point(473,417), Point(472,417), Point(472,417), Point(472,421), Point(472,422), Point(472,426), Point(470,426), Point(469,424), Point(468,421), Point(468,420), Point(466,418), Point(465,417), Point(464,415), Point(464,413), Point(463,409), Point(463,408), Point(462,413), Point(460,413), Point(460,415), Point(457,417), Point(456,420), Point(453,423), Point(451,425), Point(449,428), Point(448,433), Point(452,436), Point(455,441), Point(456,441), Point(458,443), Point(457,445), Point(455,445), Point(453,442), Point(451,441), Point(448,438), Point(446,436), Point(445,434), Point(445,432), Point(442,431), Point(441,433), Point(438,435), Point(434,436), Point(433,436), Point(432,434), Point(432,433), Point(436,431), Point(438,429), Point(441,428), Point(444,426), Point(444,425), Point(446,422), Point(448,419), Point(449,416), Point(452,413), Point(454,411), Point(456,409), Point(460,405), Point(460,404), Point(463,399), Point(463,393), Point(464,390), Point(464,389))
    veinTwo.setFill("medium blue")
    veinTwo.draw(win)

    fatOne = Polygon(Point(465,387), Point(466,384), Point(466,381), Point(470,379), Point(472,377), Point(474,373), Point(474,370), Point(476,367), Point(480,367), Point(483,367), Point(486,371), Point(486,371), Point(487,371), Point(489,373), Point(491,375), Point(494,377), Point(496,381), Point(498,384), Point(501,386), Point(509,386), Point(512,384), Point(516,379), Point(517,375), Point(520,369), Point(524,368), Point(526,376), Point(526,380), Point(529,385), Point(530,387), Point(538,391), Point(546,396), Point(548,400), Point(549,403), Point(546,404), Point(542,405), Point(536,405), Point(534,405), Point(532,407), Point(531,410), Point(530,413), Point(527,415), Point(525,415), Point(524,411), Point(524,405), Point(523,403), Point(520,399), Point(517,396), Point(512,394), Point(506,391), Point(500,391), Point(491,391), Point(482,391), Point(478,391), Point(473,394), Point(473,398), Point(475,402), Point(477,406), Point(474,405), Point(471,404), Point(468,402), Point(467,399), Point(467,395), Point(466,391), Point(465,389), Point(464,387))
    fatOne.setFill("navajo white")
    fatOne.draw(win)

    veinThree = Polygon(Point(412,460), Point(414,460), Point(416,458), Point(418,455), Point(420,452), Point(421,450), Point(421,454), Point(421,455), Point(421,456), Point(424,454), Point(426,452), Point(428,451), Point(426,456), Point(424,458), Point(423,460), Point(425,460), Point(427,460), Point(429,455), Point(431,455), Point(429,448), Point(430,447), Point(433,446), Point(434,446), Point(434,451), Point(433,455), Point(431,457), Point(429,459), Point(429,461), Point(430,464), Point(433,465), Point(435,470), Point(435,473), Point(436,475), Point(437,479), Point(439,480), Point(442,481), Point(445,483), Point(446,483), Point(448,488), Point(450,492), Point(453,497), Point(456,499), Point(458,502), Point(455,502), Point(453,499), Point(450,499), Point(449,494), Point(449,498), Point(449,501), Point(451,504), Point(449,506), Point(448,502), Point(446,498), Point(446,495), Point(446,491), Point(446,488), Point(445,487), Point(443,486), Point(440,486), Point(438,486), Point(438,487), Point(438,490), Point(438,489), Point(434,486), Point(433,483), Point(432,480), Point(431,476), Point(432,475), Point(432,472), Point(431,470), Point(428,467), Point(426,464), Point(423,462), Point(421,461), Point(419,460), Point(418,463), Point(417,465), Point(414,467), Point(413,468), Point(412,468), Point(410,469))
    veinThree.setFill("crimson")
    veinThree.draw(win)

    fatTwo = Polygon(Point(412,460), Point(415,460), Point(416,457), Point(419,455), Point(420,452), Point(423,451), Point(422,453), Point(426,451), Point(427,453), Point(427,456), Point(424,458), Point(424,459), Point(428,460), Point(431,457), Point(432,454), Point(430,451), Point(430,447), Point(432,445), Point(435,445), Point(435,449), Point(436,453), Point(437,450), Point(438,446), Point(437,441), Point(438,437), Point(441,436), Point(444,434), Point(443,432), Point(436,433), Point(434,435), Point(432,435), Point(430,437), Point(426,441), Point(424,442), Point(422,443), Point(419,446), Point(417,447), Point(415,449), Point(414,453), Point(413,456), Point(413,458), Point(415,460))
    fatTwo.setFill("navajo white")
    fatTwo.draw(win)

    fatThree = Polygon(Point(437,455), Point(436,457), Point(437,462), Point(437,465), Point(441,465), Point(443,465), Point(445,468), Point(447,472), Point(448,475), Point(450,477), Point(451,477), Point(453,477), Point(455,480), Point(456,481), Point(458,481), Point(460,482), Point(457,485), Point(457,486), Point(457,486), Point(459,488), Point(460,489), Point(462,489), Point(464,490), Point(466,492), Point(468,493), Point(471,493), Point(471,495), Point(468,497), Point(471,499), Point(472,500), Point(473,501), Point(476,504), Point(477,505), Point(471,508), Point(473,510), Point(477,511), Point(482,514), Point(480,517), Point(478,517), Point(474,517), Point(471,515), Point(469,513), Point(469,516), Point(467,516), Point(464,516), Point(462,516), Point(461,517), Point(459,517), Point(457,517), Point(454,516), Point(449,514), Point(447,513), Point(444,511), Point(442,509), Point(437,507), Point(434,505), Point(428,499), Point(424,496), Point(422,494), Point(419,490), Point(416,486), Point(413,483), Point(412,479), Point(412,475), Point(411,471), Point(411,469), Point(413,468), Point(415,466), Point(418,463), Point(420,462), Point(424,462), Point(427,465), Point(429,467), Point(431,471), Point(432,475), Point(432,477), Point(431,480), Point(433,483), Point(435,485), Point(437,487), Point(441,486), Point(442,486), Point(444,487), Point(444,491), Point(445,495), Point(447,498), Point(448,501), Point(449,503), Point(451,501), Point(450,500), Point(452,499), Point(454,499), Point(456,501), Point(457,498), Point(456,496), Point(452,494), Point(452,493), Point(450,488), Point(448,483), Point(445,481), Point(441,480), Point(437,477), Point(436,473), Point(433,469), Point(432,462), Point(431,460), Point(433,456), Point(434,454))
    fatThree.setFill("navajo white")
    fatThree.draw(win)

    fatFour = Polygon(Point(546,404), Point(543,407), Point(541,407), Point(537,406), Point(534,405), Point(538,410), Point(540,412), Point(540,415), Point(542,418), Point(544,416), Point(544,413), Point(546,410), Point(547,407), Point(549,407), Point(548,413), Point(545,419), Point(544,423), Point(541,427), Point(540,431), Point(542,434), Point(546,431), Point(547,429), Point(548,429), Point(549,430), Point(551,428), Point(551,425), Point(554,425), Point(554,427), Point(552,431), Point(551,433), Point(551,435), Point(555,435), Point(558,435), Point(560,431), Point(559,427), Point(557,423), Point(557,420), Point(558,417), Point(559,414), Point(558,411), Point(558,409), Point(558,407), Point(561,406), Point(562,405), Point(563,406), Point(564,412), Point(566,416), Point(568,417), Point(569,422), Point(570,423), Point(573,423), Point(575,423), Point(576,423), Point(577,427), Point(575,429), Point(570,430), Point(568,428), Point(565,428), Point(566,434), Point(568,437), Point(569,443), Point(568,446), Point(566,446), Point(563,446), Point(554,446), Point(549,443), Point(543,443), Point(538,440), Point(536,439), Point(538,435), Point(538,432), Point(538,429), Point(538,427), Point(536,427), Point(536,423), Point(536,420), Point(533,419), Point(532,417), Point(531,413), Point(531,411), Point(531,409), Point(533,406), Point(533,403), Point(537,403), Point(539,403), Point(544,402), Point(547,402), Point(548,402))
    fatFour.setFill("navajo white")
    fatFour.draw(win)

    fatFive = Polygon(Point(539,440), Point(536,442), Point(534,444), Point(531,445), Point(529,445), Point(528,445), Point(526,446), Point(526,449), Point(528,451), Point(528,453), Point(530,456), Point(532,457), Point(533,455), Point(535,453), Point(537,452), Point(540,451), Point(540,453), Point(537,457), Point(536,459), Point(536,461), Point(536,465), Point(536,468), Point(537,470), Point(537,473), Point(537,474), Point(535,479), Point(535,481), Point(534,483), Point(534,485), Point(533,486), Point(532,489), Point(534,493), Point(534,494), Point(537,496), Point(538,493), Point(540,493), Point(540,497), Point(538,500), Point(538,505), Point(536,508), Point(536,511), Point(535,515), Point(534,519), Point(532,520), Point(531,522), Point(528,524), Point(524,525), Point(522,525), Point(520,525), Point(516,522), Point(512,521), Point(511,519), Point(509,517), Point(508,515), Point(506,514), Point(504,513), Point(501,513), Point(494,514), Point(492,515), Point(489,515), Point(487,515), Point(485,515), Point(485,519), Point(486,519), Point(488,521), Point(492,524), Point(492,524), Point(494,525), Point(500,528), Point(506,530), Point(510,531), Point(510,532), Point(511,533), Point(514,534), Point(519,535), Point(523,535), Point(526,535), Point(530,535), Point(533,535), Point(539,535), Point(545,536), Point(550,537), Point(558,537), Point(563,537), Point(568,537), Point(570,536), Point(570,536), Point(568,533), Point(567,531), Point(566,529), Point(564,527), Point(561,523), Point(560,521), Point(560,517), Point(560,512), Point(560,509), Point(560,505), Point(559,501), Point(557,500), Point(559,497), Point(560,496), Point(559,493), Point(558,490), Point(558,486), Point(557,483), Point(556,479), Point(556,474), Point(556,469), Point(557,466), Point(561,464), Point(566,461), Point(568,458), Point(565,453), Point(563,448), Point(564,446), Point(560,445), Point(557,445), Point(552,445), Point(549,444), Point(545,443), Point(542,442), Point(540,441), Point(537,440))
    fatFive.setFill("navajo white")
    fatFive.draw(win)

    inside = Polygon(Point(475,405), Point(478,404), Point(478,400), Point(474,397), Point(474,393), Point(478,392), Point(483,391), Point(490,390), Point(499,390), Point(507,392), Point(514,394), Point(518,399), Point(522,403), Point(526,414), Point(526,416), Point(530,415), Point(532,419), Point(535,423), Point(538,427), Point(539,437), Point(536,440), Point(530,445), Point(526,446), Point(526,448), Point(529,452), Point(531,455), Point(536,455), Point(538,453), Point(535,459), Point(535,463), Point(535,469), Point(535,475), Point(534,482), Point(533,485), Point(532,491), Point(535,495), Point(538,493), Point(538,499), Point(536,509), Point(532,516), Point(528,522), Point(522,524), Point(514,520), Point(510,515), Point(506,512), Point(502,511), Point(497,512), Point(491,513), Point(485,514), Point(481,513), Point(478,511), Point(474,510), Point(471,507), Point(477,503), Point(475,501), Point(474,499), Point(470,498), Point(469,497), Point(471,493), Point(470,491), Point(465,490), Point(461,488), Point(458,487), Point(456,484), Point(456,482), Point(457,480), Point(452,479), Point(451,476), Point(448,471), Point(444,468), Point(441,465), Point(436,458), Point(436,451), Point(435,443), Point(437,439), Point(438,437), Point(442,435), Point(448,438), Point(451,441), Point(455,443), Point(458,442), Point(453,436), Point(451,432), Point(450,428), Point(451,423), Point(454,421), Point(459,416), Point(462,413), Point(466,417), Point(468,423), Point(471,427), Point(473,419), Point(477,417), Point(478,414), Point(471,411), Point(471,410), Point(475,410), Point(481,414), Point(483,416), Point(481,409), Point(477,407))
    inside.setFill("crimson")
    inside.draw(win)

    veinFour = Polygon(Point(547,456), Point(543,461), Point(541,468), Point(541,472), Point(544,474), Point(542,480), Point(541,485), Point(543,485), Point(544,493), Point(547,499), Point(545,505), Point(544,513), Point(547,514), Point(544,525), Point(544,530), Point(549,533), Point(557,537), Point(564,537), Point(560,535), Point(555,532), Point(554,527), Point(550,518), Point(552,518), Point(551,508), Point(556,511), Point(555,505), Point(552,498), Point(547,493), Point(547,485), Point(549,481), Point(555,473), Point(549,477), Point(550,470), Point(551,467), Point(548,461), Point(548,457))
    veinFour.setFill("crimson")
    veinFour.draw(win)

    bottom = Polygon(Point(480,513), Point(477,515), Point(471,515), Point(469,515), Point(467,516), Point(466,516), Point(461,516), Point(453,519), Point(460,519), Point(466,520), Point(470,521), Point(473,523), Point(476,525), Point(490,529), Point(495,532), Point(500,534), Point(506,535), Point(510,535), Point(512,533), Point(509,531), Point(503,529), Point(492,525), Point(490,522), Point(486,519), Point(483,515), Point(482,513), Point(480,516), Point(478,515), Point(474,516), Point(469,516), Point(467,515))
    bottom.setFill("crimson")
    bottom.draw(win)

    #little delay before the animation for aesthetic reasons
    time.sleep(1)
    win.getMouse()
    
    #arrow polygon drawing
    arrowHead = Polygon(Point(241,548), Point(298,547), Point(280,591), Point(280,556))
    arrowHead.setFill("dim gray")
    arrowHead.draw(win)
    

    arrowShaft = Polygon(Point(266,554), Point(62,651), Point(70,660), Point(279,560), Point(279,555))
    arrowShaft.setFill("saddleBrown")
    arrowShaft.draw(win)
    

    arrowFeathers = Polygon(Point(70,660), Point(65,697), Point(64,684), Point(60,691), Point(62,679), Point(56,683), Point(62,677), Point(46,681), Point(55,670), Point(43,670), Point(55,664), Point(35,682), Point(19,681), Point(31,660), Point(42,658), Point(31,651), Point(17,633), Point(33,639), Point(55,647), Point(58,647), Point(66,651), Point(67,658), Point(68,659), Point(70,660), Point(65,654), Point(66,651), Point(71,655))
    arrowFeathers.setFill("white")
    arrowFeathers.draw(win)
    #polygon drew over arrow to make it inside
    heartSquare = Polygon(Point(445,452), Point(460,460), Point(470,465), Point(474,478), Point(485,477), Point(494,467), Point(493,460), Point(479,449), Point(467,446), Point(448,451))
    heartSquare.setFill("crimson")
    heartSquare.setOutline("crimson")
    heartSquare.draw(win)

    bloodDrip = Polygon(Point(462,458), Point(462,461), Point(463,464), Point(462,468), Point(462,472), Point(462,475), Point(464,479), Point(464,483), Point(462,487), Point(466,488), Point(468,485), Point(466,483), Point(465,478), Point(466,473), Point(467,468), Point(465,463), Point(465,458), Point(462,456))
    bloodDrip.setFill("crimson")
    bloodDrip.setOutline("crimson")
    cloneDrip = bloodDrip.clone()
    #loop animating the arrow    
    for i in range(90):
        arrowHead.move(2,-1)
        arrowShaft.move(2,-1)
        arrowFeathers.move(2,-1)
        time.sleep(.00001)

    #arrow now in heart
    time.sleep(.2)
    #draw invisible blood object that only draws in loop
    bloodDrip.move(0,-25)
    bloodDrip.draw(win)
    for i in range(50):
        bloodDrip.move(0,1)
        time.sleep(.001)

    #splatter
    #give it a sec then let the splatter
    time.sleep(.2)
    splatOne = Polygon(Point(462,458), Point(461,466), Point(458,474), Point(453,482), Point(451,488), Point(457,493), Point(463,491), Point(464,486), Point(466,478), Point(468,471), Point(471,465), Point(471,458), Point(474,441), Point(474,435), Point(475,428), Point(469,423), Point(466,430), Point(466,440), Point(463,448), Point(463,453))
    splatOne.setFill("crimson")
    splatOne.setOutline("crimson")
    splatOne.draw(win)

    splatTwo = Polygon(Point(462,458), Point(461,466), Point(458,474), Point(453,482), Point(451,488), Point(457,493), Point(463,491), Point(464,486), Point(466,478), Point(468,471), Point(471,465), Point(471,458), Point(474,441), Point(474,435), Point(475,428), Point(469,423), Point(466,430), Point(466,440), Point(463,448), Point(463,453))
    splatTwo.setFill("crimson")
    splatTwo.setOutline("crimson")
    splatTwo.draw(win)

    splatThree = Polygon(Point(465,449), Point(468,453), Point(470,459), Point(470,464), Point(467,469), Point(466,472), Point(465,482), Point(466,495), Point(467,499), Point(466,504), Point(474,506), Point(479,505), Point(480,497), Point(479,490), Point(480,483), Point(480,475), Point(479,469), Point(478,454), Point(475,449), Point(471,446), Point(469,444), Point(466,444), Point(464,444), Point(461,455), Point(457,453), Point(471,460), Point(480,467), Point(489,474), Point(497,487), Point(501,493), Point(504,502), Point(516,507), Point(524,507), Point(523,499), Point(514,494), Point(509,483), Point(500,468), Point(498,468), Point(494,460), Point(489,457), Point(482,455), Point(464,453), Point(458,454))
    splatThree.setFill("crimson")
    splatThree.setOutline("crimson")
    splatThree.draw(win)

    splatFour = Polygon(Point(458,459), Point(456,455), Point(456,451), Point(460,448), Point(463,447), Point(468,448), Point(474,451), Point(477,450), Point(484,445), Point(491,441), Point(495,440), Point(502,440), Point(507,445), Point(505,453), Point(504,459), Point(511,462), Point(516,464), Point(517,469), Point(517,471), Point(516,472), Point(511,471), Point(504,467), Point(498,463), Point(493,461), Point(485,460), Point(478,461), Point(472,466), Point(468,466), Point(464,463), Point(461,461))
    splatFour.setFill("crimson")
    splatFour.setOutline("crimson")
    splatFour.draw(win)

    #lame splatter but I'm not going to peicemeal test all of this
    for i in range(40):
        splatOne.move(-2,-2)
        splatTwo.move(-2,-3)
        splatThree.move(1,3)
        splatFour.move(3,6)
        time.sleep(.001)
        
    splatOne.undraw()
    splatTwo.undraw()
    splatThree.undraw()
    splatFour.undraw()
    #undraw splat because it'll just loop weird if I don't
    #give it a second to display close
    time.sleep(1)
    #close message
    closeMessage = Text(Point(winWidth//2, winHeight*.9), "Click anywhere to close")
    closeMessage.draw(win)
    #mouse close
    win.getMouse()
    win.close()
    








valentineGreeting()
