import numpy as np


def polynomial(coef): return lambda x : sum(coef[i] * x ** i for i in range(len(coef)))


def st_dev(func, points):
    return np.sqrt(variance(func=func, points=points))


def variance(func, points):
    x, y = zip(*points)
    x, y = np.array(x), np.array(y)
    n = len(points)
    f_x = func(x)
    return 1 / n * np.sum(np.power(y - f_x, 2))


def mean_abs_dev(func, points):
    x, y = zip(*points)
    x, y = np.array(x), np.array(y)
    n = len(points)
    f_x = func(x)
    return 1 / n * np.sum(np.abs(y - f_x))


def norm(x):
    return np.sqrt(np.sum(x**2))