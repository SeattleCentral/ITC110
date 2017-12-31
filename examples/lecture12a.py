# Celsius to Fahrenheit
def is_it_safe(celsius):
    celsius = float(celsius)

    fahrenheit = 32 + 9 / 5 * celsius

    if fahrenheit > 90:
        # >= greater than or equal too
        # == is equal to
        print("It's way too hot outside, stay indoors and eat ice cream")
    if fahrenheit < 32:
        print("It's freezing outside! Stay indoors.")

    # Will print no matter what when function is called.
    print("Hi, there, my name is Flow.")


print("Is it safe to go outside?")
print("=========================")
celsius = input("What's the temperature in Celsius? ")
is_it_safe(celsius)
print()
