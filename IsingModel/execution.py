from ising import IsingModel  # Assuming you have an "ising" module

if __name__ == '__main__':
    # Create an instance of the IsingModel with specified parameters
    ising_model = IsingModel(N=20, J=1, H=0)
    
    # Plot the energy as a function of temperature in the range [1, 4] with 100 steps
    ising_model.plot_energies(T_min=1, T_max=4, num_steps=100)
    
    # Plot the magnetization as a function of temperature in the range [1, 4] with 100 steps
    ising_model.plot_magnetization(T_min=1, T_max=4, num_steps=100)
    
    # Plot the specific heat as a function of temperature in the range [1, 4] with 100 steps
    ising_model.plot_specific_heat(T_min=1, T_max=4, num_steps=100)
