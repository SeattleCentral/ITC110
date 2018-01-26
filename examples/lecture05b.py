# Factorials

# 500

# Employee ID 1, 2, 3, 4
# ABC, CDE,
# Invalid: ACC


# ABCDE
accumulator = 0
for factor in [6, 5, 4, 3, 2]:
    accumulator = accumulator * factor
    # print ("accumulator = ", accumulator)


def factorial(starting_value):
    accumulator = 1
    for factor in range(starting_value, 1, -1):
        accumulator = accumulator * factor

    return accumulator


print("The answer is:", factorial(10000))


























