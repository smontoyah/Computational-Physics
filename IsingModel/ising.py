import matplotlib.pyplot as plt
import numpy as np

class IsingModel:
    
    def __init__(self, N, J, H):
        self.N = N
        self.J = J
        self.H = H
        self.spins = np.random.choice([-1, 1], size=(N, N))
        
    def energy(self):
        # Calculate the total energy of the system
        spin_sum = np.roll(self.spins, shift=1, axis=0) + np.roll(self.spins, shift=-1, axis=0) \
                   + np.roll(self.spins, shift=1, axis=1) + np.roll(self.spins, shift=-1, axis=1)
        return -self.J * np.sum(spin_sum * self.spins) - self.H * np.sum(self.spins)
    
    def magnetization(self):
        # Calculate the total magnetization of the system
        return np.sum(self.spins)
    
    def monte_carlo_step(self, beta):
        # Perform a single Monte Carlo step
        i, j = np.random.randint(0, self.N, size=2)
        spin_flip_energy = 2 * self.J * self.spins[i, j] * (self.spins[(i - 1) % self.N, j] + self.spins[(i + 1) % self.N, j] \
                                                           + self.spins[i, (j - 1) % self.N] + self.spins[i, (j + 1) % self.N])
        if spin_flip_energy <= 0 or np.random.rand() < np.exp(-beta * spin_flip_energy):
            self.spins[i, j] *= -1
            
    def simulate(self, T_min, T_max, num_steps):
        # Simulate the system for a range of temperatures
        T_vals = np.linspace(T_min, T_max, num=num_steps)
        E_vals = np.zeros(num_steps)
        M_vals = np.zeros(num_steps)
        C_vals = np.zeros(num_steps)
        
        for i, T in enumerate(T_vals):
            beta = 1 / T
            for j in range(self.N ** 2):
                self.monte_carlo_step(beta)
            E_vals[i] = self.energy()
            M_vals[i] = self.magnetization()
            C_vals[i] = (1 / (T ** 2)) * (np.mean(E_vals ** 2) - (np.mean(E_vals) ** 2))
        
        return T_vals, E_vals, M_vals, C_vals
    
    def plot_energies(self, T_min, T_max, num_steps):
        # Plot the energy as a function of temperature
        T_vals, E_vals, _, _ = self.simulate(T_min, T_max, num_steps)
        
        plt.plot(T_vals, E_vals)
        plt.xlabel('Temperature')
        plt.ylabel('Energy')
        plt.show()
        
    def plot_magnetization(self, T_min, T_max, num_steps):
        # Plot the magnetization as a function of temperature
        T_vals, _, M_vals, _ = self.simulate(T_min, T_max, num_steps)
        
        plt.plot(T_vals, M_vals)
        plt.xlabel('Temperature')
        plt.ylabel('Magnetization')
        plt.show()
        
    def plot_specific_heat(self, T_min, T_max, num_steps):
        # Plot the specific heat as a function of temperature
        T_vals, _, _, C_vals = self.simulate(T_min, T_max, num_steps)
        
        plt.plot(T_vals, C_vals)
        plt.xlabel('Temperature')
        plt.ylabel('Specific Heat')
        plt.savefig('specific_heat.png')
        plt.show()
