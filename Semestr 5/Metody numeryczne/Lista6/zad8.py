import numpy as np
import matplotlib.pyplot as plt
from matrix.Matrix import Matrix
from matrix.Vector import Vector
import derivatives as df


def polynomial_interpolation(points):
    """
    Funkcja oblicza interpolację wielomianową dla zadanych punktów.
    :param points: Punkty, w których będziemy obliczać interpolację wielomianową.
    :return: Funkcja zwraca wielomian (funkcję) o obliczonych na podstawie punktów współczynnikach .
    """
    n = len(points)
    # Tworzenie macierzy układu równań
    matrix_lst = []
    for i in range(n):
        row = np.zeros(n)
        for j in range(n):
            row[j] = points[i][0] ** j
        matrix_lst.append(row)

    A = Matrix.create_from_list(matrix_lst)
    b = Vector([points[i][1] for i in range(n)])
    A_inv = A.inv()
    # Współczynniki wielomianu interpolującego są rozwiązaniem układu równań liniowych
    coeffs = A_inv.multiply_matrix_by_vector(b)
    return coeffs


def polynomial(coef):
    """
    Funkcja zwraca wielomian (funkcję) o zadanych współczynnikach
    :param coef: Lista współczynników, zaczynająca się od wyrazu wolnego i kończąca na współczynniku przy najwyższej potędze
    :return: Funkcja zwraca funkcję, obliczającą wartość wielomianu o zadanych współczynnikach w punkcie.
    """
    return lambda x : sum(coef[i] * x ** i for i in range(len(coef)))


def main():
    x = [-2.2, -0.3, 0.8, 1.9]
    f_x = [15.180, 10.962, 1.920, -2.040]
    points = list(zip(x, f_x))

    coeffs = polynomial_interpolation(points)
    poly = polynomial(coef=coeffs)

    x0 = 0
    h = np.array([0.1, 0.01, 0.001])

    der1 = df.forward_difference(poly, 0, h[0])
    der2 = df.backward_difference(poly, 0, h[0])
    der3 = df.central_difference(poly, 0, h[0])
    der4 = df.extrapolated_difference(poly, 0, h[0])

    print(der1, der2, der3, der4)


if __name__ == '__main__':
    main()
