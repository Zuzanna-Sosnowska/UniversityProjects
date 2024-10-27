import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math


def geometrical_distribution(p, n=1):
    u = np.random.rand(n)
    x = np.ceil(np.log(1 - u)/np.log(1 - p))
    return x


def geometrical_dist(p, n):
    x = np.linspace(1, n, n)
    y = 1 - np.power(1-p, x)
    return x, y


def plot1():
    p = 0.2
    n = 1000
    n1 = 35
    a = geometrical_distribution(p, n)
    x, y = geometrical_dist(p, n1)

    sns.ecdfplot(a)
    for i in range(n1 - 1):
        plt.scatter(x[i], y[i], color='g')
        plt.plot([x[i], x[i + 1]], [y[i], y[i]], color='g')
        plt.scatter(x[i + 1], y[i], facecolors='none', color='g')
    plt.show()


def poisson_distribution(lambd, n=1):
    u = np.random.uniform(0, 1, n)
    y = np.zeros(n)
    for i in range(n):
        sum = 0
        while u[i] > sum:
            sum += math.exp(-lambd) * lambd ** y[i] / math.factorial(int(y[i]))
            y[i] += 1
            print(y[i])
    return y


def poisson_dist(lambd, n=100):
    x = np.linspace(1, n, n)
    y = np.zeros(n)
    val = 0
    for i in range(n):
        val += math.exp(-lambd) * lambd ** i / math.factorial(i)
        y[i] = val
    return x, y


def plot2():
    lambd = 10
    n = 1000
    a = poisson_distribution(lambd, n)
    x, y = poisson_dist(lambd, 2 * int(lambd))

    sns.ecdfplot(a)
    for i in range(2 * int(lambd) - 1):
        plt.scatter(x[i], y[i], color='r')
        plt.plot([x[i], x[i+1]], [y[i], y[i]], color='r')
        plt.scatter(x[i+1], y[i], facecolors='none', color='r')
    plt.show()


def main():
    plot1()
    plot2()


if __name__ == '__main__':
    main()
