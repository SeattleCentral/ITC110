import time
from random import randint

from graphics import GraphWin, Circle, Point, Text

win = GraphWin("SNOW")
win.setBackground("blue")

# Draw 75 snowballs
snowballs = []
num_snowballs = 75
for i in range(num_snowballs):
    x = randint(0, 199)
    y = randint(0, 199)
    p = Point(x, y)
    snowball = Circle(p, randint(2, 3))
    snowball.setFill("white")
    snowball.draw(win)
    snowballs.append(snowball)

# Freeze between frames in seconds
animation_delay = 0.1

frames_to_render = 20
for i in range(frames_to_render):
    for snowball in snowballs:
        snowball.move(0, randint(1, 3))
        if snowball.getCenter().getY() > 199:
            snowball.undraw()
            snowball.move(0, -200)
            snowball.draw(win)
    # time.sleep(animation_delay)

label = Text(Point(99, 99), "Happy SNOW DAY!")
label.setFill("white")
label.setSize(18)
label.draw(win)

win.getMouse()
win.close()
