from numpy import float32, float64

from matrix.Matrix import Matrix
from matrix.Vector import Vector


def main():
    n = 5
    A = Matrix.create_from_list(hilbert_matrix(n))
    b = Vector([5, 4, 3, 2, 1])

    print(iter_correcting_solution(A, b))


def hilbert_matrix(n):
    return [[1 / (i + j - 1) for i in range(1, n + 1)] for j in range(1, n + 1)]


def iter_correcting_solution(A: Matrix, b: Vector):
    u = calculate_machine_unit()
    L, U = doolittle_method(A, b)
    x = U.inv().multiply_matrix_by_vector(L.inv().multiply_matrix_by_vector(b))
    r = b - A.multiply_matrix_by_vector(x)
    norm_r: float64 = r.norm()
    condition: float32 = b.norm() * u
    while norm_r > condition:
        prev = x
        x = x + U.inv().multiply_matrix_by_vector(L.inv().multiply_matrix_by_vector(r))
        r = b - A.multiply_matrix_by_vector(x)
        norm_r = r.norm()
        print()
    return x


def calculate_machine_unit():
    u = 1
    while 1 + u != 1:
        u /= 2
    return u


def doolittle_method(A: Matrix, b: Vector):
    n = A.number_of_rows()
    U = Matrix.create_from_list([[0 for i in range(n)] for j in range(n)])
    L = Matrix.create_from_list([[0 for i in range(n)] for j in range(n)])
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    return L, U


if __name__ == "__main__":
    # A = Matrix.create_from_list([[-1, 2, 1],
    #                              [1, -3, -2],
    #                              [3, -1, -1]])
    # b = Vector([-1, -1, 4])
    # L, U = doolittle_method(A, b)
    # print(U.inv().multiply_matrix_by_vector(L.inv().multiply_matrix_by_vector(b)))
    # print(np.linalg.solve(A, b))
    main()
