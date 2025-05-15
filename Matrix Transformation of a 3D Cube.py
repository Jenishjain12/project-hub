import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cube = np.array([[i,j,k] for i in [0,1] for j in [0,1] for k in [0,1]])
A = np.array([[1, 0.5, 0], [0, 1, 0.5], [0.5, 0, 1]])  # Shear + scaling

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Original cube
ax.scatter(cube[:,0], cube[:,1], cube[:,2], c='b', s=100)
for edge in [[0,1,3,2,0], [4,5,7,6,4], [0,1,5,4,0], [2,3,7,6,2], [0,2,6,4,0]]:
    ax.plot3D(cube[edge,0], cube[edge,1], cube[edge,2], 'b')

# Transformed cube
transformed = cube @ A.T
ax.scatter(transformed[:,0], transformed[:,1], transformed[:,2], c='r', s=100)
for edge in [[0,1,3,2,0], [4,5,7,6,4], [0,1,5,4,0], [2,3,7,6,2], [0,2,6,4,0]]:
    ax.plot3D(transformed[edge,0], transformed[edge,1], transformed[edge,2], 'r')

ax.set_title("3D Linear Transformation: Cube → Parallelepiped")
plt.show()