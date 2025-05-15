import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define planes
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z1 = (6 - 2*X - 3*Y) / 4  # Plane 1: 2x + 3y + 4z = 6
Z2 = (3 - X + Y) / 2       # Plane 2: x - y + 2z = 3

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue', label='2x + 3y + 4z = 6')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='red', label='x - y + 2z = 3')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.legend()
plt.title("3D Planes: Unique Solution (Intersection Line)")
plt.show()