# Passing a parameter to a function
# =================================


def greet_cat(cat):
    print ("Hello ", cat, ", my furry friend!")


greet_cat("Jimmy")

# Prints "Hello Jimmy, my furry friend!"


# Range and For Loops
# ===================

print ("A list of numbers:")

list_of_numbers = list(range(10))
print(list_of_numbers)

# Prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print ("A list of numbers on a separate line:")

for number in range(10):
    print (number)

# Prints
# 0
# 1
# 2
# ...


# Formatting Strings
# ==================

# Getting the *perfect* format in your print statement.
# Use "format" special string method.
name = "Bob",
tree = "fir"
message_to_print = "Hello, {0}. You've been {1}ed!".format(name, tree)

print(message_to_print)

# Prints "Hello, Bob. I see you've been fired!"
