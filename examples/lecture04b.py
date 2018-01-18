
def change_counter():
    print("Determine the value of your pocket change.")

    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))

    value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    print("You have ${0} in pocket change!".format(round(value, 2)))


if __name__ == '__main__':
    change_counter()
