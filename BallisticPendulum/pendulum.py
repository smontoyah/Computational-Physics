import numpy as np
import matplotlib.pyplot as plt

class BallisticPendulum:
    
    def __init__(self, length, mass_bullet, mass_block, bullet_velocity, gravity):
        """
        Initializes the parameters of the ballistic pendulum.
        """
        self.length = length
        self.mass_bullet = mass_bullet
        self.mass_block = mass_block
        self.bullet_velocity = bullet_velocity
        self.gravity = gravity
        self.time = np.arange(0, 100, 0.1)
    
    def calculate_deflection_angle(self):
        
        # As seen in class, there are certain conditions where the velocity diverges, and the pendulum keeps spinning indefinitely,
        # so we need to prevent this and inform the user.
        
        if self.bullet_velocity > (2 * np.sqrt(self.gravity * self.length) * (self.mass_bullet + self.mass_block)) / self.mass_bullet:
            raise ValueError('Change parameters')
        else:
            deflection_angle = np.arccos(1 - (self.mass_bullet * self.bullet_velocity / (self.mass_bullet + self.mass_block)) ** 2 * (1 / (2 * self.gravity * self.length)))
            deflection_angle = np.rad2deg(deflection_angle)
            return print("The deflection angle is", deflection_angle)
    
    def calculate_block_bullet_velocity(self):
        """
        Calculates the velocity of the system after impact.
        """
        block_bullet_velocity = np.sqrt(2 * self.gravity * self.length)
        return print("The bullet velocity is", block_bullet_velocity)

# We apply inheritance to the PenduloHijo class, which calculates the minimum conditions
class MinimumConditionsPendulum(BallisticPendulum):
    def __init__(self, length, mass_bullet, mass_block, bullet_velocity, gravity, theta):
        print('Initializing minimum conditions class')
        super().__init__(length, mass_bullet, mass_block, bullet_velocity, gravity)
        self.theta = np.deg2rad(theta)

    
    def pendulum_velocity(self):
        min_velocity = np.sqrt(5 * self.length * self.gravity)  # Minimum pendulum condition
        print("The minimum velocity of the system is", min_velocity)
        return min_velocity 

  
    def block_velocity(self):
        min_velocity_block = 2 * (self.mass_bullet + self.mass_block) * self.pendulum_velocity() / self.mass_bullet  # Minimum condition for small mass m
        return print("The minimum velocity of the small mass is ", min_velocity_block)
    
    # The "calculate_period" method can be overridden to calculate the period of any pendulum
    def calculate_period(self):
        T = 2 * np.pi * np.sqrt(self.length / (self.gravity))
        return print("The period of the pendulum is {}".format(T))
    
    # According to the calculation with conservation of mechanical energy, the system oscillates harmonically
    def solution(self, t):
        return np.sin(t)

    # Plot the oscillations
    def plot(self):
        plt.title('Angular motion of the pendulum')
        plt.plot(self.time, self.solution(self.time))
        plt.savefig("pendulum_graph.png")
        plt.xlabel('$t$')
        plt.ylabel('$θ(t)$')
