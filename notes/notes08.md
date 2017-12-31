<!-- # Notes from February 1st 2017
“One of the more common motivations for writing comments is bad code. We write a module and we know it is confusing and disorganizd. We know it's a mess. So we say to ourselves, *"Ooh, I'd better comment that!"* No! You'd better clean it!” 

<cite>- Rober C. Martin, *Clean Code*</cite>

## Using The Graphics Library
In this lecture, we delved into using the graphics.py library to write some potentially useful GUI applications.

We started off by writing a windowed app that captures the "click" ***event*** of the mouse and stores the value that the *event* returns. In our graphics library, it returns a `Point` object. We then printed out the X and Y coordinates using the `.getX()` and `.getY()` methods of the `Point` instance.

	from graphics import *
	
	# Create window object
	win = GraphWin()
	
	# Capture mouse click "event"
	clicked_point = win.getMouse()
	
	print("You clicked at x={0}, y={1}.".format(
	        clicked_point.getX(), clicked_point.getY()
	    ))

Code listing: [lecture08.py](../examples/lecture08.py)



## Event-driven Programming
>Draws interface elements (widgets) on the screen and then waits for the user to do something.

## Event
>Is an object that encapsulates information about what just happened. It is generated whenever a user moves the mouse, clicks the mouse, or types a key on the keyboard.

We then moved on to capturing multiple mouse click *events* in series to draw a triangle using the `Polygon` class in graphics.py. Code listing: [lecture08a.py](../examples/lecture08a.py)

Finally, we mixed GUI *event-driven* programming with traditional programming logic to create a celsius-to-fahrenheit converter application. Code listing: [lecture08b.py](../examples/lecture08b.py)

## Building a GUI App
*For informational purposes only.* You can wrap up your GUI python file(s) and include the Python interpreter into a single, executable program using [PyInstaller](https://pythonhosted.org/PyInstaller/). Note: you must build the app on the target system. (So, to build a MacOS app, you'd have to run the PyInstaller commands on a MacOS computer).

Example usage with an icon image file:

    pyinstaller --onefile --windowed -i icon.ico main.py

## Strings and Lists
A string is a sequence of characters. Literally. Therefore, the string:<br>
`"Hello, Bob."`<br>
Is represented internally as:<br>
`['H', 'e', 'l', 'l', 'o', ',', ' ', 'B', 'o', 'b', '.']`<br>
This means we can loop over the characters of a string the same way we loop over a `range()` of numbers. It also means we can access characters by their ***index***.

Example:
    
    my_string = "Hello, Bob."
    print(my_string[7])
    # Prints 'B' because that is the 7th index (starting with 0)


## Et Cetera
* Slides for [Chapter 04](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter04.pptx)
* Slides for [Chapter 05](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter05.pptx)
* Examples for [Lecture 08](../examples/lecture08.py) [Lecture 08a](../examples/lecture08a.py) [Lecture 08b](../examples/lecture08b.py)
* Open-source, production GUI library for Python: [PySide](https://wiki.qt.io/PySide)
* GPL, production GUI library for Python: [PyQt](https://riverbankcomputing.com/software/pyqt/intro)
* Package GUI apps with [PyInstaller](https://pythonhosted.org/PyInstaller/)
* The graphics.py [file download](https://canvas.seattlecentral.edu/courses/1411133/files/76130838/download?wrap=1) for Chapter 04
* Repl.it Development Environment: [https://repl.it](https://repl.it/) -->