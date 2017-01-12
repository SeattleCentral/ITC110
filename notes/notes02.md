# Notes from January 9th 2017
The term *architecture* is tossed around now in software. I'm not sure how it applies.

<cite>- Robert N. Britcher, *The Limits of Software*</cite>

## Functions
> Used to execute several statements together that solve a common problem

### Exmaple
    def main():
        name = input("What is your name? ")
        print("Hello, {}! How are you today?".format(name))
        
*Note: `.format()` is a special Python* **function** *that replaces one or more pairs of curly braces {} with one or more values. It only works when added to a string.*
        
Cal the function with
    
    main()
    
Run your program on the command prompt by first navigating to the directory, then typing

    python <filename.py>
    
Some students may have to type **python3**.
 
## Variables
> Temporarily store data or information and attach a *label* or *name* to it.

### Exmaples
    name = input("What is your name? ")
    my_favorite_number = 42

You can reference or use these variables later.

    print(my_favorite_number)
    # Prints: 42

## Et Cetera
* Slides for [Chapter 01](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter01.pptx)
* Slides for [Chapter 02](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter02.pptx)
* Examples for [Lecture 02](../examples/lecture02.py)
* If you could not login with your first initial and last name, then contact Lisa Sandoval.
* Download [Python](https://www.python.org)
* Download [Atom](https://atom.io) 