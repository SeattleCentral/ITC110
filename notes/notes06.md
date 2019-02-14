# Notes from January 28th 2019
"See, you not only have to be a good coder to create a system like Linux, you have to be a sneaky bastard too ;-)"

<cite>- Linus Torvalds *(Creator of the Linux Operating System)*</cite>

## GUI
>Graphical User Interface. The part of an application that provide windows, icons, buttons, and menus.

## Importing graphics.py
You need to import graphics.py to run the GUI exercises. The simplest way to make importing work is to place a copy of `graphics.py` in the folder you will be working out of.

The following are different methods to import functionality from the graphics.py library:

**Import module**

    import graphics
    
    # Example Usage:
    win = graphics.GraphWin()

**Import "all"**

    from graphics import *
    
    # Example Usage:
    win = GraphWin()

**Import only "what you need"**

    from graphics import GraphWin
    
    # Example Usage:
    win = GraphWin()
    
Note: you can also import select items using a comma-separated list.

    # from graphics import GraphWin, Circle, Point
    

## Et Cetera
* Slides for [Chapter 04](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter04.pptx)
* Examples for [Lecture 06](../examples/lecture06.py)
* The graphics.py [file download](https://canvas.seattlecentral.edu/courses/1411133/files/76130838/download?wrap=1) for Chapter 04
* Repl.it Development Environment: [https://repl.it](https://repl.it/)
