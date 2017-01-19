# Celsius to Fahrenheit
def temp_converter():
    celsius = input("What's the temperature in Celsius? ")
    celsius = float(celsius)

    fahrenheit = 32 + 9/5 * celsius

    print("{0} degrees Celsius is {1} degrees Fahrenheit".format(
            celsius, fahrenheit))

temp_converter()