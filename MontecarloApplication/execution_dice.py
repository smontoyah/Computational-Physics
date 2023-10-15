from dice_system import DiceSystem, Die
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Number of rolls
    rolls = 1000000

    # Create dice systems with different values of N
    system2 = DiceSystem(2)
    system3 = DiceSystem(3)
    system4 = DiceSystem(4)

    # Roll dice consecutively
    consecutive_results2 = system2.roll_consecutively(rolls)
    consecutive_results3 = system3.roll_consecutively(rolls)
    consecutive_results4 = system4.roll_consecutively(rolls)

    # Roll dice simultaneously
    simultaneous_results2 = system2.roll_simultaneously(rolls)
    simultaneous_results3 = system3.roll_simultaneously(rolls)
    simultaneous_results4 = system4.roll_simultaneously(rolls)

    # Plot the results
    plt.figure(figsize=(18, 12))

    # Histogram for consecutive rolls
    plt.subplot(2, 3, 1)
    plt.hist(consecutive_results2, bins=11, range=(1.5, 12.5), edgecolor='black')
    plt.title('N = 2 (Consecutive)')
    plt.xlabel('Sum')
    plt.ylabel('Number of microstates')

    plt.subplot(2, 3, 2)
    plt.hist(consecutive_results3, bins=16, range=(2.5, 18.5), edgecolor='black')
    plt.title('N = 3 (Consecutive)')
    plt.xlabel('Sum')
    plt.ylabel('Number of microstates')

    plt.subplot(2, 3, 3)
    plt.hist(consecutive_results4, bins=21, range=(3.5, 24.5), edgecolor='black')
    plt.title('N = 4 (Consecutive)')
    plt.xlabel('Sum')
    plt.ylabel('Number of microstates')

    # Histogram for simultaneous rolls
    plt.subplot(2, 3, 4)
    plt.hist(simultaneous_results2, bins=11, range=(1.5, 12.5), edgecolor='black')
    plt.title('N = 2 (Simultaneous)')
    plt.xlabel('Sum')
    plt.ylabel ('Number of microstates')

    plt.subplot(2, 3, 5)
    plt.hist(simultaneous_results3, bins=16, range=(3.5, 19.5), edgecolor='black')
    plt.title('N = 3 (Simultaneous)')
    plt.xlabel('Sum')
    plt.ylabel('Number of microstates')

    plt.subplot(2, 3, 6)
    plt.hist(simultaneous_results4, bins=21, range=(4.5, 25.5), edgecolor='black')
    plt.title('N = 4 (Simultaneous)')
    plt.xlabel('Sum')
    plt.ylabel('Number of microstates')

    plt.tight_layout()
    plt.savefig("dice_system_hist.png")
    plt.show()
