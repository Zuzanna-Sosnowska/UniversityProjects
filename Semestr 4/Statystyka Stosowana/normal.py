import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss


def norm_dist(mu, sigma, n=1000):
    """
    Funkcja zwraca wartości x i y dla dystrybuanty
    :param mu: wartość oczekiwana
    :param sigma: odchylenie standardowe
    :param n: długość tablicy
    :return:
    """
    x = np.linspace(mu -5*sigma, mu + 5*sigma, n)
    return x, ss.norm.cdf(x, mu, sigma)


def norm_density(mu, sigma, n=1000):
    """
    Funkcja zwraca wartości x i y dla dystrybuanty
    :param mu: wartość oczekiwana
    :param sigma: odchylenie standardowe
    :param n: długość tablicy
    :return:
    """
    x = np.linspace(mu - 5*sigma, mu + 5*sigma, n)
    return x, ss.norm.pdf(x, mu, sigma)


def lognorm_dist(mu, sigma, n=1000):
    x = np.linspace(mu - 10*sigma, mu + 10*sigma, n)
    return x, ss.lognorm.cdf(x, sigma, scale=np.exp(mu))


def lognorm_density(mu, sigma, n=1000):
    x = np.linspace(0, 10, n)
    return x, ss.lognorm.pdf(x, sigma, scale=np.exp(mu))


x, y = lognorm_density(0, 1)
plt.plot(x, y)
plt.show()
