from penduloSimple import SimplePendulum

if __name__ == "main":
    print("Running simple pendulum")

    g = 9.8  # Gravitational acceleration
    L = g / 16  # Length to satisfy the imposed condition sqrt(g/L) = 4
    theta = 1  # Initial angle
    omega0 = 0  # Initial angular velocity
    dt = 0.1  # Time step
    tmax = 5  # Maximum time

    # Create an instance with the required parameters
    myPendulum = SimplePendulum(L, g, theta, omega0, dt, tmax)
    myPendulum.euler()
    myPendulum.angularDisplacement()
