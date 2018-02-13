from graphics import *

win = GraphWin("Meh face", 1500, 1000)

top_left = Point(0, 0)
bottom_right = Point(1500, 1000)
rectangle = Rectangle(top_left, bottom_right)
rectangle.setFill('Black')
rectangle.draw(win)

center = Point(750, 500)
circle = Circle(center, 200)
circle.setFill('Yellow')
circle.draw(win)

center = Point(680, 440)
leftEye = Circle(center, 45)
leftEye.setOutline('Black')
leftEye.setWidth(5)
leftEye.setFill('Yellow')
leftEye.draw(win)

rightEye = leftEye.clone()
rightEye.move(140,0)
rightEye.draw(win)

center = Point(698, 418)
leftPupil = Circle(center, 10)
leftPupil.setFill('Black')
leftPupil.draw(win)

rightPupil = leftPupil.clone()
rightPupil.move(140,0)
rightPupil.draw(win)

point_a = Point(635, 365)
point_b = Point(725, 380)
lineLeft = Line(point_a, point_b)
lineLeft.setWidth(7)
lineLeft.draw(win)

lineRight = lineLeft.clone()
lineRight.move(140,0)
lineRight.draw(win)

point_a = Point(635, 600)
point_b = Point(865, 540)
line = Line(point_a, point_b)
line.setWidth(9)
line.draw(win)

point_a = Point(460, 650)
point_b = Point(560, 650)
linea = Line(point_a, point_b)
linea.setFill('White')
linea.setWidth(9)
linea.draw(win)

point_a = Point(445, 635)
point_b = Point(400, 435)
lineb = Line(point_a, point_b)
lineb.setFill('White')
lineb.setWidth(9)
lineb.draw(win)

point_a = Point(285, 400)
point_b = Point(385, 420)
lineb = Line(point_a, point_b)
lineb.setFill('White')
lineb.setWidth(9)
lineb.draw(win)

lined = linea.clone()
lined.move(480,0)
lined.draw(win)

point_a = Point(1055, 635)
point_b = Point(1100, 435)
linee = Line(point_a, point_b)
linee.setFill('White')
linee.setWidth(9)
linee.draw(win)

point_a = Point(1215, 400)
point_b = Point(1115, 420)
linef = Line(point_a, point_b)
linef.setFill('White')
linef.setWidth(9)
linef.draw(win)

text = Text(Point(750, 750), "Meh...")
text.setFill('White')
text.setSize(30)
text.draw(win)

text = Text(Point(750, 950), "CLICK ANYWHERE ON THE SCREEN TO CLOSE")
text.setFill('White')
text.setSize(8)
text.draw(win)


win.getMouse()
win.close()
