import matplotlib.pyplot as plt
import numpy as np
import math


def f1(y):
    return math.sin(y)


def f2(y):
    return math.sin(math.sqrt(y))/(2*math.sqrt(y))


def acceptance_rejection(f, a, b, c, n=10000, func=np.random.uniform):
    i = 0
    lst = []
    j = 0
    while i < n:
        y = func(a, b)
        u = np.random.uniform(0, 1)
        if u <= f(y) / c:
            lst.append(y)
            i += 1
        j += 1
    return np.array(lst), i/j


a = acceptance_rejection(f1, 0, math.pi/2, c=1)
b = acceptance_rejection(f2, 0, math.pi**2/4, c=0.5)
print(a[1], b[1])

plt.hist(a[0], bins=50, density=True)
plt.show()

plt.hist(np.sqrt(b[0]), bins=50, density=True)
plt.show()
