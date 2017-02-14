# Create an empty GUI window based on the graphics.py file we downloaded from canvas

# Import the graphics.py module
from graphics import *

# Open a graphics window
win = GraphWin("Meh Face", 300, 300)
win.setBackground('black')

# Describe an oval for the face
face = Oval(Point(30, 15), Point(170, 185))
face.setFill('lightblue')
face.setOutline('green')
face.setWidth(4)

# Describe the left eye and clone it for the right eye
leftEye = Oval(Point(50, 60), Point(90, 80))
leftEye.setFill('white')
leftEye.setOutline('black')
leftEye.setWidth(2)
rightEye = leftEye.clone() #rightEye is an exact copy of the left
rightEye.move(60,0)

# Describe pupils for the eyes
leftPupil = Circle(Point(65, 73), 6)
leftPupil.setFill('red')
leftPupil.setWidth(0)
rightPupil = Circle(Point(140, 68), 6)
rightPupil.setFill('orange')
rightPupil.setWidth(0)

# Describe the nose
nose1 = Line(Point(95, 95), Point(95, 105))
nose1.setWidth(3)
nose1.setFill ('blue')
nose2 = Line(Point(94, 105), Point(107, 105))
nose2.setWidth(3)
nose2.setFill ('blue')
nose3 = nose1.clone() #right side of nose is an exact copy of left side of nose
nose3.move(10,0)

# Describe the mouth

# Straight Mouth
# mouth = Line(Point(50, 130), Point(150, 130))
# mouth.setWidth(5)
# mouth.setFill('purple')

# Squiggle Mouth
mouth1 = Line (Point(90, 130), Point(100, 140))
mouth1.setWidth(2)
mouth1.setFill('purple')
mouth2 = Line (Point(100, 140), Point(110, 130))
mouth2.setWidth(2)
mouth2.setFill('purple')
mouth3 = mouth1.clone()
mouth3.move(20, 0)
mouth5 = mouth1.clone()
mouth5.move(40, 0)
mouth4 = mouth2.clone()
mouth4.move(-20, 0)
mouth6 = mouth2.clone()
mouth6.move(-40, 0)
mouth7 = mouth1.clone()
mouth7.move(-20,0)
mouth8 = mouth2.clone()
mouth8.move(20,0)

# Describe speech bubble
speechBubble = Oval(Point(190, 50), Point(290, 120))
speechBubble.setFill('white')
speechBubble.setWidth(0)
speechArrow = Polygon(Point(195, 95), Point(170, 130), Point(210,110))
speechArrow.setWidth(0)
speechArrow.setOutline('white')
speechArrow.setFill('white')

# speechText = Text(Point(240, 85), "MEH!")
outputText = Text(Point(240, 85), "")

# Speech input field
promptText = Text(Point(100, 220), "What should I say?")
promptText.draw(win)
promptText.setFill('white')
inputText = Entry(Point(240, 220), 8)
inputText.setText("MEH!")
inputText.draw(win)
instructText = Text(Point(150, 270), "Click anywhere to submit.")
instructText.setFill('white')
instructText.draw(win)

# Draw each part of the face (order matters!)
face.draw(win)
leftEye.draw(win)
rightEye.draw(win)
leftPupil.draw(win)
rightPupil.draw(win)
nose1.draw(win)
nose2.draw(win)
nose3.draw(win)
mouth1.draw(win)
mouth2.draw(win)
mouth3.draw(win)
mouth4.draw(win)
mouth5.draw(win)
mouth6.draw(win)
mouth7.draw(win)
mouth8.draw(win)

# Wait for mouse click
win.getMouse()

# Display speech buble and output (in that order!), and move pupils.
speechBubble.draw(win)
speechArrow.draw(win)
outputText.setText(inputText.getText())
outputText.draw(win)
leftPupil.move(17,0)
rightPupil.move(-20,5)

# Change instructions at bottom
instructText.move(0,100)
instructText2 = Text(Point(150, 270), "Click anywhere to close.")
instructText2.setFill('white')
instructText2.draw(win)

win.getMouse()
