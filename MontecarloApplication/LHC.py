import numpy as np
import matplotlib.pyplot as plt
import math

class CircularCollider:
    def __init__(self, R, r, n_values):
        # Constructor to initialize the circular collider parameters
        self.R = R  # Radius of the outer circle
        self.r = r  # Radius of the inner circle
        self.n_values = n_values  # List of iteration values
        self.collision_probability = []

    def simulate_collisions(self):
        for n in self.n_values:
            theta1 = np.random.uniform(0, 2 * np.pi, size=int(n))  # Angles for particles on side A
            theta2 = np.random.uniform(0, 2 * np.pi, size=int(n))  # Angles for particles on side B

            x1 = (self.R - self.r) * np.cos(theta1)  # x-coordinates of particles on side A
            y1 = (self.R - self.r) * np.sin(theta1)  # y-coordinates of particles on side A

            x2 = -(self.R - self.r) * np.cos(theta2)  # x-coordinates of particles on side B
            y2 = -(self.R - self.r) * np.sin(theta2)  # y-coordinates of particles on side B

            valid_particles = ((x1**2 + y1**2) < (self.R - self.r)**2) & ((x2**2 + y2**2) < (self.R - self.r)**2)

            if np.any(valid_particles):  # Check if there are particles that meet the condition
                collisions = np.vectorize(lambda x1, y1, x2, y2: True if math.dist([x1, y1], [x2, y2]) <= 2 * self.r else False) \
                    (x1[valid_particles], y1[valid_particles], x2[valid_particles], y2[valid_particles])  # Euclidean distance between particles < 2R
                self.collision_probability.append(collisions.sum() / valid_particles.sum())
            else:
                self.collision_probability.append(0)  # Set collision probability to zero

    def plot_collision_probability(self):
        self.simulate_collisions()
        plt.plot(self.n_values, self.collision_probability, '.-')
        plt.xlabel('Number of Iterations (n)')
        plt.ylabel('Collision Probability')
        plt.title('Collision Probability vs Number of Iterations')
        plt.grid(True)
        plt.show()
