import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import plotly.graph_objects as go

# Define a linear operator (e.g., projection)
A = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])

# Generate vectors
x, y, z = np.meshgrid(np.linspace(-1, 1, 5),
                      np.linspace(-1, 1, 5),
                      np.linspace(-1, 1, 5))
u, v, w = np.zeros_like(x), np.zeros_like(y), np.zeros_like(z)
for i in range(5):
    for j in range(5):
        for k in range(5):
            vec = np.array([x[i,j,k], y[i,j,k], z[i,j,k]])
            transformed = np.dot(A, vec)
            u[i,j,k], v[i,j,k], w[i,j,k] = transformed

# Plot
fig = go.Figure(data=go.Cone(x=x.flatten(), y=y.flatten(), z=z.flatten(),
                             u=u.flatten(), v=v.flatten(), w=w.flatten(),
                             colorscale='Viridis', sizemode="scaled"))
fig.update_layout(title="3D Linear Operator (Projection onto XZ-plane)")
fig.show()