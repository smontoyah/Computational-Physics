from ajuste import CSVPlotter

if __name__ == "__main__":

    print("Ejecutando ajustes")
    # Uso de la clase
    csv_plotter = CSVPlotter("fit_curve.csv")
    error = csv_plotter.fit_quadratic()
    error2 = csv_plotter.fit_gaussian()
    csv_plotter = CSVPlotter("fit_curve.csv")
    chi_squared = csv_plotter.fit_general()
    print("Chi-cuadrado del ajuste general:", chi_squared)
    print("Error del ajuste cuadrático:", error)
    print("Error del ajuste gaussiano:", error2)
