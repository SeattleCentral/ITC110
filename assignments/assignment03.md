## Assignment 03
Assigned on: January 25, 2017

Due: January 31, 2017

## Complete The Following

* Read Sections 2.2 through 2.8 and Chapter 3 of Python Programming by John Zelle.
* Perform the Repl.it Assignment 03.

## Description from Repl.it

1. Modify the `grader()` function to calculate your grade based on the number of points available (available\_points) and the number correct (correct\_points). Return a string with the following format: 93.50%

	Note: Use the special `.format()` codes to show two decimal places.

	The special format code is `:.2f`. Where ".2" is the number of decimal places, and "f" stands for "float".

2. Modify the `rounder()` function to convert any float to a whole number (int). Return an integer.


## Example Usage of the `:.2f` Format Specifier:

    print("My grade is {0:.2f}%".format(93.33333333333333333))

    # Prints "My grade is 93.33%"


## Example Rounder Usage

    whole_number = rounder(93.333333)
    print(whole_number)
    # Prints 93

## Code Repl.it

    # 1. Calculate your letter grade.
    # Return your grade as a string with 2 decimal places!!
    # Formula:
    # 12 points correct / 15 points available * 100% = 80.00%

    def grader(available_points, correct_points):
        # Logic code here...
        return grade

    # Test
    # print(grader(15, 12))


    # 2. Modify the rounder() function to round any float to an integer.
    # Make sure you *return* a whole number.

    def rounder(number):
        # Logic code here...
        return whole_number
        
    # Test
    # print(rounder(33.33333))

