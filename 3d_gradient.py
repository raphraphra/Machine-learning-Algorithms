import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# THIS CODE DOESN'T WORK, WILL FIX LATER

def z_function(x,y):
    return np.sin(x) + np.sin(y)

def gradient_z(x,y):
    return np.cos(x), np.cos(y)

x = np.arange(-10,10,0.5)
y = np.arange(-10,10,0.5)

X, Y = np.meshgrid(x,y)
Z = z_function(X,Y)

ax = plt.subplot(projection = '3d', computed_zorder = False)

pos = (8,7,z_function(8,7))
learning_rate = 0.005

for i in range(100):
    X_dvt, Y_dvt = gradient_z(pos[0],pos[1])
    new_x, new_y = pos[0] - learning_rate * X_dvt, pos[1] - learning_rate * Y_dvt
    pos = (new_x, new_y, z_function(new_x,new_y))

    print(pos)
    ax.plot_surface(X,Y,Z, cmap = 'viridis')
    plt.scatter(pos[0],pos[1], pos[2], c = 'red')
    plt.pause(0.001)
    ax.clear()