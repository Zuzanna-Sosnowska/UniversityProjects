import matplotlib.pyplot as plt
import numpy as np


def levy_process(alpha, T, n):
    times = np.zeros(n)
    val = np.zeros(n)
    dt = T/n
    w = 0
    for i in range(n - 1):
        delta_w = dt ** (1 / alpha) * stable_random(alpha, 0, 1)
        w += delta_w
        val[i+1] = w
        times[i+1] = (i+1) * dt
    return times, val


def stable_random(alpha, beta, size=1):
    """
    Generuje zmienne losowe z rozkładu stabilnego.

    Parametry:
    alpha : float - parametr stabilności (0 < alpha <= 2)
    beta : float - parametr asymetrii (-1 <= beta <= 1)
    size : int - liczba zmiennych losowych do wygenerowania

    Zwraca:
    numpy.ndarray - tablica zmiennych losowych
    """
    if alpha <= 0 or alpha > 2:
        raise ValueError("alpha must be in (0, 2]")
    if abs(beta) > 1:
        raise ValueError("beta must be in [-1, 1]")

    U = np.pi * (np.random.rand(size) - 0.5)
    W = np.random.exponential(1, size)

    gamma = -beta * np.tan(np.pi * alpha / 2)

    if alpha != 1:
        eta = (1 / alpha) * np.arctan(gamma)
        factor = (1 + gamma ** 2) ** (1 / (2 * alpha))
        X = factor * (np.sin(alpha * (U + eta)) / (np.cos(U) ** (1 / alpha))) * \
            (np.cos(U - alpha * (U + eta)) / W) ** ((1 - alpha) / alpha)
    else:
        eta = np.pi / 2
        X = (1 / eta) * ((np.pi / 2 + beta * U) * np.tan(U) - beta * np.log(
            (np.pi / 2) * W * np.cos(U) / (np.pi / 2 + beta * U)))

    return X


if __name__ == '__main__':
    n = 1000
    x, y = levy_process(1.1, 100, 10000)

    plt.plot(x, y)
    plt.show()

