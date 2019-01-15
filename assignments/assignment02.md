## Assignment 02
Assigned on: January 14, 2019

Due: January 21, 2019

## Complete The Following

* Perform the Repl.it Assignment 02.

## Description from Repl.it

### 1. Modify the greeter function to print out the message:
"Hello, <name>. How are you today?"

Where `<name>` will be replaced by the "name" parameter when the function is called.

Example of calling the function:

    greeter("Bob")

    # Prints: "Hello, Bob. How are you today?"



### 2. You are designing a modular bathroom with European designers, but the builders don't use the metric system. Modify the converter function so that it accepts short distance values in metric (centimeters) and converts it to inches.

Example of calling the function:

    converter(10)

    # returns 3.937....

Note: You MUST convert input to a number type (e.g. "float") inside the function definition

Further note: This function does not PRINT  the result. It RETURN's it.

## Code

    # 1.
    def greeter(name):
        # Add code here that will print out "Hello, Bob. How are you today?" when name = "Bob"
        # ...

    # Test
    # greeter("Bob")

    # 2. 
    def converter(metric_input):
        # Add code here that will convert metric_input from centimeters to inches and RETURN it.
        # ...
        return inches
        
    # Test
    # metric_input = input("Value in centimeters? ")
    # print(converter(metric_input))
