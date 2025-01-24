import matplotlib.pyplot as plt
import numpy as np
import zad1


def main():
    x = np.linspace(4, 8, 10000)
    y = g(x)
    print(newton(g, dg, 4))

    plt.plot(x, y)
    plt.axhline(y=0, color='black')
    plt.plot((4.0, 5.0), (0.0, 0.0), color='red')
    plt.show()

    print(zad1.bisection(g, 4, 5))


def newton(f, df, x0:float, acc:float=1.0e-9)->tuple:
    """
    Funkcja zwraca miejsce zerowe obliczone za pomocą metody newtona dla zadanych parametrów.
    :param f: Funkcja, której miejsca zerowego szukamy
    :param df: Pochodna funkcji f
    :param x0: Punkt startowy
    :param acc: Dokładność obliczeń
    :return: Funkcja zwraca tuple, którego pierwsza wartość to szukane miejsce zerowe, natomiast druga wartość to
    wartość funkcji f w tym punkcie
    """
    if f(x0) == 0:
        return x0, 0
    while np.abs(f(x0)) > acc:
        x0 = x0 - f(x0) / df(x0)
    return x0, f(x0)


def g(x): return cosh(x) * np.cos(x) - 1


def cosh(x): return (np.exp(x) + np.exp(-x)) / 2


def sinh(x): return (np.exp(x) - np.exp(-x)) / 2


def dg(x): return sinh(x) * np.cos(x) - cosh(x) * np.sin(x)


if __name__ == '__main__':
    main()
