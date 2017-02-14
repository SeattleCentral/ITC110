from graphics import *

def main():
    win = GraphWin("Moving Circle")

    circle = Circle(Point(75, 75), 25)
    circle.draw(win)

    win.getMouse() # Pause between each frame

    circle.move(0, 50)

    win.getMouse() # Pause between each frame

    circle.move(50, 0)

    win.getMouse() # Pause between each frame

    circle.move(0, -50)

    win.getMouse() # Pause between each frame

    circle.move(-50, 0)

main()

win.getMouse()