import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[3, 0, 0], [0, 2, 0.5], [0, 0.5, 2]])  # Symmetric matrix
eigvals, eigvecs = np.linalg.eig(A)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot eigenvectors
origin = np.zeros(3)
for vec in eigvecs.T:
    ax.quiver(*origin, *vec, color=np.random.rand(3), arrow_length_ratio=0.1)

ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
ax.set_title("Eigenvectors of a 3D Matrix (Quantum Observable Directions)")
plt.show()