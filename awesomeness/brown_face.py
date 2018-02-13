
from graphics import *
import random

win =  GraphWin("Meh Faces", width=500, height=500)

message = Text(Point(250, 465), "Click Anywhere On The Screen")
message.setFace("courier")
message.setSize(18)
message.setTextColor('maroon')

message.draw(win)

for i in range(100):

    click = win.getMouse()
    center = Point(click.getX(), click.getY())

    color1 = random.randint(1, 255)
    color2 = random.randint(1, 255)
    color3 = random.randint(1, 255)

    face = Circle(center, 50)
    face.draw(win)
    face.setFill(color_rgb(color1, color2, color3))
    face.setOutline(color_rgb(color1, color2, color3))

    eyeRight = Circle(Point(center.getX() + 20, center.getY() - 11), 5)
    eyeRight.draw(win)
    eyeRight.setFill('black')

    eyeLeft = eyeRight.clone()
    eyeLeft.move(-40, 0)
    eyeLeft.draw(win)
    eyeLeft.setFill('black')

    mouth = Line(Point(center.getX() - 13, center.getY() + 23), Point(center.getX() + 25, center.getY() + 15))
    mouth.draw(win)

    mouth2 = mouth.clone()
    mouth2.move(0, -1)
    mouth2.draw(win)

    mouth3 = mouth.clone()
    mouth3.move(0, -2)
    mouth3.draw(win)
