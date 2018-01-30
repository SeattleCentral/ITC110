# This program draws a user's traiangle.
from graphics import GraphWin, Point, Text, Polygon

win = GraphWin("Draw a Triangle")

win.setCoords(0.0, 0.0, 10.0, 10.0)

textMessage = Text(Point(5, 0.5), "Click on Three Points")
textMessage.draw(win)

point1 = win.getMouse()
point1.draw(win)

point2 = win.getMouse()
point2.draw(win)

point3 = win.getMouse()
point3.draw(win)

triangle = Polygon(point1, point2, point3)
triangle.setFill("peachpuff")
triangle.setOutline("cyan")
triangle.draw(win)


input("Press enter to close")