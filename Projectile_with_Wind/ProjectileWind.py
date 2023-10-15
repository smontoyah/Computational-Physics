from ProjectileMotion import ProjectileMotion 

import matplotlib.pyplot as plt
import numpy
import math

# Define a new class for motion with wind in the x-direction. This class inherits all attributes and methods from "ProjectileMotion" but also has an additional attribute "a" corresponding to acceleration in the x-direction.

class ProjectileMotionWithWind(ProjectileMotion):
    def __init__(self, initial_velocity, launch_angle, gravity, initial_height, initial_position, acceleration_x):
        super().__init__(initial_velocity, launch_angle, gravity, initial_height, initial_position)

        print("Initializing the ProjectileMotionWithWind class")

        self.acceleration_x = acceleration_x

    # Its unique feature is the "horizontal_position_with_wind" method, which calculates the horizontal position as a result of uniformly accelerated motion in the x-direction.
    def horizontal_position_with_wind(self):
        pos_x = [self.initial_position + i * self.horizontal_velocity() + 0.5 * self.acceleration_x * i ** 2 for i in self.arrival_time()]
        return pos_x

    # Plot the trajectory
    def plot_trajectory_with_wind(self):
        plt.figure(figsize=(10, 8))
        plt.title("Trajectory of Projectile Motion with Wind in the X-direction")
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.plot(self.horizontal_position_with_wind(), self.vertical_position())
        plt.text(self.initial_position, 0, 'a_x = {} m/s^2\n g = {} m/s^2\nV0 = {} m/s \nt_flight = {:.1f} s'.format(self.acceleration_x, self.gravity, self.initial_velocity, self.max_flight_time()), bbox=dict(facecolor='red', alpha=0.5))
        plt.savefig("projectileWithWind.png")

# The code defines a class named "ProjectileMotionWithWind" to model and visualize the trajectory of a projectile in the presence of wind in the x-direction. It inherits from the "ProjectileMotion" class and adds an additional attribute for acceleration in the x-direction and a method to calculate the horizontal position with wind.
