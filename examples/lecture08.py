from graphics import *

# Create window object
win = GraphWin()

# Capture mouse click "event"
clicked_point = win.getMouse()

print("You clicked at x={0}, y={1}.".format(
        clicked_point.getX(), clicked_point.getY()
    ))