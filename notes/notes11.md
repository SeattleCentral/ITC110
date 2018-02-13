# Notes from February 7th 2018 and February 12 2018
“Programmers will always make errors. No advance in formal languages will once and for all prevail over human fallibility.” 

<cite>- Robert N. Britcher (The Limits of Software) </cite>

## File
>A sequence of data that is stored in secondary memory (disk drive or solid state drive).

## File Processing
* All files that are opened must be closed.
* You open a file in different "modes"
* `"r"` is **read** mode
* `"w"` is **write** mode

## Reading file contents
* `<file>.read()` — Returns the entire remaining contents of the file as a single (possibly large, multi-line) string.
* `<file>.readline()` – Returns the next line of the file. This is all text up to and including the next newline character.
* `<file>.readlines()` – Returns a list of the remaining lines in the file. Each list item is a single line including the newline characters.

Example

    # Loop over each line in a text file and print out lines with the word "spy"
    def main():
        file = open('nsa_notes.txt', 'r')

        for line in file.readlines():
            if 'spy' in line:
                print(line)

        file.close()

    main()

## File Dialog with Qt

If you have Python 3 properly installed, then you can install a commercial GUI library,
PyQt5, using **pip.**

`pip install PyQt5`

Then follow this tutorial to demonstrate Qt's GUI for selecting a file.
[https://pythonspot.com/pyqt5-file-dialog/](https://pythonspot.com/pyqt5-file-dialog/)

Example Code: [Lecture 11 File Dialog with PyQt](../examples/lecture11_file_dialog.py)

Unfortunately, PySide—the free alternative to PyQt, does not yet support Python 3.5+

## Function Definition
>The part of the program that creates a function.

## Functions

We write functions for two main reason:

1. Reduce code duplication
2. Make code more modular and easier to read

Example

    def sing_happy_line():
        print("Happy birthday to you.")

    def sing_happy_name(name):
        print("Happy birthday, dear {0}.".format(name))

    def sing_happy_birthday(name):
        sing_happy_line()
        sing_happy_line()
        sing_happy_name(name)
        sing_happy_line()

    name = input("What's your name? ")

    sing_happy_birthday(name)


## Et Cetera
* Slides for [Chapter 05](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter05.pptx)
* Slides for [Chapter 06](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter06.pptx)
* Slides for [Chapter 07](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter07.pptx)
* Examples for [Lecture 11](../examples/lecture11.py) [Lecture 11a](../examples/lecture11a.py) [Lecture 11b](../examples/lecture11b.py) [Lecture 11c](../examples/lecture11c.py) [Lecture 11d](../examples/lecture11d.py) [Lecture 11e](../examples/lecture11e.py)
* Python and the Principle of Least Astonishment: [Blog Post](http://lucumr.pocoo.org/2011/7/9/python-and-pola/)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)