import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

class ReversibleStorage:
    def __init__(self, max_data_points=5):
        self.data_points = []  # Store (x, y) pairs
        self.max_data_points = max_data_points

    def add_data(self, x, y):
        """ Adds a new data point and removes the oldest if limit is exceeded """
        self.data_points.append((x, y))
        if len(self.data_points) > self.max_data_points:
            self.data_points.pop(0)  # Remove the oldest entry

    def get_interpolation_function(self):
        """ Creates a polynomial function using Lagrange interpolation """
        if len(self.data_points) < 2:
            return None  # Not enough data
        
        x_vals, y_vals = zip(*self.data_points)  # Separate x and y
        return lagrange(x_vals, y_vals)  # Generate polynomial

    def reconstruct_data(self, x_old):
        """ Recovers old data using interpolation """
        poly = self.get_interpolation_function()
        if poly is None:
            return None  # Not enough data
        return poly(x_old)  # Estimate value at x_old

# Example Usage
storage = ReversibleStorage(max_data_points=5)

# Add some data points
storage.add_data(1, 10)
storage.add_data(2, 20)
storage.add_data(3, 30)
storage.add_data(4, 40)
storage.add_data(5, 50)

print("Stored Data:", storage.data_points)

# Adding new data (deletes oldest value)
storage.add_data(6, 60)
print("Updated Data (Oldest Removed):", storage.data_points)

# Recover deleted data (approximate value for x=1)
x_old = 1
recovered_value = storage.reconstruct_data(x_old)

print(f"Reconstructed value for x={x_old}: {recovered_value:.2f}")

# Visualization
x_vals = np.linspace(1, 6, 100)  # Generate x values for the plot
poly = storage.get_interpolation_function()

if poly:
    y_vals = poly(x_vals)
    plt.plot(x_vals, y_vals, label="Interpolated Function", linestyle="--")
    plt.scatter(*zip(*storage.data_points), color='red', label="Stored Data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Reconstructing Deleted Data using Polynomial Interpolation")
    plt.show()
