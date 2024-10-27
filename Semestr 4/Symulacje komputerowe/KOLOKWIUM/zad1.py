import numpy as np
import matplotlib.pyplot as plt


def GEN(N):
    z = np.zeros(N)
    for i in range(N):
        while True:
            u1 = np.random.uniform(0, 1)
            u2 = np.random.uniform(0, 4 / np.pi)
            if u2 <= f(u1):
                z[i] = u1
                break
    return z


def f(x):
    return 4 / np.pi * np.sqrt(1-x ** 2)


N = 10 ** 5
z = GEN(N)
x = np.linspace(0, 1, N)
y = f(x)

plt.hist(z, density=True)
plt.plot(x, y)
plt.show()
