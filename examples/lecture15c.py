class Dog(object):
    # Default / `Class` attributes
    counter = 0
    class_name = 'Dog'

    def __init__(self, name=''):
        # Update `Class` counter
        Dog.counter += 1
        # Instance variable:
        self.instance_name = name

    def get_instance_name(self):
        print ("The name is: ", self.instance_name)

    @classmethod
    def get_class_name(self, name):
        print ("The name is: ", name)


fido = Dog(name='Fido')
print (Dog.counter)
print ("Instance variable: ", fido.instance_name)
print ("Property: ", fido.class_name)

fifi = Dog(name='Fifi')
print (Dog.counter)
print ("Instance variable: ", fifi.instance_name)
print ("Property: ", fifi.class_name)

print ('--------------')

fido.get_instance_name()
Dog.get_class_name('Test')
