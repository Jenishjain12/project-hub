import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from ipywidgets import interact, FloatSlider

def plot_3d_transform(a11=1, a12=0, a13=0,
                      a21=0, a22=1, a23=0,
                      a31=0, a32=0, a33=1):
    A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0],
                     [0,0,1], [1,0,1], [1,1,1], [0,1,1]])
    transformed = np.dot(cube, A.T)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(cube[:,0], cube[:,1], cube[:,2], color='blue', s=100)
    ax.scatter3D(transformed[:,0], transformed[:,1], transformed[:,2], color='red', s=100)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    plt.title("Interactive 3D Matrix Transformation")
    plt.show()

interact(plot_3d_transform,
         a11=FloatSlider(min=-2, max=2, step=0.1, value=1),
         a12=FloatSlider(min=-2, max=2, step=0.1, value=0),
         a13=FloatSlider(min=-2, max=2, step=0.1, value=0),
         a21=FloatSlider(min=-2, max=2, step=0.1, value=0),
         a22=FloatSlider(min=-2, max=2, step=0.1, value=1),
         a23=FloatSlider(min=-2, max=2, step=0.1, value=0),
         a31=FloatSlider(min=-2, max=2, step=0.1, value=0),
         a32=FloatSlider(min=-2, max=2, step=0.1, value=0),
         a33=FloatSlider(min=-2, max=2, step=0.1, value=1))