# Notes from January 22nd 2017
"I have always wished for my computer to be as easy to use as my telephone; my wish has come true because I can no longer figure out how to use my telephone."

<cite>- Bjarne Stroustrup *(Inventor of the C++ Programming Language)*</cite>

## Library
>Is a module that contains some useful definitions. For example: it could simply be a file filled with useful function definitions.

Example use of the built-in `math` library:

    import math

    square_root = math.sqrt(9)
    print(square_root)
    # Prints 3
    
## Decimal
>An alternate number type that accurately tracks decimal places. It has a lot of overhead when performing calculations because of the extra internal processing required (unlike `float` or `int`).

Example importing and using a Decimal:

    from decimal import Decimal
    
    principle = Decimal('100.00')
    rate = Decimal('0.0299')
    
    after_one_year = principle + principle * rate
    print(after_one_year)
    # Prints 102.990000

## Integer and Float Operations
When mixing different numerical types in mathematical operations, Python will try to convert the numbers types in a way that makes sense.

So when multiplying an integer by a float, Python will convert the integer to a float. (As opposed to the other way around, which would cause a "loss of information").

	my_int = int(5)
	my_float = float(3.67)
	
	print(my_int * my_float)
	#      ^ this gets converted to a float
	# Prints 18.35

## Et Cetera
* Slides for [Chapter 03](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter03.pptx)
* Slides for [Chapter 04](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter04.pptx)
* Examples for [Lecture 05](../examples/lecture05.py)
* The graphics.py [file download](https://canvas.seattlecentral.edu/courses/1411133/files/76130838/download?wrap=1) for Chapter 04
* Repl.it Development Environment: [https://repl.it](https://repl.it/)