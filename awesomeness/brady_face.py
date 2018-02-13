# Assignment:   5(ThomasBradyITC110Assignment4.py)
# Name:         Thomas Brady
# Date:         2/1/18
# Description:  This program imports the graphics library and draws
#               a "meh" face using circles, rectangles, and lines.

from graphics import *

def Meh():

    # Build Graphic Window and set Coordinates
    win = GraphWin("Meh Face!!!!", 500,500)
    win.setBackground("white")
    win.setCoords(0,0,100,100)

    # Draw Head
    circHead = Circle(Point(50,50),37)
    circHead.setFill("white")
    circHead.setWidth(6)
    circHead.draw(win)

    # Draw Left Eye
    circEye1 = Circle(Point(35,60),10)
    circEye1.setWidth(6)
    circEye1.draw(win)

    # Draw Left Eyeball Retina
    circEyeBallOne = Circle(Point(35,60),4)
    circEyeBallOne.setFill("black")
    circEyeBallOne.draw(win)

    # Draw Rectangle to cut Left Retina in half
    circCutRetinaOne = Rectangle(Point(30.9,60),Point(39.1,64.1))
    circCutRetinaOne.setFill("white")
    circCutRetinaOne.setOutline("white")
    circCutRetinaOne.draw(win)

    # Draw Line for Left Eyelid 
    lineEyeLid1 = Line(Point(25,60),Point(45,60))
    lineEyeLid1.setWidth(6)
    lineEyeLid1.draw(win)

    # Draw Right Eye
    circEye2 = Circle(Point(65,60),10)
    circEye2.setWidth(6)
    circEye2.draw(win)

    # Draw Right Eyeball Retina
    circEyeBallTwo = Circle(Point(65,60),4)
    circEyeBallTwo.setFill("black")
    circEyeBallTwo.draw(win)

    # Draw Rectangle to cut Right Retina in half
    circCutRetinaOne = Rectangle(Point(60.9,60),Point(69.1,64.1))
    circCutRetinaOne.setFill("white")
    circCutRetinaOne.setOutline("white")
    circCutRetinaOne.draw(win)
    
    # Draw Line for Right Eyelid    
    lineEyeLid2 = Line(Point(55,60),Point(75,60))
    lineEyeLid2.setWidth(6)
    lineEyeLid2.draw(win)

    # Draw Left Eyebrow
    lineEyeBrowLeft = Line(Point(27,74),Point(43,74))
    lineEyeBrowLeft.setWidth(6)
    lineEyeBrowLeft.draw(win)

    # Draw Right Eyebrow
    lineEyeBrowRight = Line(Point(57,74),Point(73,74))
    lineEyeBrowRight.setWidth(6)
    lineEyeBrowRight.draw(win)

    #Draw Lines for Mouth
    lineMouth1 = Line(Point(50,30),Point(63,36))
    lineMouth1.setWidth(6)
    lineMouth1.draw(win)

    lineMouth2 = Line(Point(62.8,36),Point(71,32))
    lineMouth2.setWidth(6)
    lineMouth2.draw(win)

    lineMouth3 = Line(Point(50.3,30),Point(37,36))
    lineMouth3.setWidth(6)
    lineMouth3.draw(win)
                      
                                                 
    lineMouth4 = Line(Point(37.2,36),Point(29,32))
    lineMouth4.setWidth(6)
    lineMouth4.draw(win)

    # Draw meh. label
    lblMeh = Text(Point(51.5,5),"meh.")
    lblMeh.setTextColor("black")
    lblMeh.setStyle("bold")
    lblMeh.setFace("courier")               
    lblMeh.setSize(35)
    lblMeh.draw(win)
Meh()
input('')
