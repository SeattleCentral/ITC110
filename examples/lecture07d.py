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
    x = getClosestGridCoord(point.getX())
    y = getClosestGridCoord(point.getY())

    return Point(x, y)


def getClosestGridCoord(value):
    value = int(value)
    return value - (value % 10


if __name__ == '__main__':
    main()
