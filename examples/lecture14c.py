def main():
    sum = 0
    count = 0

    value = float(input("Enter a grade (negative value to stop): "))
    while value >= 0:
        sum += value
        count += 1
        value = float(input("Enter a grade (negative value to stop): "))

    print("The average grade is {0}.".format(sum / count))


if __name__ == '__main__':
    print ("Get your average grade.")
    main()