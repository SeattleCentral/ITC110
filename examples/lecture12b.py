# Celsius to Fahrenheit Module
def is_it_safe(celsius):
    celsius = float(celsius)

    fahrenheit = 32 + 9 / 5 * celsius

    if fahrenheit > 90:
        # >= greater than or equal too
        # == is equal to
        print("It's way too hot outside, stay indoors and eat ice cream")
    # Bad Practie: nested else's and if's
    # else:
    #     if fahrenheit < 32:
    #         print("It's freezing outside! Stay indoors.")
    #     else:
    #         if fahrenheit < 45:
    #             print("It's kind of cold, but okay.")
    #         else:
    #             print("It's fine outside.")
    elif fahrenheit < 32:
        print("It's freezing outside! Stay indoors.")
    elif fahrenheit < 45:
        print("It's kind of cold, but okay.")
    else:
        print("It's fine outside.")

    # Will print no matter what when function is called.
    # print("Hi, there, my name is Flow.")


if __name__ == '__main__':
    print("Is it safe to go outside?")
    print("=========================")
    celsius = input("What's the temperature in Celsius? ")
    is_it_safe(celsius)
    print()
