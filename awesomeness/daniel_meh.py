from graphics import *

win = GraphWin('Meh')

center = Point(100, 100)
circ = Circle(center, 100)
circ.setFill('yellow')
circ.draw(win)

left_eye = Point(60, 60)
circ = Circle(left_eye, 20)
circ.setFill('black')
circ.draw(win)

right_eye = Point(150, 60)
circ = Circle(right_eye, 20)
circ.setFill('black')
circ.draw(win)

pupil_left = Point(65, 60)
circ = Circle(pupil_left, 5)
circ.setFill('magenta')
circ.draw(win)

pupil_right = Point(155, 60)
circ = Circle(pupil_right, 5)
circ.setFill('gray')
circ.draw(win)

line = Line(Point(160, 160), Point(60, 160))
line.draw(win)


nose = Point(105, 105)
circ = Circle(nose, 10)
circ.setFill('purple')
circ.draw(win)

forehead = Point(20, 15)
label = Text(forehead, "Meh...")
label.draw(win)

input()
