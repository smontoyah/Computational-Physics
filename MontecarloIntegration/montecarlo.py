import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

class MonteCarloIntegrator:
    def __init__(self, f, a, b, num_samples):
        # Class constructor
        self.f = f  # Function to integrate
        self.a = a  # Lower limit of integration
        self.b = b  # Upper limit of integration
        self.num_samples = num_samples  # Number of random samples

    def integrate(self):
        # Basic Monte Carlo integration
        integral_sum = 0
        
        for i in range(self.num_samples):
            x = random.uniform(self.a, self.b)  # Generate a random sample
            integral_sum += self.f(x)  # Evaluate the function at the sample point
            
        integral = (self.b - self.a) * (integral_sum / self.num_samples)  # Compute the integral
        
        return integral

    def integral_exacta(self):
        # Integration using the standard library
        integral, _ = quad(self.f, self.a, self.b)  # Use quad from scipy to compute the integral
        
        return integral

    def compare_methods(self):
        # Print values and their comparison
        exact_integral = self.integral_exacta()
        mc_integral = self.integrate()
        error_relativo = abs((mc_integral - exact_integral) / exact_integral)
    
        print("The integral of the function between {} and {} is:".format(self.a, self.b))
        print("Exact (scipy):", self.integral_exacta())
        print("Monte Carlo:", self.integrate())
        print("Relative error of Monte Carlo: {} %".format(error_relativo * 100))

    def plot(self):
        # Create a bar plot comparing the two integration methods
        exact_integral = self.integral_exacta()
        mc_integral = self.integrate()
        
        plt.bar(["Exact", "Monte Carlo"], [exact_integral, mc_integral])
        plt.ylabel("Value of the integral")
        plt.savefig("comparison_methods.png")
        plt.show()
