<!-- # Notes from March 1st 2017
“To err is human; To really foul things up requires a computer.” 

<cite>- Uncertain</cite>

## Exception Handling
>The process of responding to errors, often changing the flow of program execution.

In Python, we use `try/except` blocks to handle errors. For example, say we want to convert some user input to a float, but we know the user may type in non-numeric data.

Example:

    try:
        user_input = input("Enter a number: ")
        float_value = float(user_input)
        print ("The square of your number is:", float_value ** 2)
    except:
        print ("You did not enter a valid number.")


The above example "catches" the error when a user types in a bunch of letters,
such as "banana". It then goes into the `except` block, skipping the rest of 
the `try` block that occurs after the error. 

## Exception Types

There are multiple different exception types. You may have noticed different error codes while developing your programs.

This line of code:

    float_value = float('banana')

Will produce a `ValueError`. You can "catch" specific error cases in your `except` block. 

Example:

	try:
        user_input = input("Enter a number: ")
        float_value = float(user_input)
        print ("The square of your number is:", float_value ** 2)
	except ValueError as error:
        print("Message: ", error, "\n")
        
        
This syntax also allows you to capture the error message itself `as error` and print it later.


## Et Cetera
* Slides for [Chapter 07](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter07.pptx)
* Slides for [Chapter 08](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter08.pptx)
* Examples for [Lecture 13](../examples/lecture13.py) [Lecture 13a](../examples/lecture13a.py)
* List of Python, built-in [Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)
 -->