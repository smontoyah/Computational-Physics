from pendulum import BallisticPendulum, MinimumConditionsPendulum

if __name__ == "__main__":

    # Parameters to model the ballistic pendulum
    deflection_angle = 140  # Deflection angle
    gravity = 9.8  # Gravitational acceleration
    length = 10  # Length of the string
    mass_bullet = 0.1  # Mass of the bullet
    mass_pendulum = 10  # Mass of the pendulum
    initial_velocity = 400  # Initial velocity of the bullet
    
    # Create instances of the classes with their respective parameters
    myPendulum = BallisticPendulum(length, mass_bullet, mass_pendulum, initial_velocity, gravity)
    myPendulum2 = MinimumConditionsPendulum(length, mass_bullet, mass_pendulum, initial_velocity, gravity, deflection_angle)

    # Call the methods that print the physical information to the console
    myPendulum.calculate_deflection_angle()
    myPendulum.calculate_block_bullet_velocity()
    myPendulum2.pendulum_velocity()
    myPendulum2.block_velocity()
    myPendulum2.calculate_period()
    myPendulum2.plot()
