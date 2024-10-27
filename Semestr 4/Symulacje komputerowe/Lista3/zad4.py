import matplotlib.pyplot as plt
import numpy as np
import random
import math


def uniform_ratio_method(h, c=1, n=1000):
    arr = []
    i = 0
    while i < n:
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if 0 < x < h(y/x):
            arr.append(c * y/x)
            i += 1
    return arr


def h(x):
    return 1/(1 + x * x)


def k(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)


# plt.hist(uniform_ratio_method(h), density=True)
# plt.show()
#
# plt.hist(uniform_ratio_method(k), density=True)
# plt.show()


def cauchy_ratio_method(n=1000):
    arr = []
    i = 0
    while i < n:
        x = random.random()
        y = random.random()
        if 0 < x*x < 1 - y*y:
            arr.append(y/x)
            i += 1
    return arr


def normal_ratio_method(n=1000):
    arr = []
    i = 0
    while i < n:
        x = random.random()
        y = random.random()
        if 0 < 2 * y * y < (x * x)/(math.log(x)):
            arr.append(y/x)
            i += 1
    return arr


plt.hist(normal_ratio_method(), density=True)
plt.show()
