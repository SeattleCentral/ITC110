def main():
    sum = 0.0
    count = 0

    print ("Press [Enter] to exit.")

    temp = input("What's the temperature? ")
    while temp != "":
        sum += float(temp)
        count += 1
        temp = input("What's the temperature? ")

    print("The average temperature is:", sum / count)


if __name__ == '__main__':
    print ("Get the average temperature.")
    main()