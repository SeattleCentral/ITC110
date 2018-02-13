print("Thank for your enrolling in ITC110.")
print("Let's setup your BE 1130 username.")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

username = first_name[0] + last_name[:7]

print ("Your username is {0}, and your password is: {1}".format(
    username.lower(), "P@ssw0rd1"))
