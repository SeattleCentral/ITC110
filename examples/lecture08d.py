from graphics import *
from converter import temp_convert

# Create window object
win = GraphWin("Celsius Converter", 300, 200)
win.setCoords(0.0, 0.0, 3.0, 4.0)

Text(Point(1, 3), "   Celsius Temperature:").draw(win)
Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)

user_input = Entry(Point(2, 3), 5)
user_input.setText("0.0")
user_input.draw(win)

output = Text(Point(2, 1), "")
output.draw(win)

button = Text(Point(1.5, 2.0), "Convert It!")
button.draw(win)

Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

win.getMouse()

fahr = temp_convert(user_input.getText())
output.setText(fahr)

button.setText("Quit")
win.getMouse()
win.close()
