import numpy as np
import matplotlib.pyplot as plt

d0 = lambda x: x**3

start = -2
finish = 2
step = 0.01

y_bottom = -5
y_top = 5

def derivative(f):

    return lambda x: (f(x+0.001) - f(x)) / 0.001

d1 = derivative(d0)
d2 = derivative(d1)
d3 = derivative(d2)
d4 = derivative(d3)
d5 = derivative(d4)

taylor = lambda x,a: d0(a) + d1(a)*(x - a) + d2(a) * ((x-a)**2) / 2 + d3(a) * ((x-a)**3) / 6 + d4(a) * ((x-a)**4) / 24 + d5(a) * ((x-a)**5) / 120

a = start

values = np.arange(start,finish,0.01)


while a <= finish:
     
    plt.plot(values, d0(values), c="purple")
    plt.plot(values, taylor(values, a), c='green')
    plt.scatter(a, d0(a), c="red")
    plt.xlim(start, finish)
    plt.ylim(y_bottom, y_top)
    plt.pause(0.001)
    plt.clf()
    a += step

    
