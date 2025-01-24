import matplotlib.pyplot as plt
import useful_functions as uf
from scipy.optimize import curve_fit
import aproximation
import numpy as np


def main():
    x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
    y = np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828])
    points = list(zip(x, y))

    linear_coeffs = aproximation.polynomial_approximation(points=points, polynom_deg=1)
    quadratic_coeffs = aproximation.polynomial_approximation(points=points, polynom_deg=2)

    scipy_linear_coeffs, lin_cov_matrix = curve_fit(lambda t, a, b: uf.polynomial([a, b])(t), x, y)
    scipy_quadratic_coeffs, quadr_cov_matrix = curve_fit(lambda t, a, b, c: uf.polynomial([a, b, c])(t), x, y)


    linear = uf.polynomial(linear_coeffs)
    quadratic = uf.polynomial(quadratic_coeffs)

    scipy_linear = uf.polynomial(scipy_linear_coeffs)
    scipy_quadratic = uf.polynomial(scipy_quadratic_coeffs)

    x_lst = np.linspace(0, 4, 1000)
    y_linear = linear(x_lst)
    y_quadratic = quadratic(x_lst)
    y_scipy_linear = scipy_linear(x_lst)
    y_scipy_quadratic = scipy_quadratic(x_lst)

    plt.plot(x_lst, y_linear, label='Linear')
    plt.plot(x_lst, y_quadratic, label='Quadratic')
    plt.plot(x_lst, y_scipy_linear, label='Scipy linear')
    plt.plot(x_lst, y_scipy_quadratic, label='Scipy quadratic')
    plt.scatter(x, y, label='Data', color='red')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("odchylenie standardowe dla funkcji liniowej:", uf.st_dev(func=linear,points=points))
    print("odchylenie standardowe dla funkcji kwadratowej:", uf.st_dev(func=quadratic,points=points))
    print("Średnie odchylenie bezwzględne dla funkcji liniowej:", uf.mean_abs_dev(func=linear,points=points))
    print("Średnie odchylenie bezwzględne dla funkcji kwadratowej:", uf.mean_abs_dev(func=quadratic,points=points))


if __name__ == '__main__':
    main()
