from ProjectileWind import ProjectileMotionWithWind

if __name__ == "__main__":
    print("***************IMPORTANT****************************************")
    print("The reference system is positive upwards and to the right")
    print("*****************************************************************")

    initial_velocity = 20  # Magnitude of the initial velocity
    launch_angle = 45  # Launch angle
    gravity = 0  # Gravitational acceleration
    initial_height = 0  # Initial height
    initial_position_x = 50  # Initial horizontal position
    wind_acceleration_x = -5  # Wind acceleration (+ to the right)

    # Create an instance of the "ProjectileMotionWithWind" class to model and plot the trajectory with wind.
    tirop = ProjectileMotionWithWind(initial_velocity, launch_angle, gravity, initial_height, initial_position_x, wind_acceleration_x)
    tirop.plot_trajectory_with_wind()

 
