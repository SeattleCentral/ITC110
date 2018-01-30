# This program draws a user's traiangle.
from graphics import GraphWin, Point, Rectangle
import random


def main():
    win = GraphWin("Paint a Mosaic", width=400, height=400)
    win.setCoords(0.0, 0.0, 100.0, 100.0)

    # This while loop will run indefinitely (Ctrl + C to kill the process)
    while True:
        point = win.getMouse()
        topLeft = getClosestGridVertix(point)
        bottomRight = Point(topLeft.getX() + 10, topLeft.getY() + 10)
        rectangle = Rectangle(topLeft, bottomRight)

        # Randomly set a hexadecimal color as fill.
        color = "#{0:06x}".format(random.randint(0, 0xFFFFFF))
        rectangle.setFill(color)

        rectangle.draw(win)


def getClosestGridVertix(point):
    # Find nearest upper left vertix in 10 point grid
    x = int(point.getX())
    while (x % 10) != 0:
        x = x - 1

    y = int(point.getY())
    while (y % 10) != 0:
        y = y - 1

    return Point(x, y)


if __name__ == '__main__':
    main()
