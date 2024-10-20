import matplotlib.pyplot as plt
import numpy as np


def prosta_regresji(x, y):
    b1 = np.sum((x - np.mean(x))*(y - np.mean(y))) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b0, b1


def simple_moving_average(x, base):
    p = int((base - 1) / 2)
    t = np.zeros(len(x) - 2*p)
    for i in range(len(t)):
        t[i] = np.sum(x[i:i+2*p]) * 1 / base
    return t


def main():
    x = np.loadtxt('../Lista1/zad2_lista1.txt')
    y = np.loadtxt('../Lista1/zad3_lista1.txt')
    x = np.array(x)
    y = np.array(y)

    b01, b11 = prosta_regresji(x, y)
    x1 = np.linspace(-1, 10, 1000)
    y1 = b01 + b11 * x1

    plt.plot(x1, y1, color='red')
    plt.scatter(x, y)
    plt.show()

    x_11 = simple_moving_average(x, 11)
    y_11 = simple_moving_average(y, 11)

    b02, b12 = prosta_regresji(x_11, y_11)
    x2 = np.linspace(-1, 10, 1000)
    y2 = b02 + b12 * x2

    plt.plot(x2, y2, color='red')
    plt.scatter(x, y)
    plt.show()



if __name__ == '__main__':
    main()
