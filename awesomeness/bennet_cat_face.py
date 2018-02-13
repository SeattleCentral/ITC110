from graphics import *
def main():
    win = GraphWin("Cat",500,500)

    win.setBackground(color_rgb(140,247,242))
    fur = color_rgb(242, 183, 82)

    #Cat head
    cathead = Circle(Point(250,250), 125)
    cathead.setFill(fur)
    cathead.setOutline(fur)
    cathead.draw(win)

    #cat eyes

    righteye = Circle(Point(318,245), 20)
    righteye.setFill("black")
    righteye.draw(win)

    lefteye = Circle(Point(177,243), 20)
    lefteye.setFill("black")
    lefteye.draw(win)

    #cat ears
    leftear = Polygon(Point(125,97), Point(230,131), Point(140,206))
    leftear.setFill(fur)
    leftear.setOutline(fur)
    leftear.draw(win)

    leftear = Polygon(Point(371,97), Point(287,131), Point(361,206))
    leftear.setFill(fur)
    leftear.setOutline(fur)
    leftear.draw(win)

    #catnose

    nose = Polygon(Point(229,281), Point(254,281), Point(242,298))
    nose.setFill(color_rgb(245,173,255))
    nose.setOutline(color_rgb(245,173,255))
    nose.draw(win)

    #mouth

    mouth= Line(Point(205,330), Point(285,312))
    mouth.draw(win)
    #close window

    print ("Click to quit")
    win.getMouse()
    win.close()

main()
