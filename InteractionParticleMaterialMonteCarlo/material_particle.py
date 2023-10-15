import random
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, energy):
        self.energy = energy
        
    def lose_energy(self, delta_energy):
        self.energy -= delta_energy
        
class Material:
    def __init__(self, density, energy_loss_probabilities):
        self.density = density
        self.energy_loss_probabilities = energy_loss_probabilities
        
    def get_energy_loss(self):
        # Get a random energy loss based on the defined probabilities
        return random.choices(list(self.energy_loss_probabilities.keys()), 
                              list(self.energy_loss_probabilities.values()))[0]
    
    def get_energy_loss_probability(self, delta_energy):
        # Get the probability of energy loss for a given delta_energy
        return self.energy_loss_probabilities.get(delta_energy, 0)
    

# This function simulates the energy evolution of a particle passing through a material
# composed of multiple cells. It takes the particle, material, and the number of cells as parameters.

def simulate_particle(particle, material, num_cells):
    energies = []  # An empty list to store the particle's energies
    for i in range(num_cells):  # For each cell
        delta_energy = material.get_energy_loss()  # Determine the energy the particle loses in the cell
        probability = material.get_energy_loss_probability(delta_energy)  # Get the probability of losing that energy
        if random.uniform(0, 1) < probability:  # If the particle loses that energy with that probability
            particle.lose_energy(delta_energy)  # Reduce the particle's energy
        energies.append(particle.energy)  # Add the current energy of the particle to the list
    return energies  # Return the list of particle energies over the material
