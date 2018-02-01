# This program draws a user's traiangle.
from graphics import GraphWin, Point, Rectangle, color_rgb
import random

win = GraphWin("Paint a Mosaic", width=400, height=400)

win.setCoords(0.0, 0.0, 100, 100)


for i in range(100):
    point = win.getMouse()
    topLeft = Point(point.getX() - 5, point.getY() - 5)
    bottomRight = Point(point.getX() + 5, point.getY() + 5)
    rectangle = Rectangle(topLeft, bottomRight)

    red = random.randint(1, 255)
    green = random.randint(1, 255)
    blue = random.randint(1, 255)

    color = color_rgb(red, green, blue)

    # Hexadecimal method
    # color = "#{0:06x}".format(random.randint(0, 0xFFFFFF))

    rectangle.setFill(color)

    rectangle.draw(win)


input("Press enter to close")
