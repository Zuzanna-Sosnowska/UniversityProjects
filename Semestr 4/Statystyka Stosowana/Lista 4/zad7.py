import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def x_distribution(theta, n=1000):
    u = np.random.uniform(0, 1, n)
    return theta - np.log(u)


def density_plot(theta, n=1000):
    x = np.linspace(theta, theta*3, n)
    y = np.exp(-(x-theta))
    return x, y


def dist_plot(theta, n=1000):
    x = np.linspace(theta, theta*3, n)
    y = 1 - np.exp(-(x-theta))
    return x, y


def main():
    n = 1000
    theta = 5
    x1, y1 = density_plot(theta, n)
    v = x_distribution(theta, n)
    plt.hist(v, density=True)
    plt.plot(x1, y1)
    plt.show()

    x2, y2 = dist_plot(theta, n)

    sns.ecdfplot(v)
    plt.plot(x2, y2)
    plt.show()

    u = np.zeros(n)
    for i in range(n):
        u[i] = np.min(x_distribution(theta, n))

    np.sort(u)
    plt.boxplot(u)
    plt.show()


if __name__ == '__main__':
    main()
