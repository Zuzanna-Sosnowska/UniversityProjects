import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy


# Rozkład wykładniczy
def exp(lamb, n=1):
    u = np.random.rand(n)
    return -1/lamb * np.log(u)


def exp_dist(lamb, n=1):
    x = np.linspace(0, n)
    return x, 1 - np.exp(-lamb*x)


def exp_density(lamb, n=1):
    x = np.linspace(0, n)
    return x, lamb * np.exp(-lamb*x)


def normal_distribution(miu, sigma, n=1):
    u = np.random.rand(n)
    return miu + np.sqrt(2) * sigma * scipy.special.erfinv(2 * u - 1)


def normal_density(miu, sigma, n=1000):
    x = np.linspace(-3*sigma + miu, 3*sigma + miu, n)
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(- (x - miu) ** 2 / (2 * sigma ** 2))
    return x, y


def normal_dist(miu, sigma, n=1000):
    x = np.linspace(-3 * sigma, 3 * sigma, n)
    y = 0.5 * (1 + scipy.special.erf((x - miu) / (sigma * np.sqrt(2))))
    return x, y


def cauchy_distribution(x0, gamma, n=1):
    u = np.random.uniform(0, 1, n)
    return x0 + gamma * np.tan(np.pi * (u - 0.5))


def cauchy_dist(x0, gamma, n=1000):
    x = np.linspace(x0 - 10*gamma, x0 + 10*gamma, n)
    y = 1 / np.pi * np.arctan((x - x0) / gamma) + 0.5
    return x, y


def cauchy_density(x0, gamma, n=1000):
    x = np.linspace(x0 - 10 * gamma, x0 + 10 * gamma, n)
    y = 1 / (np.pi * gamma * (1 + ((x - x0) / gamma) ** 2))
    return x, y


def plot1(lambd, n):
    x = exp(lambd, n)
    x_dist, u_dist = exp_dist(lambd, 5)
    x_density, u_density = exp_density(lambd, 5)

    sns.ecdfplot(x)
    plt.plot(x_dist, u_dist)
    plt.show()

    plt.hist(x, density=True, bins=100)
    plt.plot(x_density, u_density)
    plt.show()


def plot2(miu, sigma, n):
    a = normal_distribution(miu, sigma, n)
    x2, y2 = normal_density(miu, sigma, n)
    x3, y3 = normal_dist(miu, sigma, n)
    plt.hist(a, density=True, bins=20)
    plt.plot(x2, y2)
    plt.show()

    sns.ecdfplot(a)
    plt.plot(x3, y3)
    plt.show()


def plot3(x0, gamma, n):
    a = cauchy_distribution(0, 1, n)
    a = [i for i in a if i > -10 and i < 10]
    x1, y1 = cauchy_dist(x0, gamma, n)
    x2, y2 = cauchy_density(x0, gamma, n)

    plt.hist(a, density=True, bins=50)
    plt.xlim(x0 - 10 * gamma, x0 + 10 * gamma)
    plt.plot(x2, y2)
    plt.show()

    sns.ecdfplot(a)
    plt.plot(x1, y1)
    plt.show()


def main():
    n = 10000

    lambd = 2
    plot1(lambd, n)

    miu, sigma = 0, 1
    plot2(miu, sigma, n)

    x0, gamma = 0, 1
    plot3(x0, gamma, n)


if __name__ == '__main__':
    main()
