from graphics import *

def main ():
    
    win = GraphWin("Big Dipper", 500, 500)
    win.setBackground('midnightblue')
	
    Circle1 = Circle(Point(50,140), 5)
    Circle1.setFill('lightblue')
    Circle1.draw(win)
    time.sleep(1)
	
    Circle2 = Circle(Point(170, 170), 5)
    Circle2.setFill('lightblue')
    Circle2.draw(win)
    time.sleep(1)
	
    Circle3 = Circle(Point(220,230),5)
    Circle3.setFill('lightblue')
    Circle3.draw(win)
    time.sleep(1)
	
    Circle4 = Circle(Point(270,260),5)
    Circle4.setFill('lightblue')
    Circle4.draw(win)
    time.sleep(1)
	
    Circle5 = Circle(Point(270,370),5)
    Circle5.setFill('lightblue')
    Circle5.draw(win)
    time.sleep(1)
	
    Circle6 = Circle(Point(400,420),5)
    Circle6.setFill('lightblue')
    Circle6.draw(win)
    time.sleep(1)
	
    Circle7 = Circle(Point(450,310),7)
    Circle7.setFill('lightblue')
    Circle7.draw(win)
    time.sleep(1)
	
    Line1 = Line(Point(50,140), Point(170,170))
    Line1.setFill('deeppink')
    Line1.draw(win)
    time.sleep(1)
	
    Line2 = Line(Point(170,170), Point(220,230))
    Line2.setFill('deeppink')
    Line2.draw(win)
    time.sleep(1)
	
    Line3 = Line(Point(220,230), Point(270,260))
    Line3.setFill('deeppink')
    Line3.draw(win)
    time.sleep(1)
	
    Line4 = Line(Point(270,260), Point(270,370))
    Line4.setFill('deeppink')
    Line4.draw(win)
    time.sleep(1)
	
    Line5 = Line(Point(270,370), Point(400,420))
    Line5.setFill('deeppink')
    Line5.draw(win)
    time.sleep(1)
	
    Line6 = Line(Point(400,420), Point(450,310))
    Line6.setFill('deeppink')
    Line6.draw(win)
    time.sleep(1)
	
    Line7 = Line(Point(450,310), Point(270,260))
    Line7.setFill('deeppink')
    Line7.draw(win)
	
    time.sleep(2)
	
    Circle1.move(0,20)
    Circle2.move(0,20)
    Circle3.move(0,20)
    Circle4.move(0,20)
    Circle5.move(0,20)
    Circle6.move(0,20)
    Circle7.move(0,20)
    Line1.move(0,20)
    Line2.move(0,20)
    Line3.move(0,20)
    Line4.move(0,20)
    Line5.move(0,20)
    Line6.move(0,20)
    Line7.move(0,20)
	
    time.sleep(2)
	
    Circle1.move(0,-120)
    Circle2.move(0,-120)
    Circle3.move(0,-120)
    Circle4.move(0,-120)
    Circle5.move(0,-120)
    Circle6.move(0,-120)
    Circle7.move(0,-120)
    Line1.move(0,-120)
    Line2.move(0,-120)
    Line3.move(0,-120)
    Line4.move(0,-120)
    Line5.move(0,-120)
    Line6.move(0,-120)
    Line7.move(0,-120)
	
    #Wait for mouse click
    win.getMouse()
	
main()
