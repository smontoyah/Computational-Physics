import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

class CSVPlotter:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def fit_quadratic(self):
        # Read the CSV file
        data = pd.read_csv(self.csv_file)

        # Extract data columns
        x = data["x"]
        y = data["y"]

        # Define the quadratic function
        def quadratic_func(x, a, b, c):
            return a * x**2 + b * x + c

        # Fit the quadratic function to the data
        popt, pcov = curve_fit(quadratic_func, x, y)

        # Calculate the fit error (sum of squared residuals)
        residuals = y - quadratic_func(x, *popt)
        error = np.sum(residuals**2)

        # Create a new set of points for the fitted function
        x_fit = np.linspace(x.min(), x.max(), 100)
        y_fit = quadratic_func(x_fit, *popt)

        # Create the figure and axes
        fig, ax = plt.subplots()

        # Plot the fitted function
        ax.plot(x_fit, y_fit, 'r-', label="Quadratic Fit")

        # Plot the data
        ax.plot(x, y, '.', label="Data")

        # Customize axes and chart title
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Quadratic Fit of Data")

        # Add the error to the legend
        legend_text = f"Quadratic Fit\nError: {error:.2f}"
        ax.legend([legend_text])

        # Show the plot
        plt.savefig("quadratic_fit.png")
        plt.show()

        return error

    def fit_gaussian(self):
        # Read the CSV file
        data = pd.read_csv(self.csv_file)

        # Extract data columns
        x = data["x"]
        y = data["y"]

        # Define the Gaussian function
        def gaussian_func(x, norm, mean, sigma):
            return norm * np.exp(-(x - mean)**2 / (2 * sigma**2))

        # Fit the Gaussian function to the data
        popt, pcov = curve_fit(gaussian_func, x, y)

        # Calculate the fit error (chi-squared)
        residuals = y - gaussian_func(x, *popt)
        chi_squared = np.sum(residuals**2)

        # Create a new set of points for the fitted function
        x_fit = np.linspace(x.min(), x.max(), 100)
        y_fit = gaussian_func(x_fit, *popt)

        # Create the figure and axes
        fig, ax = plt.subplots()

        # Plot the fitted function
        ax.plot(x_fit, y_fit, 'r-', label="Gaussian Fit")

        # Plot the data
        ax.plot(x, y, '.', label="Data")

        # Customize axes and chart title
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Gaussian Fit of Data")

        # Add the chi-squared value to the legend
        legend_text = f"Gaussian Fit\nχ²: {chi_squared:.2f}"
        ax.legend([legend_text])

        # Show the plot
        plt.savefig("gaussian_fit.png")
        plt.show()

        return chi_squared
    
    def fit_general(self):
        # Read the CSV file
        data = pd.read_csv(self.csv_file)

        # Extract data columns
        x = data["x"]
        y = data["y"]

        # Define the general function
        def general_func(x, b, norm, mean, sigma):
            return x + b + norm * np.exp(-(x - mean)**2 / (2 * sigma**2))

        # Fit the general function to the data
        popt, pcov = curve_fit(general_func, x, y)

        # Calculate the fit error (chi-squared)
        residuals = y - general_func(x, *popt)
        chi_squared = np.sum(residuals**2)

        # Create a new set of points for the fitted function
        x_fit = np.linspace(x.min(), x.max(), 100)
        y_fit = general_func(x_fit, *popt)

        # Create the figure and axes
        fig, ax = plt.subplots()

        # Plot the fitted function
        ax.plot(x_fit, y_fit, 'r-', label="General Fit")

        # Plot the data
        ax.plot(x, y, '.', label="Data")

        # Customize axes and chart title
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("General Fit of Data")

        # Add the chi-squared value to the legend
        legend_text = f"General Fit\nχ²: {chi_squared:.2f}"
        ax.legend([legend_text])

        # Show the plot
        plt.savefig("general_fit.png")
        plt.show()

        return chi_squared
