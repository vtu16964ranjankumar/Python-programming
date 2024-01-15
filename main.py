import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([0, 5, 10, 15, 20, 25])
y = np.array([100, 111, 119, 132, 140, 151])

# Perform linear regression using the least squares method
coefficients = np.polyfit(x, y, 1)
slope, intercept = coefficients

# Generate y values for the best-fitting line
y_fit = slope * x + intercept

# Plot the original data points and the best-fitting line
plt.scatter(x, y, label='Data points')
plt.plot(x, y_fit, color='red', label=f'Best-fitting line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('best-fitting straight line using Least Squares Method')
plt.show()

# Print the slope and y-intercept
print(f"Slope (m): {slope}")
print(f"Y-intercept (b): {intercept}")
