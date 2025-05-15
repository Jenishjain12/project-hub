import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define planes
x, y = np.meshgrid(range(-5, 6), range(-5, 6))
z1 = (6 - 2*x - 3*y) / 4  # 2x + 3y + 4z = 6
z2 = (3 - x + y) / 2       # x - y + 2z = 3
z3 = (5 - x - 2*y) / 3     # x + 2y + 3z = 5

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1, alpha=0.5, color='r')
ax.plot_surface(x, y, z2, alpha=0.5, color='g')
ax.plot_surface(x, y, z3, alpha=0.5, color='b')
ax.set_title("3D Linear System: Unique Solution (3 Planes Intersecting at a Point)")
plt.show()