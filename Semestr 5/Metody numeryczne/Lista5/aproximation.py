import numpy as np
from matplotlib import pyplot as plt
from matrix.Matrix import Matrix
from matrix.Vector import Vector
from scipy.optimize import fsolve, curve_fit
import useful_functions as uf


def curve_fit_implemented(points, func, derivative_vector):
    x, y = zip(*points)
    g_func_vector = []
    n = len(derivative_vector)
    for derivative in derivative_vector:
        g_func_vector.append(get_g_functions(points, func, derivative))
    solutions = fsolve(lambda t: [g_func_vector[i](t) for i in range(n)], np.ones(n))
    return solutions


def get_g_functions(points, func, derivative):
    x, y = zip(*points)
    x, y = np.array(x), np.array(y)
    return lambda params: np.sum((y - func(x, params)) * derivative(x, params))


def norm(x):
    return np.sqrt(np.sum(x**2))


def func(x, params):
    a, b = params
    return a * np.exp(b * x)


def a_der(x, params):
    a, b = params
    return np.exp(b * x)


def b_der(x, params):
    a, b = params
    return a * np.exp(b * x) * x


def polynomial_approximation(points, polynom_deg):
    def x_i(x, i):
        return np.sum(np.power(x, i))

    def xy_i(x, y, i):
        return np.sum(np.power(x, i) * y)

    k = polynom_deg
    n = len(points)
    x, y = zip(*points)
    b = Vector([xy_i(x, y, i) for i in range(k+1)])
    matrix_lst = []
    matrix_row = [n] + [x_i(x, i) for i in range(1, k+1)]
    matrix_lst.append(matrix_row[:])
    for i in range(1, k+1):
        matrix_row.pop(0)
        matrix_row.append(x_i(x, k+i))
        matrix_lst.append(matrix_row[:])
    A = Matrix.create_from_list(matrix_lst)
    A_inv = A.inv()
    return A_inv.multiply_matrix_by_vector(b)


def main():
    x = np.array([1.2, 2.8, 4.3, 5.4, 6.8, 7.9])
    y = np.array([7.5, 16.1, 38.9, 67.0, 146.6, 266.2])
    points = list(zip(x, y))
    sol1 = curve_fit_implemented(points, func, [a_der, b_der])

    popt, popcov = curve_fit(lambda x, a, b: func(x, [a, b]), x, y)

    x2 = np.linspace(0, 8, 800)
    y2 = func(x2, sol1)
    y3 = func(x2, popt)

    plt.plot(x2, y2)
    plt.plot(x2, y3)
    plt.scatter(x, y)
    plt.show()

    a, b = sol1
    a2, b2 = popt
    points = list(zip(x, y))

    print("odchylenie standardowe dla zaimplementowanej metody:", uf.st_dev(func=lambda x: a * np.exp(b * x), points=points))
    print("odchylenie standardowe dla funkcji z biblioteki:", uf.st_dev(func=lambda x: a2 * np.exp(b2 * x), points=points))


if __name__ == '__main__':
    main()
