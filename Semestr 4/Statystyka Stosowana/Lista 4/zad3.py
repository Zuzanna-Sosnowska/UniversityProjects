import numpy as np
from matplotlib import pyplot as plt


def arithmetic_average(x):
    return np.sum(x)/len(x)


def variance_estimator(x, ver=True):
    average = arithmetic_average(x)
    if ver:
        return np.sum(np.power(x - average, 2))/len(x)
    else:
        return np.sum(np.power(x - average, 2))/(len(x) - 1)


def lognormal_variance(miu, sigma):
    return np.exp(2*miu + sigma**2) * (np.exp(sigma**2) - 1)


if __name__ == '__main__':
    miu = 3
    sigma = 1
    n = 10000
    arr1 = []
    arr2 = []
    for i in range(n):
        u = lognormal_variance(miu, sigma)
        x = np.random.lognormal(miu, sigma, n)
        arr1.append(u - variance_estimator(x))
        arr2.append(u - variance_estimator(x, False))
    v = np.linspace(0, n, n)

    plt.plot(v, arr1)
    plt.show()

    plt.plot(v, arr2)
    plt.show()
