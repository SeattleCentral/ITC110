def convert_to_number(value):
    try:
        value = int(value)
        return value
    except Exception:
        return 0


def main():
    print("Find the largest number")

    number_string = input("Enter a list of numbers, separated by a space: ")
    # Expected input = "4 6 23 99 32 1 0 -4 44 76"
    numbers = number_string.split(" ")
    # Expected list = ["4", "6", "23", ...]

    max_number = convert_to_number(numbers[0])
    for number in numbers:
        number = convert_to_number(number)
        if number > max_number:
            max_number = number

    print("The greatest number is:", max_number)


if __name__ == '__main__':
    main()
