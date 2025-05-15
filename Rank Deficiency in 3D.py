import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])  # Projection onto XY-plane

# Generate random points
points = np.random.randn(50, 3)
transformed = points @ A.T

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2], c='b', label='Original')
ax.scatter(transformed[:,0], transformed[:,1], transformed[:,2], c='r', label='Transformed')
ax.set_title("Rank-Deficient Matrix Collapses 3D → 2D")
plt.legend()
plt.show()