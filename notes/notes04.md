# Notes from January 17th 2017
"Programmers will always make errors. No advance in formal languages will once and for all prevail over human fallibility.”

<cite>- Robert N. Britcher, *The Limits of Software*</cite>

## Literal
> A literal is a representation of a specific value, for example `3` is a literal representation of the whole number three.

## Variable
> A variable is an identifier that stores a value. For example, the variable `my_number` stores the value three.

    my_number = 3
    
## Operators
> Operators are used to combine expressions. We commonly use mathematical operators to perform calculations. Here are some example *operators*:

    * / + - %  **

## Lists
> A list is a data type that allows grouping multiple, ordered pieces of data. For example, here is a list of numbers from 1 to 5:

    my_list = [1, 2, 3, 4, 5]

We use square brackets `[]` to denote the start and end of a list, and each item is separated by a comma.

## For Loop
The chaos function used a `for` loop in conjunction with the `range()` function. We can also use a `for` loop with a custom list.

Example:

    for x in [1, 2, 3, 4, 5]:
        print(x)

Prints<br>
1<br>
2<br>
3<br>
4<br>
5<br>

## Type
You can get the ***type*** of a variable or literal using the built-in `type()` function

Examples:

    >>> my_number = 13
    >>> type(my_number)
    <class 'int'>
    
    >>> type (13)
    <class 'int'>
    
    >>> type("I have quotes!")
    <class 'str'>
    
    >>> type (86.66666)
    <class 'float'>

# Number Types

## Integer
The integer number type includes whole numbers (no decimal part). You can force an integer number type with `int()`. These take up far less memory than other number types.

## Float
The float number type supports a decimal, or *fractional* component. For example: `3.333`. Because a computer cannot natively store partial numbers, it uses an approximation scheme to represent the fractional component, which is not always accurate. You can force a float number type with `float()`.

## Et Cetera
* Slides for [Chapter 03](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter03.pptx)
* Examples for [Lecture 04](../examples/lecture04.py)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)