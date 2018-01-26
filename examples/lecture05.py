
# Solve Quadratic Equation
# ========================

import math


def solve_quadratic(a, b, c):
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print ("The solution is:", root1, root2)


solve_quadratic(3, 4, -1)
























