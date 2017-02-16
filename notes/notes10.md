# Notes from February 13th 2017
“Funny, but it does seem right!  Barry, go for it...” 

<cite>- Guido van Rossum, *comment while making the .join() method decision*</cite>

## Lists vs Strings
>In Python, a `String` is a sequence of characters, but a `List` is a sequence of
>*arbitrary* values.

## Mutable
>Means that it ***can*** be changed.

Lists are *mutable* because you can add, remove, and change the values inside a List without creating a new one. Stings are not mutable, or *immutable*, because they cannot change—they must be recreated.

## Lists and Strings are Objects

Lists and Strings in Python are implemented as *objects*. This allows them to have their own utility methods.

Examples

    my_string = "Hello, Bob"

    print(my_string.lower())
    # Prints "hello, bob"

    my_string.split(', ')
    # Creates a List ["Hello", "Bob"]


    my_list = ["Jan", "Feb", "Mar"]

    my_list.append("Apr")
    # Changes `my_list` to ["Jan", "Feb", "Mar", "Apr"]


## Cryptography and Encoding
>The process of encoding information for the purpose of keeping it secret or transmitting it privately is called ***encryption.***
>
>***Cryptography*** is the study of encryption methods.

Character encoding/decoding in Python.

`ord()` — Accepts a single character and returns its numerical (or ordinal) representation.

`chr()` — Accepts an integer and returns the character represented by it.

See [lecture10.py](../examples/lecture10.py) for an example of using `ord()` and `chr()` to create a pair of encoder and decoder functions.

## Python's `.join()` Method
In order to join a List of values into a single `String`, you may use 
the `.join()` method, which does ***not*** belong to the `List` object—it belongs
to a `String`.

Example

    word_list = ["I", "am", "a", "list", "of", "words"]

    new_string = " ".join(word_list)
    #             ^ Note: this is the separator string.

    print(new_string)
    # Prints "I am a list of words"

A full discussion on why the `.join()` method belongs to the String instead of the 
List object can be found in [this blog post.](http://lucumr.pocoo.org/2011/7/9/python-and-pola/#seemingly-inverse-logic)

## Et Cetera
* Slides for [Chapter 05](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter05.pptx)
* Examples for [Lecture 10](../examples/lecture10.py)
* Python and the Principle of Least Astonishment: [Blog Post](http://lucumr.pocoo.org/2011/7/9/python-and-pola/)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)