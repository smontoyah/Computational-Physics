from EDO import EDO

if __name__ == "__main__":
    print("Running the Euler method")

    # Set the initial values and parameters
    x0 = 0.0  # Initial value of the independent variable
    y0 = -1.0  # Initial value of the dependent variable
    xmax = 1.0  # Maximum value of the independent variable
    n = 100  # Number of steps

    # Define your ODE as f
    def f(y, x):
        return np.exp(-x)

    # Create an instance of the EDO class
    solver = EDO(f, y0, x0, xmax, n)
    solver.plot()