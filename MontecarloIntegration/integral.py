import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integral():
    # Function to integrate
    f = lambda x: x**2 * np.cos(x)
    
    # Integration interval
    a, b = 0, np.pi
    
    # Calculate the integral
    I, _ = quad(f, a, b)
    
    # Plot the function
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y)
    plt.title("Graph of the function x^2 * cos(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
    # Print the result
    print("The integral of the function x^2 * cos(x) in the interval [0, pi] is:", I)

integral()
