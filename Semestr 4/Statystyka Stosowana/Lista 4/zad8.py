import matplotlib.pyplot as plt
import numpy as np


def arithmetic_mean(x):
    return sum(x)/len(x)


def median(x):
    x = np.sort(x)
    return x[len(x)//2]


if __name__ == '__main__':

    miu = 5
    sigma = 1
    p = 30
    n = [10*(i+1) for i in range(p)]
    m = 100
    mse1 = np.zeros(p)
    mse2 = np.zeros(p)
    l = 0
    for k in n:
        MSE1 = np.zeros(m)
        MSE2 = np.zeros(m)
        for j in range(m):
            u1 = np.zeros(k)
            u2 = np.zeros(k)
            for i in range(k):
                x = np.random.normal(loc=miu, scale=sigma, size=2*k+1)
                u1[i] = arithmetic_mean(x)
                u2[i] = median(x)
            np.sort(u1)
            np.sort(u2)
            MSE1[j] = 1/k * np.sum((miu-u1)*(miu-u1))
            MSE2[j] = 1/k * np.sum((miu-u2)*(miu-u2))
        mse1[l] = arithmetic_mean(MSE1)
        mse2[l] = arithmetic_mean(MSE2)
        l += 1

    plt.plot(n, mse1, label='arithmetic mean')
    plt.plot(n, mse2, label='median')
    plt.legend(loc='best')
    plt.show()
