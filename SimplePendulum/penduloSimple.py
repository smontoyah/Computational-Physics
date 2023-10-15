import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class SimplePendulum:
    def __init__(self, L, g, theta0, omega0, dt, tmax):
        self.L = L  # Length of the pendulum string
        self.g = g  # Acceleration due to gravity
        self.theta0 = theta0  # Initial angle
        self.omega0 = omega0  # Initial angular velocity
        self.dt = dt  # Time step
        self.tmax = tmax  # Maximum simulation time

    def euler(self):
        # Variable initialization
        theta = np.zeros(int(self.tmax / self.dt) + 1)
        omega = np.zeros(int(self.tmax / self.dt) + 1)
        t = np.arange(0, self.tmax + self.dt, self.dt)
        theta[0] = self.theta0
        omega[0] = self.omega0

        # Solving the differential equation using the Euler method
        for i in range(len(t) - 1):
            omega[i + 1] = omega[i] - (self.g / self.L) * np.sin(theta[i]) * self.dt
            theta[i + 1] = theta[i] + omega[i + 1] * self.dt

        # Plotting the results
        fig, ax = plt.subplots()
        ax.set_title("$\Theta$(t) and $\omega$(t) using the Euler method")
        ax.plot(t, theta, label=r'$\theta(t)$')
        ax.plot(t, omega, label=r'$\omega(t)$')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Angle (rad) / Angular Velocity (rad/s)')
        fig.savefig("euler_method_plot.png")
        ax.legend()

    def angularDisplacement(self):
        # Definition of the function describing the differential equation
        def pendulum(y, t, L, g):
            theta, omega = y
            dydt = [omega, -(g / L) * np.sin(theta)]
            return dydt

        # Initial conditions and simulation time
        y0 = [self.theta0, self.omega0]
        t = np.arange(0, self.tmax + self.dt, self.dt)

        # Solving the differential equation using odeint
        sol = odeint(pendulum, y0, t, args=(self.L, self.g))
        theta = sol[:, 0]
        omega = sol[:, 1]

        # Plotting the results
        fig, ax = plt.subplots()
        ax.plot(t, theta, label=r'$\theta(t)$')
        ax.plot(t, omega, label=r'$\omega(t)$')
        ax.set_title("$\Theta$(t) and $\omega$(t) using angular displacement")
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Angle (rad) / Angular Velocity (rad/s)')
        fig.savefig("angular_displacement_plot.png")
        ax.legend()
