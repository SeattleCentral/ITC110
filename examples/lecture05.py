def count_money():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = 0.00

    # Add quarters
    total += quarters * 0.25

    # Add dimes
    total += dimes * 0.10

    # Add nickels
    total += nickels * 0.05

    # Add pennies
    total += pennies * 0.01

    total = round(total, 2)

    return total


print("I have $", count_money(), sep="")


# Decimals
# ========

from decimal import Decimal


def count_money():
    quarters = Decimal(input("How many quarters? "))
    dimes = Decimal(input("How many dimes? "))
    nickels = Decimal(input("How many nickels? "))
    pennies = Decimal(input("How many pennies? "))

    total = Decimal('0.00')

    # Add quarters
    total += quarters * Decimal('0.25')

    # Add dimes
    total += dimes * Decimal('0.10')

    # Add nickels
    total += nickels * Decimal('0.05')

    # Add pennies
    total += pennies * Decimal('0.01')

    return total


print("I have $", count_money(), sep="")


# Solve Quadratic Equation
# ========================

import math


def solve_quadratic(a, b, c):
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print ("The solution is:", root1, root2)


solve_quadratic(3, 4, -1)
























