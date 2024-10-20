import matplotlib.pyplot as plt
import numpy as np


def prosta_srednia_ruchoma(x, podstawa):
    p = int((podstawa - 1) / 2)
    t = np.zeros(len(x) - podstawa)
    for i in range(len(t)):
        t[i] = 1 / podstawa * np.sum(x[i:i+p])
    return t


def simple_moving_average(x, base):
    p = int((base - 1) / 2)
    t = np.zeros(len(x) - 2*p)
    for i in range(len(t)):
        t[i] = np.sum(x[i:i+2*p]) * 1 / base
    return t


def main():
    data = np.loadtxt('../Lista1/zad2_lista1.txt')
    x = data
    x = np.array(x)
    b1 = 11
    b2 = 25
    b3 = 301
    x1 = simple_moving_average(x, b1)
    x2 = simple_moving_average(x, b2)
    x3 = simple_moving_average(x, b3)
    plt.plot(np.linspace(0, len(x), len(x)), x)
    plt.plot(np.linspace(0, len(x1), len(x1)), x1)
    plt.plot(np.linspace(0, len(x2), len(x2)), x2)
    plt.plot(np.linspace(0, len(x3), len(x3)), x3)
    plt.show()


if __name__ == '__main__':
    main()
