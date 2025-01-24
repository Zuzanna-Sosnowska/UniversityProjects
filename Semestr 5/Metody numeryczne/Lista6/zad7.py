import numpy as np

x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
f_x = np.array([0.000000, 0.078348, 0.138910, 0.192916, 0.244981])

x0 = 0.2

h = 0.1

def f(x):
    i = np.where(abs(x - x0) < 1.e-16)[0]
    return f_x[i]

print(f(x+2*h), f(x+h), f(x), f(x-h), f(x-2*h))

