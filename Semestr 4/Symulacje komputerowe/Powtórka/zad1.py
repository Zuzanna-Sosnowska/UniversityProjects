import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def f(x):
    return (4 * x) ** (-0.5) * np.exp(-np.sqrt(x))


def F(x):
    return 1 - np.exp(-np.sqrt(x))


def f_density_distribution(n=1000):
    u = np.random.uniform(0, 1, n)
    return (np.log(1-u)) ** 2

def main():
    n = 10000
    a = f_density_distribution(n)
    b = [i for i in a if i <= 10]
    x1 = np.linspace(0.05, 10, n)
    x2 = np.linspace(0, 60, n)
    y1 = f(x1)
    y2 = F(x2)

    plt.hist(b, bins=30, density=True, label='histogram')
    plt.plot(x1, y1, color='r', label='teoretyczna gęstość')
    plt.legend()
    plt.show()

    sns.ecdfplot(a, label='jądrowy estymator dystrybuanty')
    plt.plot(x2, y2, color='r', label='teoretyczna dystrybuanta')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
