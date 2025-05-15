import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from qiskit.visualization import plot_bloch_vector

# Quantum state |ψ⟩ = α|0⟩ + β|1⟩ (normalized: |α|² + |β|² = 1)
plot_bloch_vector([1, 0, 0], title="Qubit State |0⟩")  # |0⟩
plot_bloch_vector([0, 0, 1], title="Qubit State |1⟩")  # |1⟩
plot_bloch_vector([1/np.sqrt(2), 0, 1/np.sqrt(2)], title="Superposition (|0⟩ + |1⟩)/√2")
plt.tight_layout()
plt.show()