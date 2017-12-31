number_of_drinks = int(input("How many drinks have you had? "))

while number_of_drinks < 8:
    print("You're fine... Have another!")
    number_of_drinks = int(input("How many drinks have you had? "))

print("Woah! You better stop!")
