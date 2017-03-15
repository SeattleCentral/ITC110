# Notes from March 13th 2017
"All non-trivial abstractions, to some degree, are leaky."

<cite>- Joel Spolsky *(Joel on Software)*</cite>

[Law of Leaky Abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

## Class
>A description of what attributes an object will have. The "blueprints" for creating new objects.

## Constructor
>A special method that is invoked when creating a new object from a *Class*. In Python, this is the `__init__()` method.

## Self
All methods in a Python class have an initial argument, `self`, that is implicitly passed to method calls.

Example:

    class Dog:

        def bark(self):
            print("Woof!")
    
    
    fido = Dog()
    fido.bark()
    # Prints "Woof!"

## Multi-Sided Dice

Create a simple class that can simulate dice rolls.

    class Dice:

        # Constructor
        def __init__(self, sides):
            self.sides = sides
            self.value = 1

        # Accessor method
        def getValue(self):
            return self.value

        #Mutator methods
        def roll(self):
            self.value = randrange(1, self.sides + 1)

        def setValue(self, value):
            self.value = value

## Pumpkin Projectile

Given a cannon that fires a pumpkin at a set angle and initial velocity, determing how far the pumpkin will fly before landing on a large, soft marshmallow.

Note: Python doesn't perform trigonometric calculations in degrees, therefore we have to convert to radians.

    from math import sin, cos, radians

    class Pumpkin:
        """
        Store and calculate data relating to a pumpkin projectile.
        """

        # Class property
        # ==============
        time_interval = 0.1

        # "Constructor" method
        # ====================
        def __init__(self, angle, velocity, initial_height=0):
            # Instance variables
            self.x_position = 0
            self.y_position = initial_height
            self.highest_point = initial_height

            # Convert angle to radians
            angle_in_radians = radians(angle)

            self.x_velocity = velocity * cos(angle_in_radians)
            self.y_velocity = velocity * sin(angle_in_radians)

        # Mutator methods
        # ===============
        def update(self):
            self.x_position = self.getNextX()
            self.y_position = self.getNextY()
            self.setHighestPoint()

        def getNextX(self):
            return self.x_position + self.time_interval * self.x_velocity

        def getNextY(self):
            final_y_velocity = self.y_velocity - self.time_interval * 9.8
            y_position = self.y_position + self.time_interval * (
                (self.y_velocity + final_y_velocity) / 2.0 # Average y velocity
            )
            self.y_velocity = final_y_velocity
            return y_position

        def setHighestPoint(self):
            if self.y_position > self.highest_point:
                self.highest_point = self.y_position

        # Accessor methods
        # ================
        def getX(self):
            return self.x_position

        def getY(self):
            return self.y_position

        def getHighestPoint(self):
            return self.highest_point


## Et Cetera
* Slides for [Chapter 10](http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter10.pptx)
* Examples for [Lecture 16](../examples/lecture16.py) [Lecture 16a](../examples/lecture16a.py) [Lecture 16b](../examples/lecture16b.py)
* Repl.it Development Environment: [https://repl.it](https://repl.it/)