import matplotlib.pyplot as plt
import numpy as np


def normal_uniform_ratio_method(n):
    x = np.zeros(n)
    y = np.zeros(n)

    i = 0
    while i < n:
        a = np.random.uniform(0, 1)
        b = np.random.uniform(-1, 1)
        if np.sqrt(2*np.pi) * a ** 2 <= np.exp(-b ** 2 / (2 * a ** 2)):
            x[i] = a
            y[i] = b
            i += 1
    return y / x


def normal_density(miu, sigma, n=1000):
    x = np.linspace(-3*sigma + miu, 3*sigma + miu, n)
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(- (x - miu) ** 2 / (2 * sigma ** 2))
    return x, y


def main():
    miu = 0
    sigma = 1
    n = 10000
    z = normal_uniform_ratio_method(n)
    x, y = normal_density(miu, sigma, n)

    plt.hist(z, density=True, bins=50)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
