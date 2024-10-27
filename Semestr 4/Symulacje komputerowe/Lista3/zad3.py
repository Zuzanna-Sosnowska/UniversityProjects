import matplotlib.pyplot as plt
import numpy as np
import random


def exp_distribution(lambd=1):
    u = np.random.uniform(0, 1)
    return -1 / lambd * np.log(u)


def half_normal_distribution(c, lambd=1, n=1000):
    i = 0
    arr = []
    while i < n:
        y = exp_distribution(lambd)
        u = np.random.uniform(0, 1)
        if u <= abs(1 / (2 * np.pi) * np.exp(-y**2 / 2))/(c * lambd * np.exp(-lambd * y)):
            i += 1
            arr.append(y)
    return arr


def normal_distribution(c, n=1000, lambd=1):
    arr = []
    i = 0
    counter = 0
    while i < n:
        counter += 1
        u = random.random()
        if u <= 0.5:
            while u != 1:
                y = exp_distribution(lambd)
                a = np.random.uniform(0, 1)
                if a <= (1 / (2 * np.pi) * np.exp(-(y ** 2) / 2)) / (c * 0.5 * lambd * np.exp(-lambd * y)):
                    u = 1
                    i += 1
                    arr.append(y)
        else:
            while u != 1:
                y = -exp_distribution(lambd)
                p = abs(y)
                a = np.random.uniform(0, 1)
                if a <= (1 / (2 * np.pi) * np.exp(-(p ** 2) / 2)) / (c * 0.5 * lambd * np.exp(-lambd * p)):
                    i += 1
                    u = 1
                    arr.append(y)

    return arr


def normal_dist_density(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)


arr = normal_distribution(1, 100000)
x = np.linspace(-5, 5, 1000)
y = normal_dist_density(x)

plt.hist(arr, density=True, bins=100)
plt.plot(x, y, color='r')
plt.legend(['Teoretyczna gęstość', 'Akceptacja-odrzucenie'], loc="upper right")
plt.show()
