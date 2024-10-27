import matplotlib.pyplot as plt
import numpy as np


def acceptance_rejection(alpha, n=10000, function=np.random.uniform):
    i = 0
    C = alpha + 1
    lst = []
    j = 0
    while i < n:
        y = function()
        u = np.random.uniform(0, 1)
        if u <= y ** alpha / C:
            lst.append(y)
            i += 1
        j += 1
    return lst, i/j


def f(alpha, n=1000):
    x = np.linspace(0, 1, n)
    y = (alpha + 1) * np.power(x, alpha)
    return x, y


def main():
    # a = np.zeros(10)
    # for i in range(10):
    #     p = acceptance_rejection(i)
    #     a[i] = p[1]
    #
    # plt.plot(a)
    # plt.show()

    alpha = 3
    b = acceptance_rejection(alpha)
    x, y = f(alpha)
    plt.hist(b[0], bins=100, density=True)
    plt.plot(x, y, color='r')
    plt.show()


if __name__ == '__main__':
    main()
