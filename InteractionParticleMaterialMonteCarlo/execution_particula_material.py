from material_particle import Material, Particle, simulate_particle
import matplotlib.pyplot as plt

if __name__ == "__main":
    density = 1.0  # Material density in g/cm³
    energy_loss_probabilities = {
        0.1: 0.1,
        0.5: 0.4,
        1.0: 0.3,
        5.0: 0.2
    }  # Energy loss probabilities in each cell
    material = Material(density, energy_loss_probabilities)
    particle = Particle(100.0)  # Initial energy of the particle
    num_cells = 100  # Number of cells the particle traverses

    energies = simulate_particle(particle, material, num_cells)

    plt.plot(range(num_cells), energies)
    plt.xlabel('Cell')
    plt.ylabel('Energy (MeV)')
    plt.title('Energy Evolution of a Particle Passing Through a Material')
    plt.savefig("particle_energy.png")
    plt.show()
