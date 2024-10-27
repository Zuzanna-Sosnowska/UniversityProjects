import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zad1


def normal_distribution(miu=2, sigma=2, n=2000):
    return np.random.normal(loc=miu, scale=sigma, size=n)


def normal_dist_density(x, miu=2, sigma=2):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-miu)**2/(2*sigma**2))


def y_distribution(miu=0, sigma=2, n=2000):
    return np.abs(normal_distribution(miu, sigma, n) - miu)


def y_dist_density(x, miu=2):
    return normal_dist_density(x + miu) + normal_dist_density(miu - x)


def odch_przec_od_wart_sred(x):
    return 1/len(x) * sum(np.abs(x - zad1.arithmetic_average(x)))


def expected_value_y(sigma=2, n=2000):
    return np.array([np.sqrt(2/np.pi)*sigma for i in range(n)])


if __name__ == '__main__':

    y = np.arange(10, 10000, 10)
    a = []
    for n in y:
        x = normal_distribution(2, 2, n)
        a.append(odch_przec_od_wart_sred(x))
    plt.plot(y, a)

    plt.plot(y, expected_value_y(2, len(y)))
    plt.show()


