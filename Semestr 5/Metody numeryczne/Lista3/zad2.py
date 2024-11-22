from matrix.Matrix import Matrix
from matrix.Vector import Vector
from functions import calculate_machine_unit
import numpy as np


def main():
    n = 20
    A = create_matrix_to_ex_2(n)
    b = create_vector_to_ex_2(n)
    print(gauss_seidle_method(A, b, tol=calculate_machine_unit(), showit=True))
    print(np.linalg.solve(A, b))


def create_matrix_to_ex_2(n):
    A = Matrix.identity_matrix(n)
    A = 4 * A
    for i in range(1, n):
        A[i][i-1] = -1
        A[i-1][i] = -1
    A[n-1][0] = 1
    A[0][n-1] = 1
    return A


def create_vector_to_ex_2(n):
   return Vector([0 for i in range(n-1)] + [100])


def decompose_matrix(A:Matrix):
    """
    Funkcja zwraca rozkład macierzy A dany wzorem: A = D + L + U, gdzie macierz D to macierz diagonalna, a
    macierze L i U to macierze górno i dolno trójkątne (tzn. L oraz U mają zera na głównej przekątnej).
    :param A: Macierz A
    :return: Funkcja zwraca kolejno macierz D, L i U
    """
    D = Matrix.create_from_list(np.zeros_like(A))
    L = Matrix.create_from_list(np.zeros_like(A))
    U = Matrix.create_from_list(np.zeros_like(A))

    for i in range(A.number_of_columns()):
        for j in range(A.number_of_rows()):
            if i == j:
                D[i][j] = A[i][j]
            elif i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]

    return D, L, U


def gauss_seidle_method(A:Matrix, b:Vector, tol=1e-12, showit=False, iter=100)-> Vector:
    """
    Metoda rozwiązuje układ równań postaci b = Ax metodą Gaussa-Seidla.
    :param A: Macierz układu równań
    :param b: Wektor układu równań
    :param iter: Maksymalna liczba iteracji
    :param tol: Dokładność rozwiązania. Im mniejsza wartość parametru tol, tym większa dokładność rozwiązania
    :param showit: Jeśli wartość parametru wynosi True, to funkcja pokaże, ile iteracji potrzeba, aby uzyskac wynik
    :return: Funkcja zwraca wektor rozwiązań zadanego układu równań
    """
    D, L, U = decompose_matrix(A)
    n = A.number_of_rows()
    Q = inverse_lower_triangular_matrix(D + L)
    x = np.zeros(n)

    for it in range(iter):
        x_old = x.copy()
        x = Q.multiply_matrix_by_vector(b - U.multiply_matrix_by_vector(x))
        if (x - x_old).norm_inf() < tol:
            if showit:
                print(f"Zbieżność osiągnięta po {it + 1} iteracjach.")
            return x
    raise ValueError("Metoda Gaussa–Seidela nie osiągnęła zbieżności.")


def inverse_lower_triangular_matrix(A:Matrix)->Matrix:
    """
    Funkcja zwraca macierz odwrotną do macierzy dolnotrójkątnej (posiadającej elementy na głównej przekątnej)
    :param A: Macierz dolnotrójkątna A
    :return: Macierz odwrotna do macierzy A
    """
    B = A.copy()
    I = Matrix.identity_matrix(B.number_of_rows())
    for i in range(B.number_of_rows()):
        modifier = 1.0 / B[i][i]
        I[i] = modifier * I[i]
        B[i][i] = 1.0
        for j in range(i + 1, B.number_of_rows()):
            nullifier = B[j][i]
            I[j] = I[j] - nullifier * I[i]
            B[j][i] = 0.0
    return I


if __name__ == '__main__':
    main()
