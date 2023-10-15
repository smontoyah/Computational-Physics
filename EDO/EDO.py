import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class ODESolver:
    def __init__(self, f, y0, t0, t_max, n):
        self.f = f  # The ODE function f(y, t)
        self.y0 = y0  # Initial condition y0
        self.t0 = t0  # Initial time t0
        self.t_max = t_max  # Maximum time to solve for
        self.n = n  # Number of steps
        self.h = (self.t_max - self.t0) / self.n  # Step size

    def euler_solve(self):
        t = np.arange(self.t0, self.t_max + self.h, self.h)
        y = np.zeros(len(t))
        y[0] = self.y0
        for i in range(1, len(t)):
            y[i] = y[i - 1] + self.h * self.f(y[i - 1], t[i - 1])
        return t, y

    def odeint_solve(self):
        t = np.linspace(self.t0, self.t_max, 101)
        y = odeint(self.f, self.y0, t)
        return t, y[:, 0]

    def plot(self):
        t_euler, y_euler = self.euler_solve()
        t_odeint, y_odeint = self.odeint_solve()
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_title("Comparison between Euler and exact (odeint) solutions")
        ax.plot(t_euler, y_euler, '.', label='Euler')
        ax.plot(t_odeint, y_odeint, label='Odeint')
        ax.set_xlabel('t')
        ax.set_ylabel('y')
        ax.legend()
        fig.savefig('euler_exacta.png')
        plt.show()
