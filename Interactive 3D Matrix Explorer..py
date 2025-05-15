import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interact, FloatSlider

def plot_matrix(a11=1, a12=0, a13=0,
               a21=0, a22=1, a23=0,
               a31=0, a32=0, a33=1):
    A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
    sphere = np.array([[np.sin(θ)*np.cos(φ), np.sin(θ)*np.sin(φ), np.cos(θ)] 
                      for θ in np.linspace(0, np.pi, 20) 
                      for φ in np.linspace(0, 2*np.pi, 20)])
    transformed = sphere @ A.T
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(sphere[:,0], sphere[:,1], sphere[:,2], c='b', alpha=0.2)
    ax.scatter(transformed[:,0], transformed[:,1], transformed[:,2], c='r', alpha=0.5)
    ax.set_title("Matrix Transforming Unit Sphere")
    plt.show()

interact(plot_matrix,
         a11=(-2, 2, 0.1), a12=(-2, 2, 0.1), a13=(-2, 2, 0.1),
         a21=(-2, 2, 0.1), a22=(-2, 2, 0.1), a23=(-2, 2, 0.1),
         a31=(-2, 2, 0.1), a32=(-2, 2, 0.1), a33=(-2, 2, 0.1))

