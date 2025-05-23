import scipy
import Funkcje
from matrix.Matrix import Matrix
from matrix.Vector import Vector


def main():
    A = [[10, -2, -1, 2, 3, 1, -4, 7],
         [5, 11, 3, 10, -3, 3, 3, -4],
         [7, 12, 1, 5, 3, -12, 2, 3],
         [8, 7, -2, 1, 3, 2, 2, 4],
         [2, -15, -1, 1, 4, -1, 8, 3],
         [4, 2, 9, 1, 12, -1, 4, 1],
         [-1, 4, -7, -1, 1, 1, -1, -3],
         [-1, 3, 4, 1, 3, -4, 7, 6]]
    b = [0, 12, -5, 3, -25, -26, 9, -7]

    A = Matrix.create_from_list(A)
    b = Vector(b)
    print(Funkcje.gaussian_solver(A, b))
    print(scipy.linalg.solve(A, b))


if __name__ == '__main__':
    main()
