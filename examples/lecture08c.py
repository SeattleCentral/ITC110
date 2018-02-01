from graphics import *

# Create window object
win = GraphWin()

for i in range(10):
    point = win.getMouse()
    key = win.getKey()
    label = Text(point, key)
    label.draw(win)
