temp_list = [44, 52, 65, 88, 111, 34, 56, 44, 23, 87, 32]


for i in range(0, len(temp_list)):
    print(i + 1)
    if temp_list[i] >= 110:
        print(temp_list[i])
        break


while True:
    verb = input("How do you feel about cats? ")
    print("Cats are", verb)
    if verb == "quit":
        break


while True:
    age = input('How old are you? ')
    try:
        age = int(age)
        if age > 0:
            break
        print('You must be older than 0 to type.')
    except Exception:
        print('You must enter a valid number')



