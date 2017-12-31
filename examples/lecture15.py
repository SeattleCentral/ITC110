user_flavor = input("What flavor do you want [vanilla]: ")

# if user_flavor:
#     # True for non-empty strings
#     flavor = user_flavor
# else:
#     flavor = 'vanilla'

flavor = user_flavor and 'vanilla'

print("I am serving you:", flavor)
