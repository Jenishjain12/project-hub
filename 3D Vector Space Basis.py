import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

basis = np.eye(3)
A = np.array([[1, 0.5, 0], [0.5, 1, 0], [0, 0, 2]])  # Transformation

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Original basis (i, j, k)
colors = ['r', 'g', 'b']
for i, vec in enumerate(basis):
    ax.quiver(0, 0, 0, *vec, color=colors[i], label=f'Original e_{i}')

# Transformed basis
for i, vec in enumerate(basis @ A.T):
    ax.quiver(0, 0, 0, *vec, color=colors[i], linestyle='--', label=f'Transformed e_{i}')

ax.legend()
ax.set_title("Basis Vectors Before/After Transformation")
plt.show()