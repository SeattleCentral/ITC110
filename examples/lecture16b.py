# Flying pumpkin projectile project
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
        self.highest_point = self.checkHighestPoint()

    # Helper methods
    # ==============
    def getNextX(self):
        return self.x_position + self.time_interval * self.x_velocity

    def getNextY(self):
        final_y_velocity = self.y_velocity - self.time_interval * 9.8
        y_position = self.y_position + self.time_interval * (
            (self.y_velocity + final_y_velocity) / 2.0 # Average y velocity
        )
        self.y_velocity = final_y_velocity
        return y_position

    def checkHighestPoint(self):
        if self.y_position > self.highest_point:
            return self.y_position
        else:
            return self.highest_point

    # Accessor methods
    # ================
    def getX(self):
        return self.x_position

    def getY(self):
        return self.y_position

    def getHighestPoint(self):
        return self.highest_point


def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    velocity = float(input("Enter the intial velocity (in m/s): "))
    initial_height = float(input("Enter the initial height (m): "))

    # Instantiate a new object, "pumpkin"
    pumpkin = Pumpkin(angle, velocity, initial_height)

    while pumpkin.getY() >= 0.0:
        pumpkin.update()

    print ("\nDistance traveled: {0:0.1f} meters".format(pumpkin.getX()))
    print ("The highest point reached is {0:0.1f} meters\n".format(
            pumpkin.getHighestPoint() ))


if __name__ == '__main__':
    main()












