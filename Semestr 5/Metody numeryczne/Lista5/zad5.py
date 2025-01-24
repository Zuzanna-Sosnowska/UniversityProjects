import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import aproximation
import numpy as np


def polynomial(coef): return lambda x : sum(coef[i] * x ** i for i in range(len(coef)))


def main():
    T = np.array([0, 21.1, 37.8, 54.4, 71.1, 87.8, 100])
    mi_k = np.array([1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296]) * 10 ** -3

    T_lst = np.array([10, 30, 60, 90])


    points = tuple(zip(T, mi_k))

    coeffs = aproximation.polynomial_approximation(points=points, polynom_deg=3)

    t = np.linspace(0, 100, 1000)
    poly = polynomial(coeffs)

    curve_fit(lambda x, a, b, c, d : polynomial([a, b, c, d])(x), T, mi_k)
    coeffs2, covariance_matrix = curve_fit(lambda x, a, b, c, d : polynomial([a, b, c, d])(x), T, mi_k)
    poly2 = polynomial(coeffs2)

    coeffs3 = np.polyfit(T, mi_k, 3)[::-1]
    poly3 = polynomial(coeffs3)

    mi = poly(t)
    mi2 = poly2(t)
    mi3 = poly3(t)
    mi_k_lst = poly(T_lst)

    print(coeffs)
    print(coeffs2)

    plt.plot(t, mi)
    plt.plot(t, mi2)
    plt.plot(t, mi3)
    plt.scatter(T, mi_k, color='red')
    plt.scatter(T_lst, mi_k_lst, color='green', marker='^')
    plt.show()


if __name__ == '__main__':
    main()

