## Assignment 05
Assigned on: February 08, 2017

Due: February 15, 2017

## Complete The Following

* Read the rest of Chapter 4 and Sections 5.1 through 5.7 of Python Programming by John Zelle.
* Perform and upload the following code as a .py file.

## Code Assignment
Using the **graphics.py** library, create a window that opens and shows a simple animation.

You may use your artistic style to animate any object or combination of objects, but the animation must have at least 4 frames.

<u>How do you create an animation?</u>

1. You can create a simple animation using `win.getMouse()`. Remember `.getMouse()` is a blocking method—the app stops executing until the user clicks somewhere in the window. You could use the click event as a signal to move an object (e.g. a `Circle`) drawn on the screen.
2. You can move most objects using the `.move()` method. It accepts accepts two parameters: an X and Y value that denote the number of units to move in the X/Y plane. 

Upload the assignment as a `.py` file to Canvas.

P.s. You can also import the `time` module and use `time.sleep()`<br>
[Python docs - time.sleep](https://docs.python.org/3/library/time.html#time.sleep )