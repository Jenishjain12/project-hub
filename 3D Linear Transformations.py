import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define cube vertices
cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0],
                 [0,0,1], [1,0,1], [1,1,1], [0,1,1]])

# Transformation matrix (scaling + shear)
A = np.array([[2, 0.5, 0], [0.5, 1, 0], [0, 0, 3]])

# Apply transformation
transformed_cube = np.dot(cube, A.T)

# Plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Original cube (wireframe)
ax.scatter3D(cube[:,0], cube[:,1], cube[:,2], color='blue', s=100)
for i in range(4):
    ax.plot3D(*zip(cube[i], cube[(i+1)%4]), 'b-')
    ax.plot3D(*zip(cube[i+4], cube[(i+1)%4+4]), 'b-')
    ax.plot3D(*zip(cube[i], cube[i+4]), 'b-')

# Transformed cube (solid)
transformed_faces = [[transformed_cube[j] for j in [0,1,2,3]],
                     [transformed_cube[j] for j in [4,5,6,7]],
                     [transformed_cube[j] for j in [0,1,5,4]],
                     [transformed_cube[j] for j in [2,3,7,6]],
                     [transformed_cube[j] for j in [1,2,6,5]],
                     [transformed_cube[j] for j in [0,3,7,4]]]
ax.add_collection3d(Poly3DCollection(transformed_faces, alpha=0.5, color='red'))

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.title("3D Transformation: Cube → Parallelepiped")
plt.show()