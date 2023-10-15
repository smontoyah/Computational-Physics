# Import the required class from the "particula" module
from particula import MultiCycleParticleMotion

# Import necessary libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


if __name__ == "__main__":
    # Define the parameters for the charged particle motion
    E = 18.6 * 1.602E-19  # Kinetic energy
    m = 9.1E-31  # Mass of the electron
    q = 1.602E-19  # Charge of the electron
    B = 0  # Magnetic field [T]
    ang = 30  # Angle [°]
    ciclos = 7

    # Create an instance of the MultiCycleParticleMotion class to simulate the particle's motion
    mov = MultiCycleParticleMotion(1, E, m, q, B, ang, ciclos)
    
    # Generate time values for multiple cycles
    t = mov.view_cycles()
    mov.t = t  # Renaming the method to use it as a variable (not necessary, but it clarifies the intent)
    
    # Plot the trajectory of the particle
    mov.plot_trajectory()

    # Print additional information about the particle's motion
    print("********** Additional INFO ***********")
    print("Radius of curvature = {:.2E} m".format(mov.r))
    print("Initial velocity (V_0) = {:.2E} m/s".format(mov.v))
    print("Angular frequency (w) = {:.2E} rad/s".format(mov.w))
    print("***********************************")
