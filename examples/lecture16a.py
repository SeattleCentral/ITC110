from random import randrange

# Dice class

class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

# Testing our class
mydie = Dice(6)
yourdie = Dice(6)
print("Initial value")
print(mydie.getValue())
print(yourdie.getValue())

print("Rolling....")
mydie.roll()
print(mydie.getValue())
print(yourdie.getValue())

# Enter rolling loop
# for i in range(15):
#     mydie.roll()
#     print(mydie.getValue())  





























