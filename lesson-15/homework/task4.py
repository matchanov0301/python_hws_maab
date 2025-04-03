import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

x_values = np.random.uniform(0, 10, 100)
y_values = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)

plt.figure(figsize=(8, 6))
plt.scatter(x_values, y_values, c=colors, cmap='viridis')

plt.title("Scatter Plot of 100 Random Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.colorbar(label="Color Intensity")
plt.show()
