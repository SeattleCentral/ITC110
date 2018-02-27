
def main():
    """
    This reads the file lecture15e.txt,
    and parses the data to average it.
    """
    data_file = open('lecture15f.csv', 'r')
    sum_of_values = 0.0
    count = 0

    data_file.readline()
    for line in data_file:
        print ('line of file =', line)
        # 'float,float,float,float'
        for data_point in line.split(','):
            # ['float', 'float', 'float',]
            print ('data point in line =', data_point)
            sum_of_values = sum_of_values + float(data_point)
            count += 1

    print("The average of {0} values is {1}".format(
        count,
        sum_of_values / count))


if __name__ == '__main__':
    main()
