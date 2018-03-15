# Notes from February 28th 2018
"Whoever stole my copy of Microsoft Office...I will find you. You have my Word."

<cite>- Unknown</cite>


## Boolean Operators
The Boolean operators `and` and `or` are used to combine two Boolean expressions and produce a Boolean result.

Example:

    if a > 10 and a < 20:
        print ("a is between 10 and 20")

## Truth Tables
In a truth table, *P* and *Q* represent smaller Boolean expressions.

The last column gives the value of *P* and *Q* for each possible combination.
        
## `and` Truth Table

| P | Q | P and Q |
|---|---|---------|
| T | T |    T    |
| T | F |    F    |
| F | T |    F    |
| F | F |    F    |

## `or` Truth Table

| P | Q |  P or Q |
|---|---|---------|
| T | T |    T    |
| T | F |    T    |
| F | T |    T    |
| F | F |    F    |

## `not` Truth Table
Note: `not` is a *unary* Boolean operator

| P | not P |
|---|-------|
| T |   F   |
| F |   T   |

## Event Loop
>A type of loop that continually tests for external events (like GUI actions) and calls the appropriate functions to handle them.

Example:

	from graphics import *
	
	def handle_key(key, win):
	    if key == 'r':
	        win.setBackground('pink')
	    elif key == 'w':
	        win.setBackground('white')
	    elif key == 'g':
	        win.setBackground('green')    
	    elif key == 'b':
	        win.setBackground('lightblue')
	
	win = GraphWin('Click and Type', 500, 500)
	
	# Event Loop
   	while True:
        key = win.checkKey()
        if key == 'q':
            break
	
        if key:
            handle_key(key, win)
	
	win.close()
	
## Review of Objects
See [Example 15c](../examples/lecture15c.py)

For an in-depth look at Python's unique way of defining object attributes, take at look at [this blog post.](https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
)


## Et Cetera
* Slides for [Chapter 08](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter08.pptx)
* Slides for [Chapter 10](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter10.pptx)
* Examples for [Lecture 15](../examples/lecture15.py) [Lecture 15a](../examples/lecture15a.py) [Lecture 15b](../examples/lecture15b.py) [Lecture 15c](../examples/lecture15c.py)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)