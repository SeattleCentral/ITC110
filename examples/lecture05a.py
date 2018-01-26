
# Solve Quadratic Equation
# ========================

import math


def solve_quadratic(a, b, c):
    try:
        discRoot = math.sqrt(b * b - 4 * a * c)
        x1 = (-b + discRoot) / (2 * a)
        x2 = (-b - discRoot) / (2 * a)
    except ValueError:
        print ("Values are out of bounds")
        return False, False
    return x1, x2


cat1, cat2 = solve_quadratic(4, 2, 2)

print ("x1 =", cat1)
print ("x2 =", cat2)























