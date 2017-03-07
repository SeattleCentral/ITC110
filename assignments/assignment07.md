## Assignment 07
Assigned on: March 06, 2017

Due: March 10, 2017

## Complete The Following

* Read Chapter 7 and Chapter 8 through section 8.3 of Python Programming by John Zelle.
* Perform the Repl.it Assignment 07.


## Description from Repl.it
1. Create a function, `letter_grade()`, that accepts a float parameter and returns a single character letter grade based on the following list:

	* 90.0 - 100.0, "A"
	* 80.0 - 89.99, "B"
	* 70.0 - 79.99, "C"
	* 60.0 - 69.99, "D"
	* 59.99 and below, "F"
	
	Example usage of letter_grade()
	
	    print(letter_grade(88.5))
	    # Prints "B"
	
	*Note: I strongly recommend if/elif/else.*

2. Create a function, `safe_letter_grade()`, that behaves exactly as letter_grade() defined above, except allow it to handle non-numeric parameters by attempting to convert any string values to a float. Use a try/except block to handle invalid parameter values. In cases where an invalid value is passed in, return the string message:<br>
**"Please enter a valid number."**
	
	Example usage of safe\_letter\_grade()
	
	    print(safe_letter_grade(88.5))
	    # Prints "B"
	
	    print(safe_letter_grade("88.5"))
	    # Prints "B"
	
	    print(safe_letter_grade("eighty five"))
	    # Prints "Please enter a valid number."