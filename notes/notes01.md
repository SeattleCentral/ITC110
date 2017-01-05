# Notes from January 4th 2017
Be mindful of these tidbits of information. They may become quiz questions. Which leads to test questions. Which leads to suffering...

<cite>- Yoda</cite>

## Fundamentals

### Universal Machine
> A machine that stores and manipulates information under the control of a changeable program

### Computer Program
> A detailed, step-by-step set of instructions telling a computer what to do.

### Computer Science
* Asks, "What can be computed?"
* Can be answered by:
	* Design
		* Actually develop the ***algorithm*** to solve the problem
		* Cons - This can never prove what *can't* be designed
	* Analysis
		* Examine algorithms and problems mathematically
		* Pros - determine what is *unsolvable* or impracticle to solve
	* Experimentation
		* For when it's too complex for analysis or direct design

### Hardware Basics
Only important insomuch as you want a general idea how your computer works. Hardware architecture becomes more important in advanced courses where it may affect program design decisions. Python does a really good job of abstracting away our considerations for the underlying hardware.

* Input Devices
	* Information passed into the computer from the "outside"
	* Keyboard, mouse, microphone, sensors
* Output Devices
	* How the computer sends information back to us.
	* Monitor (screen), printer, speakers
* CPU
	* Is the "brain" of the computer
	* Carries out all the basic operations including arithmetic ops
* Memory
	* Main
		* Accessed directly by the CPU and frequently used during program processing
		* Often referred to as "RAM" (Random Access Memory)
		* Normally very fast, but volatile (lost when powered off)
	* Secondary
		* Only accessed for file operations like loading the initial source code file or saving results to a file
		* Hard drive, USB drive, etc.

## Programming Languages

### High-level Computer Languages
> Designed to be more easily understood by humans and then compiled or interpretted for the machine later.

Examples: Python, Java, C++, JavaScript

### Low-level Computer Languages
> Not readily understood by humans. Binary, or *machine language*, that can immediately execute on the machine.

Note: Assembly language is often considerd "low-level" even though it is a slight abstraction on top of binary.

### Compilers
> Convert programs written in a high-level language into the machine language of a particular computer.

### Interpreters
> Simulate or "virtualize" a computer that understands a high-level language directly. It does this by analyzing and ***interpreting*** code and converting it into binary as it's being executed. 


## Python
Is a high-level, interpreted programming language.

Try it!

    >>> print ("Hello, ITC110!!")


## Et Cetera
* Examples for [Lecture 01](../examples/lecture01.py)
* Example of a ["compiled" language (C)](../examples/test.c)
* If you could not login with your first initial and last name, then contact Lisa Sandoval.
* I looked through the 2nd edition of the book, and it appears to follow the same layout. Just a few "older" references that won't make a difference. (E.g. I think it mentions floppy disks as secondary memory, lol).
* Download [Python](https://www.python.org)
* Download [Atom](https://atom.io) 