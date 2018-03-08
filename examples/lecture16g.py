import math


class Projectile:
    angle = None
    speed = None
    initial_height = 1  # in meters
    time_interval = 0.1
    x_velocity = 0
    y_velocity = 0

    def __init__(self, angle=None, speed=None, initial_height=1):
        if angle is None:
            raise Exception('Must set an initial= angle')
        else:
            self.angle = angle

        if speed is None:
            raise Exception('Must set an initial speed.')
        else:
            self.speed = speed

        self.initial_height = initial_height
        self.x = 0
        self.y = self.initial_height
        self.set_initial_velocity()

    def set_initial_velocity(self):
        theta = math.radians(self.angle)
        self.x_velocity = self.speed * math.cos(theta)
        self.y_velocity = self.speed * math.sin(theta)

    def get_distance(self):
        while self.y >= 0:
            self.x = self.x + (self.x_velocity * self.time_interval)
            new_y_velocity = self.y_velocity - (
                self.time_interval * 9.8    # m/s^2
            )
            self.y = self.y + (self.time_interval * (
                (self.y_velocity + new_y_velocity) / 2.0
            ))
            self.y_velocity = new_y_velocity
        return self.x


class PumpkinProjectile(Projectile):
    speed = 40

    def __init__(self, *args, **kwargs):
        kwargs['speed'] = self.speed
        super(PumpkinProjectile, self).__init__(*args, **kwargs)


class AppleProjectile(Projectile):
    speed = 200

    def __init__(self, *args, **kwargs):
        kwargs['speed'] = self.speed
        super(AppleProjectile, self).__init__(*args, **kwargs)


print('We want to put the observation stands at 500m.')

humpty = PumpkinProjectile(angle=30)
print('Pumpkin "humpty" will make it to', humpty.get_distance(), 'meters.')


dumpty = PumpkinProjectile(angle=50, initial_height=2)
print('Pumpkin "dumpty" will make it to', dumpty.get_distance(), 'meters.')

johnny = AppleProjectile(angle=45)
print('Apple "johnny" will make it to', johnny.get_distance(), 'meters.')

