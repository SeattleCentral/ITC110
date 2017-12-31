# Dog Example


class Dog(object):
    def __init__(self, name="", owner_name=""):
        self.name = name
        self.owner_name = owner_name

    def bark(self):
        print("Woof! Hello, {0}.".format(self.owner_name))


fido = Dog("Fido", "Mr. Bob")

# Creats an "Alias"
fifi = fido

fido.owner_name = "Ms. Suzy"

fido.bark()
fifi.bark()
