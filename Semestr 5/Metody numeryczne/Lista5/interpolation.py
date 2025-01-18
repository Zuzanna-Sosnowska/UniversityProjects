import matplotlib.pyplot as plt
from matrix.Matrix import Matrix
from matrix.Vector import Vector
import numpy as np
from scipy.interpolate import interp1d


def polynomial_interpolation(points):
    n = len(points)
    matrix_lst = []
    for i in range(n):
        row = np.zeros(n)
        for j in range(n):
            row[j] = points[i][0] ** j
        matrix_lst.append(row)

    A = Matrix.create_from_list(matrix_lst)
    b = Vector([points[i][1] for i in range(n)])
    A_inv = A.inv()
    coeffs = A_inv.multiply_matrix_by_vector(b)
    return polynomial(coef=coeffs)


def lagrange(x, points):
    x_data, y_data = zip(*points)
    n = len(points)
    y = 0
    for i in range(n):
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x - x_data[j]) / (x_data[i] - x_data[j])
        y = y + w * y_data[i]
    return y


def polynomial(coef): return lambda x : sum(coef[i] * x ** i for i in range(len(coef)))


def main():
    points = [(-2, 3), (1, 1), (2, -3), (4, 8)]


if __name__ == '__main__':
    main()
