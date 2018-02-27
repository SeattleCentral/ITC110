import math


def quadratic():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    try:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print ("\nThe solutions is: ", root1, ",", root2)
    except ValueError as kitten:
        print("\nThe exact error message is: ", kitten)
        print("\nThere are no real solutions.")
    except Exception as error:
        print("\nAn unknown error has occurred:", error)


if __name__ == '__main__':
    quadratic()
