# Notes from February 22nd 2017
“For S3, we believe we understand root cause and are working hard at repairing. Future updates across all services will be on dashboard.” 

<cite>- @awscloud (During massive 4 hour outage) </cite>

## Decision Structures
>Statements that allow a program to execute different sequences of instructions for different cases, allowing the program to “choose” an appropriate course of action.

## Two-way Decisions

You can control the flow of program execution based on a two-way decisision using Python's `if`/`else` statements.

Basic sytax

    if <condition>:
        # Do stuff...
    else:
        # Do other stuff...

The condition itself can be any valid Python statement that evaluates to "True" or "False."

Example

    if fahrenheit < 32:
        print("It's freezing outside! Stay indoors.")
    else:
        print("Have fun in the sun!")


## Multi-way Decisions

While you can make multi-way decisions by nesting multiplie `if/else` statements inside of each other, this is generally considered bad practice. Fortunately, Python provides a solution. Use `elif`, as in "else if", to make decisions with multiple possible cases.

Example (Good Practice)

    if fahrenheit > 90:
        print("It's way too hot outside, stay indoors and eat ice cream")
    elif fahrenheit < 32:
        print("It's freezing outside! Stay indoors.")
    elif fahrenheit < 45:
        print("It's kind of cold, but okay.")
    else:
        print("It's fine outside.")

Bad Practice Version

    # Bad Practie: nested else's and if's
    if fahrenheit > 90:
        print("It's way too hot outside, stay indoors and eat ice cream")
    else:
        if fahrenheit < 32:
            print("It's freezing outside! Stay indoors.")
        else:
            if fahrenheit < 45:
                print("It's kind of cold, but okay.")
            else:
                print("It's fine outside.")

## Relation Operators

Python has several built-in *relational operators* that let you compare values. Here is a list of some useful ones:

* `<` - Less than
* `>` - Greater than
* `<=` - Less than or equal to
* `>=` - Greater than or equal to
* `==` - Equal to
* `!=` - Not equal to

## Et Cetera
* Slides for [Chapter 07](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter07.pptx)
* Examples for [Lecture 12](../examples/lecture12.py) [Lecture 12a](../examples/lecture12a.py) [Lecture 12b](../examples/lecture12b.py) [Lecture 12c](../examples/lecture12c.py)
* Why does Python not have `switch/case` statements? [Blog by Pydanny](https://www.pydanny.com/why-doesnt-python-have-switch-case.html)
* Want to learn more about programming at a lower level? [The C Programming Langauge](https://www.amazon.com/Programming-Language-Brian-W-Kernighan/dp/0131103628)
* Python and the Principle of Least Astonishment: [Blog Post](http://lucumr.pocoo.org/2011/7/9/python-and-pola/)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)