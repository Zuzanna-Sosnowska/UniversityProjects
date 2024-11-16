import Funkcje
from matrix.Matrix import Matrix, Vector


def main():
    A = Matrix.create_from_list(
        [[3.50, 2.77, -0.76, 1.80],
         [-1.80, 2.68, 3.44, -0.09],
         [0.27, 5.07, 6.90, 1.61],
         [1.71, 5.45, 2.68, 1.71]])
    b = Vector([7.31, 4.23, 13.85, 11.55])

    x = Funkcje.gaussian_solver(A, b)
    print(A.multiply_matrix_by_vector(x))


if __name__ == '__main__':
    main()
