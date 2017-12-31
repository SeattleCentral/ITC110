from datetime import date

# JavaScript has zero-indexed months
# So 01 is February (because 00 is January and 11 is December)
#              > 0123456789
date_from_web = "2017-01-08"

year = int(date_from_web[0:4])
month = int(date_from_web[5:7]) + 1     # Python has one-indexed MM
day = int(date_from_web[8:])

python_date = date(year, month, day)

print("My date in Python is: {0}".format(
    python_date.strftime('%c'))
)

# String Concatenation
name = "Bob"
my_long_string = "Hello, " + name + ". How are you today?"
print(my_long_string)


chant = "I am fine. Really. Ok?\n" * 10
print(chant)

# Username Example
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")

uname = first_name[0] + last_name[0:7]

print("Congratulations, you are registered.")
print("Your username is: " + uname.lower() + ".")
























