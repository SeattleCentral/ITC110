
class Animal:
    legs = 4
    sound = 'Roar'

    def __init__(self, *args, **kwargs):
        if kwargs.get('legs', None) is not None:
            # Not safe: kwargs['legs'] is not None:
            self.legs = kwargs['legs']
        if kwargs.get('sound', None) is not None:
            self.sound = kwargs['sound']

    def talk(self):
        print(self.sound)


print('We are talking to the dog.')
dog = Animal(sound='Woof')
dog.talk()

print('We are talking to a default animal.')
animal = Animal()
animal.talk()

print('We are talking to a cat.')
cat = Animal(legs=3, sound='Meow')
cat.talk()

print('And by the way, the cat only has', cat.legs, 'legs.')


class Dolphin(Animal):
    fins = 4
    sound = 'Sqeeeeek'

    def __init__(self, *args, **kwargs):
        if kwargs.get('fins', None) is not None:
            self.fins = kwargs['fins']
        if kwargs.get('sound', None) is not None:
            self.sound = kwargs['sound']


print('We are talking to a standard dolphin.')
dolphy = Dolphin()
dolphy.talk()

print('We are talking to a veteral of SeaWorld.')
crusty = Dolphin(fins=3, sound='Squerrrk. Squeek. HELP!')
crusty.talk()


