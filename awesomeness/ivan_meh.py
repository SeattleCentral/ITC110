from graphics import *

"""
Note from the Insructor:
========================
Ivan Mwiruki has graciously allowed me to use his "meh" face
application code as an example.
"""


def main():
    win = GraphWin("Meh Face", 500, 500)
    win.setBackground("black")

    face = Circle(Point(250, 200), 150)
    face.setFill("yellow")
    face.draw(win)

    # Note from the Instructor:
    # I like these descriptive variable names!
    # No one has to guess what "leftEye" and "rightEye" represent.
    leftEye = Circle(Point(200, 150), 25)
    leftEye.setFill("black")
    rightEye = leftEye.clone()
    rightEye.move(110, 0)
    leftEye.draw(win)
    rightEye.draw(win)

    smile = Line(Point(170, 270), Point(330, 270))
    smile.setWidth(8)
    smile.draw(win)

    label = Text(Point(250, 400), "Why so serious?")
    label.setFace("helvetica")
    label.setFill("white")
    label.setSize(30)
    label.draw(win)

    win.getMouse()
    win.close()


main()
