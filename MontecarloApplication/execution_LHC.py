# Import the CircularCollider class from LHC module
from LHC import CircularCollider

if __name__ == "__main__":
    print("Running LHC")

    # Instantiate the collider and run the simulation
    R = 5  # Radius of the circular collider
    r = 1  # Radius of the particles
    n_values = [10, 100, 1000, 10000]  # Number of particles to simulate
    print("In this adapted version, random angles theta1 and theta2 are generated in the range of 0 to 2π, representing the angular position of particles on faces A and B of the circular collider, respectively. Then, the coordinates x1, y1, x2, and y2 corresponding to the particles on both faces are calculated.")

    collider = CircularCollider(R, r, n_values)
    collider.plot_collision_probability()
