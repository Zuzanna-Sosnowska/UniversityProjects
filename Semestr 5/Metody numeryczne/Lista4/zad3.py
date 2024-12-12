import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g
import zad1


def function(t):
    u = 2510
    M0 = 2.8 * 10 ** 6
    m = 13.3 * 10 ** 3
    return u * np.log(M0 / (M0 - m * t)) - g * t

def main():
    v = 335
    t = np.linspace(0, 100, 10000)
    sol = zad1.brent(lambda x: function(x) - v, 0, 100)

    plt.plot(t, function(t), label='prędkość rakiety')
    plt.axhline(y=v, color='green', label='prędkość dźwięku')
    plt.scatter(sol, function(sol), color='red', label=f'({sol}, {function(sol)})')
    plt.xlabel(r'$t$')
    plt.ylabel('Prędkość rakiety')
    plt.title('Wykres prędkości rakiety od czasu')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
