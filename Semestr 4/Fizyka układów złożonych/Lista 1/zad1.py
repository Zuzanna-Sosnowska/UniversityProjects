import matplotlib.pyplot as plt
import numpy as np


def f(x, a):
    while True:
        x = a * x * (1 - x)
        yield x


if __name__ == '__main__':
    x_0 = 0.97
    a = 3.5
    n = 50
    g = f(x_0, a)
    x = np.linspace(0, n, n)
    y = [next(g) for i in range(n)]

    plt.plot(x, y)
    plt.show()
