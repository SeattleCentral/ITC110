def sing_happy_line():
    print("Happy birthday to you.")

def sing_happy_name(name):
    print("Happy birthday, dear {0}.".format(name))

def sing_happy_birthday(name):
    sing_happy_line()
    sing_happy_line()
    sing_happy_name(name)
    sing_happy_line()

    # Another way to do it...
    # repeat_lines = [0, 1, 3]
    # for i in range(4):
    #     if i in repeat_lines:
    #         sing_happy_line()
    #     else:
    #         sing_happy_name(name)

name = input("What's your name? ")

sing_happy_birthday(name)
