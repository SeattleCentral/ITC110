
def main():
    """
    This is a mult-line string...and a comment because it's discarded by
    the interpreter
    ====================================================================
    * Point 1
    * Point 2

    This function averages a list of numbers of unknown length.
    The user types 'q' to quit.
    """

    sum_of_values = 0.0
    count = 0

    x = input('Enter the next number in list to average. ("q" to exit) ')
    while 'q' not in x.lower():
        print ('x =', x)
        sum_of_values = sum_of_values + float(x)
        count += 1
        x = input('Enter number in list to avg. ("q" to exit) ')

    print("The average of {0} values is {1}".format(
        count,
        sum_of_values / count))


if __name__ == '__main__':
    main()
