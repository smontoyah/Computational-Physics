import math
import numpy as np
import matplotlib.pyplot as plt

class ProjectileMotion():
    def __init__(self, initial_velocity, launch_angle, gravity, initial_height, initial_position):
        print("Initializing the ProjectileMotion class")

        # Parameters
        self.initial_velocity = initial_velocity
        self.launch_angle_rad = math.radians(launch_angle)
        self.gravity = gravity
        self.initial_height = initial_height
        self.initial_position = initial_position

    def horizontal_velocity(self):
        vel_x = self.initial_velocity * round(math.cos(self.launch_angle_rad), 3)
        return vel_x

    def vertical_velocity(self):
        vel_y = self.initial_velocity * round(math.sin(self.launch_angle_rad), 3)
        return vel_y

    def max_flight_time(self):
        try:
            t_max = (-(self.vertical_velocity()) - np.sqrt(self.vertical_velocity() ** 2 - 2 * self.gravity * self.initial_height)) / (self.gravity)
            return t_max
        except:
            return "Error in calculating t_max, please review parameters."

    def arrival_time(self):
        arr_time = np.arange(0, self.max_flight_time(), 0.001)
        return arr_time

    def horizontal_position(self):
        pos_x = [self.initial_position + i * self.horizontal_velocity() for i in self.arrival_time()]
        return pos_x

    def vertical_position(self):
        pos_y = [self.initial_height + i * self.vertical_velocity() + 0.5 * self.gravity * i ** 2 for i in self.arrival_time()]
        return pos_y

    def plot_trajectory(self):
        plt.figure(figsize=(10, 8))
        plt.plot(self.horizontal_position(), self.vertical_position())
        plt.savefig("projectile1.png")

# The code defines a class named `ProjectileMotion` to model and visualize the trajectory of a projectile. It takes several parameters, calculates the trajectory, and provides methods to access and plot the results.
