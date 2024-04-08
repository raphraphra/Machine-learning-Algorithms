# BUILDING A GRADIENT DESCENT; FOR FUN IG?

# The point is to reach a local minimum
#first, compute a function, then its derivative
#define a learning rate.
# then, until you reach a minimum, define a point and update its position based on the derivative

#to animate such a process, use plt.pause(delay), then plt.clf() => clear figure

import matplotlib.pyplot as plt
import numpy as np

def y_function(x):
    return 2*np.sin(x)

def y_derivative(x):
    return 2*np.cos(x)

current_pos = (0, y_function(0))

X = np.arange(-10,10,0.1)
Y = y_function(X)

learning_rate = 0.01

for _ in range(300):
    
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    
    current_pos = (new_x, new_y)
    
    plt.plot(X,Y)
    plt.scatter(current_pos[0],current_pos[1], c = 'red')
    plt.pause(0.001)
    plt.clf()
