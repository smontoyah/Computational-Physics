# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a class
class ParticleMotion():
    def __init__(self, time, particle_energy, particle_mass, particle_charge, magnetic_field, angle):
        self.B = magnetic_field  # Magnetic field
        self.m = particle_mass   # Mass
        self.t = time            # Time
        self.Ek = particle_energy  # Kinetic energy of the particle
        self.q = particle_charge  # Particle charge
        self.ang = angle        # Angle with respect to the magnetic field
        self.w = abs(self.q) * self.B / self.m  # Angular frequency
        self.v = np.sqrt(self.Ek * 2 / self.m)  # Solve for initial velocity (v_0) from Ek
        self.v_c = self.v * np.sin(np.pi / 180 * self.ang)  # Component of velocity that causes curvature
        self.r = self.v_c * self.m / (abs(self.q) * self.B)  # Radius of the trajectory

    # Movement in the x-direction
    def position_x(self):
        x = self.r * np.sin(self.w * self.t)
        return x

    # Movement in the y-direction
    def position_y(self):
        y = self.r * np.cos(self.w * self.t)
        return y

    # Movement in the z-direction
    def position_z(self):
        vz = self.v * np.cos(np.pi / 180 * self.ang)
        z = vz * self.t
        return z

    # Period
    def period(self):
        T = 2 * np.pi / self.w
        return T

    # Plot the trajectory
    def plot_trajectory(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.position_x(), self.position_y(), self.position_z(), "g",
                label="Ek = {:.2E} J \nB = {} T \n$\phi$ = {}° \ncycles = {}".format(self.Ek, self.B, self.ang, self.cycles))
        ax.set_xlabel('X [m]')
        ax.set_ylabel('Y [m]')
        ax.set_zlabel('Z [m]')
        ax.set_title('Charged Particle Trajectory with Oblique v to B')
        ax.legend(loc='upper right')
        plt.savefig("xyz_particle.png")

# To observe just one cycle of the particle, we create another class that inherits from ParticleMotion
class MultiCycleParticleMotion(ParticleMotion):
    def __init__(self, time, particle_energy, particle_mass, particle_charge, magnetic_field, angle, cycles):
        super().__init__(time, particle_energy, particle_mass, particle_charge, magnetic_field, angle)
        self.cycles = cycles

    def view_cycles(self):
        t = np.linspace(0, self.cycles * super().period(), 1000)
        return t
