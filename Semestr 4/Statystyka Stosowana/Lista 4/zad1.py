import matplotlib.pyplot as plt
import numpy as np


def arithmetic_mean(arr):
    return np.sum(arr) / len(arr)


def log_normal_mean(miu=0.0, sigma=1.0):
    return np.exp((sigma**2)/2 + miu)


def log_normal_var(miu=0.0, sigma=1.0, n=1000):
    return np.exp(2*miu+sigma**2)*(np.exp(sigma**2) - 1)/n


if __name__ == '__main__':
    n = 1000
    miu = 1
    sigma = 2
    estimator = []
    for i in range(n):
        a = np.random.lognormal(miu, sigma, n)
        estimator.append(arithmetic_mean(a))

    estimator = np.sort(estimator)

    print(arithmetic_mean(estimator))
    print(log_normal_mean(miu, sigma))

    print(np.var(estimator))
    print(log_normal_var(miu, sigma, n))

    plt.boxplot(estimator)
    plt.axhline(y=arithmetic_mean(estimator), color='r', linestyle='-')
    plt.show()


