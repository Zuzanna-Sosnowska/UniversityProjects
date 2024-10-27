import matplotlib.pyplot as plt
import numpy as np


def mean_estim(x, ver=True):
    if ver:
        return np.sum(x)/len(x)
    else:
        return np.sum(x) / (len(x) - 1)


def variance_estim(x, ver=True):
    if ver:
        return np.sum((x-mean_estim(x))**2)/len(x)
    else:
        return np.sum((x-mean_estim(x))**2)/(len(x) - 1)


if __name__ == '__main__':
    miu = 2
    sigma = 5
    n = 500
    N = 100
    M = 1000
    a = np.zeros(M)
    b = np.zeros(M)
    y = np.linspace(0, M, M)
    for j in range(M):
        miu_est = np.zeros(N)
        sigma_est = np.zeros(N)
        for i in range(N):
            x = np.random.normal(loc=miu, scale=sigma, size=n)
            miu_est[i] = mean_estim(x, False)
            sigma_est[i] = variance_estim(x, False)
        b[j] = 1 / N * np.sum(miu_est - miu)
        a[j] = 1 / N * np.sum(sigma_est - sigma**2)

    a_sr = mean_estim(a)
    b_sr = mean_estim(b)
    plt.plot(y, a)
    plt.title("Błąd miu")
    plt.axhline(y=a_sr, color='r')
    plt.show()
    plt.plot(y, b)
    plt.title("Błąd sigma")
    plt.axhline(y=b_sr, color='r')
    plt.show()
