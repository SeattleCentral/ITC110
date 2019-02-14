from graphics import GraphWin, Point, Circle, Polygon, Text


win = GraphWin("Valentine", 600, 600)

left_circle = Circle(Point(200, 200), 100)
left_circle.setFill("red")
left_circle.setOutline("red")
left_circle.draw(win)

right_circle = left_circle.clone()
right_circle.move(200, 0)
right_circle.draw(win)


p1 = Point(110, 245)
p2 = Point(300, 500)
p3 = Point(490, 245)
p4 = Point(300, 200)

bottom = Polygon(p1, p2, p3, p4)
bottom.setFill("red")
bottom.setOutline("red")
bottom.draw(win)

happy = Text(Point(300, 240), "Happy")
happy.setFill("white")
happy.setSize(32)
happy.draw(win)

valentines = Text(Point(300, 280), "Valentine's")
valentines.setFill("white")
valentines.setSize(32)
valentines.draw(win)

day = Text(Point(300, 320), "Day")
day.setFill("white")
day.setSize(32)
day.draw(win)

p = win.getMouse()
win.close()
