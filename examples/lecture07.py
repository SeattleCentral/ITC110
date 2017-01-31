# Create an empty window
from graphics import GraphWin, Point, Circle, Line

win = GraphWin()
# win2 = GraphWin()

# class Point(x, y)
circle_center = Point(50, 60)

# class Circle(Point(), radius)
circle = Circle(circle_center, 20)
circle.setFill('red')
circle.draw(win)


# Draw a Line
# class Line(Point(), Point())
a = Point(100, 100)

# Moving a point
# a.move(50, -50)
# a.draw(win)

b = Point(170, 110)

# Accessor methods
print("A's x =", a.getX())
print("B's x =", b.getX())

# What's happening inside the object...
    # def getX(self):
    #     return self.x

# Lines
my_line = Line(a, b)

my_line.draw(win)

# Closes the window programmatically
# win.close()

input()























