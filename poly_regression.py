import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# THIS CODE DOESN'T WORK, WILL FIX LATER


X = np.arange(0,100,0.5).reshape(200,1)
Y = X ** 2  + np.random.randn(200,1) * 200 + np.random.randn(200,1) * 20

def gradient_descent(a_now,b_now, c_now, learning_rate):

    a_grad = 0
    b_grad = 0
    c_grad = 0

    n = X.shape[0]

    for i in range(n):
        x = X[i]
        y = Y[i]
        
        a_grad += (2/n) * (-(x**2)) * (y - (a_grad*(x**2)+b_grad*x+c_grad))
        b_grad += (2/n) * (-x) * (y - (a_grad*(x**2)+b_grad*x+c_grad))
        c_grad += -(2/n) * (y - (a_grad*(x**2)+b_grad*x+c_grad))
                                    

    a = a_now - learning_rate * a_grad
    b = b_now - learning_rate * b_grad
    c = c_now - learning_rate * c_grad

    return a,b,c

a = 0
b = 0
c = 0
epoch = 100

L = 0.0001

for i in range(epoch):
    if i % 10 == 0:
        print(f'Iteration : {i}')

    a,b,c = gradient_descent(a,b,c,L)

print(a,b,c)
    
f = lambda x: a*(x**2) + b * x + c

plt.scatter(X,Y, color = 'black')
plt.plot(X,f(X), color = 'red')
plt.show()