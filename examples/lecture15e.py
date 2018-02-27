
def main():
    """
    This reads the file lecture15e.txt,
    and parses the data to average it.
    """
    data_file = open('lecture15e.txt', 'r')
    sum_of_values = 0.0
    count = 0

    for line in data_file:
        print ('line of file =', line)
        sum_of_values = sum_of_values + float(line)
        count += 1

    print("The average of {0} values is {1}".format(
        count,
        sum_of_values / count))


if __name__ == '__main__':
    main()
