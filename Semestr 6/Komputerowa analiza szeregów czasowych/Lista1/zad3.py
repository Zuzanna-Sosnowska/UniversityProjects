import matplotlib.pyplot as plt
import numpy as np


def prosta_regresji(x, y):
    b1 = np.sum((x - np.mean(x))*(y - np.mean(y))) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b0, b1


if __name__ == '__main__':
    x = np.loadtxt('../Lista1/zad2_lista1.txt')
    y = np.loadtxt('../Lista1/zad3_lista1.txt')
    x = np.array(x)
    y = np.array(y)

    b0, b1 = prosta_regresji(x, y)
    x1 = np.linspace(-1, 10, 1000)
    y1 = b0 + b1 * x1

    plt.plot(x1, y1, color='red')
    plt.scatter(x, y)
    plt.show()
