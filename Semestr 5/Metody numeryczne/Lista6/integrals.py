import matplotlib.pyplot as plt
import numpy as np

from matrix.Matrix import Matrix
from matrix.Vector import Vector


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


def polynomial(coef): return lambda x : sum(coef[i] * x ** i for i in range(len(coef)))


def integrate_trapezoidal(f, a, b, n):
    h = (b - a) / n
    x0 = f(a)
    xn = f(b)
    mid = 0
    for i in range(1, n):
        x = a + i * h
        mid += f(x)
    integral = h * ((xn + x0) / 2 + mid)
    return integral


def integrate_simpson(f, a, b, n):
    h = (b - a) / n
    x0 = f(a)
    xn = f(b)
    xi = 0
    xj = 0
    for i in range(1, n):
        x = a + i * h
        if i % 2 ==0:
            xi += f(x)
        else:
            xj += f(x)
    integral = h * (x0 + 4 * xj + 2 * xi + xn) / 3
    return integral


def GaussLegendre(f, a, b, weights, nodes):
    n = len(nodes)
    h = (b - a) / 2
    c = (a + b) / 2
    val = 0
    for i in range(0, n):
        val += weights[i] * f(h * nodes[i] + c)
    integral = h * val
    return integral