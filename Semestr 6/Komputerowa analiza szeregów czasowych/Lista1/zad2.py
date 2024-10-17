import matplotlib.pyplot as plt
import numpy as np


def prosta_srednia_ruchoma(x, podstawa):
    p = int((podstawa - 1) / 2)
    t = np.zeros(len(x) - podstawa)
    for i in range(len(t)):
        t[i] = 1 / podstawa * np.sum(x[i:i+p])
    return t


if __name__ == '__main__':
    data = np.loadtxt('../Lista1/zad2_lista1.txt')
    x = data
    x = np.array(x)
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # pod1 = 5
    # print(prosta_srednia_ruchoma(a, pod1))
    podstawa1 = 11
    podstawa2 = 25
    podstawa3 = 201
    x1 = prosta_srednia_ruchoma(x, podstawa1)
    x2 = prosta_srednia_ruchoma(x, podstawa2)
    x3 = prosta_srednia_ruchoma(x, podstawa3)

    plt.plot(np.linspace(0, len(x), len(x)), x, color='blue')
    plt.plot(np.linspace(0, len(x1), len(x1)), x1, color='red')
    plt.plot(np.linspace(0, len(x2), len(x2)), x2, color='orange')
    plt.plot(np.linspace(0, len(x3), len(x3)), x3, color='green')
    plt.show()