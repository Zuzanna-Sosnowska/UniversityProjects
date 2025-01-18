import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import useful_functions as uf
import aproximation
import numpy as np


# def ex_4_approx(points):
#     x, y = zip(*points)
#     mean_x, mean_y = np.mean(x), np.mean(y)
#     b1 = np.sum((x - mean_x) * (y - mean_y)) / np.sum(np.power(x - mean_x, 2))
#     b0 = mean_y - b1 * mean_x
#     return b0, b1


def func(x, params):
    a, b = params
    return a * np.exp(b * x)


def main():
    x = np.array([1.2, 2.8, 4.3, 5.4, 6.8, 7.9])
    y = np.array([7.5, 16.1, 38.9, 67.0, 146.6, 266.2])
    points = tuple(zip(x, np.log(y)))

    x_lst = np.linspace(0, 8, 1000)
    b0, b1 = aproximation.polynomial_approximation(points=points, polynom_deg=1)
    b = b1
    a = np.exp(b0)
    y_lst = a * np.exp(b * x_lst)

    popt, popcov = curve_fit(lambda t, a, b: func(x=t, params=[a, b]), x, y)
    a2, b2 = popt

    y2_lst = func(x_lst, [a2, b2])

    plt.plot(x_lst, y_lst, label='zaimplementowana metoda')
    plt.plot(x_lst, y2_lst, label='curve_fit z biblioteki scipy')
    plt.scatter(x, y, color='red', label='zadane punkty')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(sum(abs(y - a * np.exp(b * x)))/len(x))
    print(y, a * np.exp(b * x))
    print(y -  a * np.exp(b * x))

    points = tuple(zip(x, y))
    print("odchylenie standardowe dla zaimplementowanej metody:", uf.st_dev(func=lambda x: a * np.exp(b * x), points=points))
    print("odchylenie standardowe dla funkcji z biblioteki:", uf.st_dev(func=lambda x: a2 * np.exp(b2 * x), points=points))


if __name__ == '__main__':
    main()
