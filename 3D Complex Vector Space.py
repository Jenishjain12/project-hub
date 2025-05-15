import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Complex state vector: α|0⟩ + β|1⟩
α = 0.6 + 0.4j
β = 0.1 - 0.7j
vec = np.array([α, β])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot real and imaginary components
ax.quiver(0, 0, 0, np.real(α), np.real(β), 0, color='b', label='Real Part')
ax.quiver(0, 0, 0, np.imag(α), np.imag(β), 0, color='r', label='Imaginary Part')
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
ax.set_title("Complex Quantum State in 3D")
plt.legend()
plt.show()