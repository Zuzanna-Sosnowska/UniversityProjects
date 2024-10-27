import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def cauchy_uniform_ratio_method(n):
    x = np.zeros(n)
    y = np.zeros(n)

    i = 0
    while i < n:
        a = np.random.uniform(0, 1)
        b = np.random.uniform(-1, 1)
        if a**2 + b**2 <= 1:
            x[i] = a
            y[i] = b
            i += 1
    return y / x


def cauchy_density(x0, gamma, n=1000):
    x = np.linspace(x0 - 10 * gamma, x0 + 10 * gamma, n)
    y = 1 / (np.pi * gamma * (1 + ((x - x0) / gamma) ** 2))
    return x, y


def main():
    x0 = 0
    gamma = 1
    n = 10000
    z = cauchy_uniform_ratio_method(n)
    z = [i for i in z if i > -10 and i < 10]
    x, y = cauchy_density(x0, gamma, n)

    plt.hist(z, density=True, bins=75)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
