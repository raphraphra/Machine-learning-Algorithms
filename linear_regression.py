import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


X = np.arange(0,100,0.5).reshape(200,1)
Y = X * 2  + np.random.randn(200,1) * 8 + np.random.randn(200,1) * 20

def gradient_descent(m_now,b_now,learning_rate):

    m_grad = 0
    b_grad = 0

    n = X.shape[0]

    for i in range(n):
        x = X[i]
        y = Y[i]
        m_grad += -(2/n) * x * (y - (m_now * x + b_now))
        b_grad += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - learning_rate * m_grad
    b = b_now - learning_rate * b_grad

    return m,b

m = 0
b = 0
epoch = 700

L = 0.0001

for i in range(epoch):
    if i % 50 == 0:
        print(f'Iteration : {i}')
    m, b = gradient_descent(m,b,L)

print(m,b)
    
f = lambda x: m*x + b

plt.scatter(X,Y, color = 'black')
plt.plot(X,f(X), color = 'red', lw = 5)
plt.show()