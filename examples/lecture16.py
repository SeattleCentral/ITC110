# Flying pumpkin projectile project
# Aka p3

from math import sin, cos, radians

def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    velocity = float(input("Enter the intial velocity (in m/s): "))
    initial_height = float(input("Enter the initial height (m): "))
    time_interval = 0.1

    # Convert angle to radians
    angle_in_radians = radians(angle)

    x_position = 0
    y_position = initial_height
    x_velocity = velocity * cos(angle_in_radians)
    y_velocity = velocity * sin(angle_in_radians)

    highest_point = initial_height

    while y_position >= 0.0:
        # Calculate position and velocity in seconds
        x_position = x_position + time_interval * x_velocity
        final_y_velocity = y_velocity - time_interval * 9.8
        y_position = y_position + time_interval * (
            (y_velocity + final_y_velocity) / 2.0 # Average velocity
        )
        y_velocity = final_y_velocity

        if y_position > highest_point:
            highest_point = y_position

    print ("\nDistance traveled: {0:0.1f} meters".format(x_position))
    print ("The highest point reached is {0:0.1f} meters\n".format(
            highest_point))


main()












