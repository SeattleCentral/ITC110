
def main():
    print ("Here is your list of chaotic numbers")
    x = float(input("Enter a number beween 0 and 1: "))
    print(type(x))
    for i in range(10):
        x = 3.9 * x * (1 - x)   # This is chaotic math
        print (x)


if __name__ == '__main__':
    main()
