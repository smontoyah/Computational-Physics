from montecarlo import MonteCarloIntegrator  # Import the MonteCarloIntegrator class
import numpy as np

if __name__ == "__main__":
    N = 10000  # Enter the number of samples for Monte Carlo integration

    def f(x):
        return x**2 * np.cos(x)  # Define the function to integrate

    integrator = MonteCarloIntegrator(f, 0, np.pi, N)  # Create an instance of the MonteCarloIntegrator class
    integrator.compare_methods()  # Compare Monte Carlo and exact integration methods
    integrator.plot()  # Create a bar plot comparing the methods
