def main():
    sum = 0
    count = 0

    more_data = "yes"

    while more_data[0] == "y":
        value = float(input("Enter a number to average: "))
        sum += value
        count += 1

        more_data = input("Do you have another number to enter? (yes or no) ")

    print("The average of the {0} numbers entered is {1}.".format(
        count, sum / count))


if __name__ == '__main__':
    print ("Get the average of x numbers.")
    main()
