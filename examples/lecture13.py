import math


def main():
    print("This program finds the real solutions to a quadratic equation.\n")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        print("\nThe solutions are: ", root1, root2)
    except ValueError as error:
        if str(error) == "math domain error":
            print("\nNo real roots")
            print("Message: ", error, "\n")
        else:
            print("\nInvalid coefficient given")
            print("Message: ", error, "\n")
    except ZeroDivisionError as error:
        print("\nYour coefficients will divide by zero.")
        print("Message: ", error, "\n")
    except Exception as error:
        print("\nSomething went wrong, sorry!")
        print("Message: ", error, "\n")


if __name__ == '__main__':
    main()

# # Disregard this....
# class Dog(object):

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "{0} the Doggy.".format(self.name)

# doggy = Dog('Bartholemew')
# print(doggy)
