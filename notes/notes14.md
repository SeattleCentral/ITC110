# Notes from March 6th 2017
"Success these days is a relative term. Some products and systems get by simply because a very small portion of them are used. Adn then there are the help desks used by the commercial software houses. Staffing them must be cheaper than testing. As for the Apollo and Shuttle space projects, the management plan did not call for help desks."

<cite>- Robert N. Britcher, *The Limits of Software*</cite>

# Definite Loop
The `for` loop is a *definite loop* because the number of iterations is determined when the loop starts.

For example:

    for i in range(10):
        print(i)

It is known at the beginning that the loop will iterate 10 times (0 through 9).

# Indefinite Loop
>A loop that iterates until certain conditions are met. Also called a *conditional loop.*

Example:

    while raining:
        print("Wear an umbrella") # If this sounds odd, that's because it is.

The above loop may iterate indefinitely, but will hopefully stop around June. ;-)

The synaxa for a `while` loop is:

    while <condition>:
        <body>

Where `condition` is a Boolean expression, just like with `if` statements.


## Sentinel Loop
>A loop that continues to process data until reaching a special value that signals the end.

Example:

    sum = 0
    count = 0

    value = float(input("Enter a grade (negative value to stop): "))
    while value >= 0:
        sum += value
        count += 1
        value = float(input("Enter a grade (negative value to stop): "))

    print("The average grade is {0}.".format(sum / count))

This sentinel loop will execute until the user types a special value of any negative number.


## Et Cetera
* Slides for [Chapter 08](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter08.pptx)
* Slides for [Chapter 10](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter10.pptx)
* Examples for [Lecture 14](../examples/lecture14.py) [Lecture 14a](../examples/lecture14a.py) [Lecture 14b](../examples/lecture14b.py) [Lecture 14c](../examples/lecture14c.py) [Lecture 14d](../examples/lecture14d.py) [Lecture 14e](../examples/lecture14e.py)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)