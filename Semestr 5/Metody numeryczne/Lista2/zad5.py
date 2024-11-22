import scipy
import Funkcje
from matrix.Matrix import Matrix
from matrix.Vector import Vector


def polynomial_coeffs_lst(x0):
    return [x0 ** i for i in range(5)]


def main():
    points = [(0, -1), (1, 1), (3, 3), (5, 2), (6, -2)]
    A = []
    b = []
    for x, y in points:
        A.append(polynomial_coeffs_lst(x))
        b.append(y)
    A = Matrix.create_from_list(A)
    b = Vector(b)

    print(Funkcje.gaussian_solver(A, b))
    print(scipy.linalg.solve(A, b))


if __name__ == '__main__':
    main()
