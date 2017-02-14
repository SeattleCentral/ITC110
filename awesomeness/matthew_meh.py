from graphics import *

win = GraphWin()


leftEar = Circle(Point(40, 108), 12)
leftEar.setFill('yellow')
leftEar.draw(win)

rightEar = Circle(Point(160, 108), 12)
rightEar.setFill('yellow')
rightEar.draw(win)

faceOutline = Oval(Point(40, 195), Point(160, 5))
faceOutline.setFill('yellow')
faceOutline.draw(win)

my_leftEyeball = Point(73, 75)
my_rightEyeball = Point(127, 75)
eyeSize = 25
pupilSize = 3

leftEye = Circle(my_leftEyeball, eyeSize)
leftEye.setFill('white')
leftEye.draw(win)

leftPupil = Circle(my_leftEyeball, pupilSize)
leftPupil.setFill('black')
leftPupil.draw(win)

rightEye = Circle(my_rightEyeball, eyeSize)
rightEye.setFill('white')
rightEye.draw(win)

rightPupil = Circle(my_rightEyeball, pupilSize)
rightPupil.setFill('black')
rightPupil.draw(win)

scruff = Oval(Point(50, 170), Point (151, 115))
scruff.setFill('beige')
scruff.draw(win)

mouth1 = Line(Point(60, 144), Point(140, 144))
mouth1.setWidth(2)
mouth1.draw(win)

nose = Circle(Point(100, 105), 10)
nose.setFill('yellow')
nose.draw(win)

hair1 = Line(Point(34, 94), Point(38, 81))
hair1.setWidth(2)
hair1.draw(win)

hair2 = Line(Point(38, 81), Point(42, 94))
hair2.setWidth(2)
hair2.draw(win)

hair3 = Line(Point(200-42, 94), Point(200-38, 81))
hair3.setWidth(2)
hair3.draw(win)

hair4 = Line(Point(200-38, 81), Point(200-34, 94))
hair4.setWidth(2)
hair4.draw(win)


win.getMouse()
win.close()
