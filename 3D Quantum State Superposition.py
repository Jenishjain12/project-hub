import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from qiskit.visualization import plot_bloch_vector

# Superposition states
states = [
    [1/np.sqrt(2), 0, 1/np.sqrt(2)],  # (|0⟩ + |1⟩)/√2
    [1/np.sqrt(2), 1/np.sqrt(2), 0],   # (|0⟩ + i|1⟩)/√2
    [0, 0, -1]                         # |1⟩ phase flipped
]

fig = plt.figure(figsize=(15, 5))
for i, state in enumerate(states, 1):
    ax = fig.add_subplot(1, 3, i, projection='3d')
    plot_bloch_vector(state, ax=ax)
    ax.set_title(f"State {i}")
plt.tight_layout()
plt.show()