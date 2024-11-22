from matrix.Matrix import Matrix
import numpy as np


def calculate_machine_unit():
    u = 1
    while 1 + u != 1:
        u /= 2
    return 2 * u


def doolittle_method(A: Matrix) -> (Matrix, Matrix):
    n = A.number_of_rows()
    U = Matrix.create_from_list([[0 for i in range(n)] for j in range(n)])
    L = Matrix.create_from_list([[0 for i in range(n)] for j in range(n)])
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    return L, U


def norm(x):
    return np.sum(np.abs(x))