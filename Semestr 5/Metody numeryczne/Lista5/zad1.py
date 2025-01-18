import matplotlib.pyplot as plt
import numpy as np
import interpolation
from scipy.interpolate import lagrange


def main():
    h_lst = np.array([0, 3, 6])
    ro_lst = np.array([1.225, 0.905, 0.652])
    points = tuple(zip(h_lst, ro_lst))

    poly = interpolation.polynomial_interpolation(points)

    poly2 = lagrange(h_lst, ro_lst)

    h = np.linspace(0, 6, 1000)
    ro = poly(h)

    ro2 = poly2(h)

    plt.plot(h, ro, label='moja funkcja', linewidth=2)
    plt.plot(h, ro2, label='biblioteka', linestyle=':')
    plt.scatter(h_lst, ro_lst, color='red')
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    main()
