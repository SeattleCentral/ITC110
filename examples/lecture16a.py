# Dice class
from random import randrange


class Dice:
    """
    Simulate a multi-sided die.
    """

    # Constructor
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    # Accessor method
    def getValue(self):
        return self.value

    # Mutator methods
    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def setValue(self, value):
        self.value = value


# Testing our class
mydie = Dice(6)
print("Initial value")
print(mydie.getValue())

print("Rolling....")
mydie.roll()
print(mydie.getValue())

# Enter rolling loop
for i in range(15):
    mydie.roll()
    print(mydie.getValue())
