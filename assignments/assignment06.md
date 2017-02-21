## Assignment 06
Assigned on: February 20, 2017

Due: February 27, 2017

## Complete The Following

* Read the rest of Chapter 5 and Chapter 6 of Python Programming by John Zelle.
* Perform the Repl.it Assignment 06.


## Description from Repl.it
1. A Caesar cipher is a simple substitution cipher based on the idea of shifting each letter in a plaintext message by a fixed number (called the key) of positions in the alphabet. For example, a key of 2 would change "Banana" to "Dcpcpc".  The original message can be recovered by "reencoding" it by taking the negative value of the key.

    Write 2 functions, encoder() and decoder(), that take a message and key parameter, and return an encrypted or decrypted message, respectively.

Example:

    print(encoder("Banana", 2))
    # Prints "Dcpcpc"

    print(decoder("Dcpcpc", 2))
    # Prints "Banana"

Note:
Recall that ord() returns an integer value for a character, and chr() returns a character from an integer. 

    print(chr(ord("B") + 2))
    # Prints "D"

{:start="2"}
2. Write a function, word_count(), that returns the number (int) of words in a given sentence (string type). Consider spaces as word separators. 

Example:

    print(word_count("Hello, Ricky Bobby, and that's a nice car"))
    # Prints 8