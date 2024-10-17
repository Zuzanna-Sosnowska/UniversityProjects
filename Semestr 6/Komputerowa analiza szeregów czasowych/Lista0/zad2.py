import matplotlib.pyplot as plt
import numpy as np


def random_y(miu=0, sigma=1, n=1000):
    return np.abs(np.random.normal(miu, sigma, n) - miu)


def estimator_MM(x):
    return np.sqrt(2*np.pi)/2 * np.mean(x)


def estimator_NW(x):
    return np.sqrt(1/len(x) * np.sum(np.power(x, 2)))


if __name__ == '__main__':
    miu = 2
    sigma = 3
    n = 1000
    m = 1000
    MM = np.zeros(m)
    NW = np.zeros(m)
    for i in range(m):
        y = random_y(miu, sigma, n)
        MM[i] = estimator_MM(y)
        NW[i] = estimator_NW(y)

    plt.boxplot([MM, NW], tick_labels=['MM', 'NW'])
    plt.axhline(y=sigma, linestyle='--', color='blue', label='sigma')
    plt.title(r'Porównanie estymatorów $\sigma$ wyznaczonych' + '\n' + 'metodą momentów i największej wiarogodności')
    plt.legend()
    plt.show()
