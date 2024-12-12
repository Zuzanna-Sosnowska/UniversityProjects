from functions import doolittle_method, norm, calculate_machine_unit
from matrix.Matrix import Matrix
from matrix.Vector import Vector
import numpy as np
import scipy


def main():
    n = 5
    A = hilbert_matrix(n)
    b = np.array([5-i for i in range(n)])
    print(iter_correcting_solution(A, b))
    print(np.linalg.solve(A, b))
    print(scipy.linalg.solve(A, b))


def hilbert_matrix(n:int)->np.ndarray:
    """
    Funkcja zwraca macierz Hilberta o określonym wymiarze.
    :param n: rozmiar macierzy Hilberta
    :return: Obiekt klacy np.ndarray, który jest macierzą Hilberta
    """
    return np.array([[1 / (i+j-1) for i in range(1, n+1)] for j in range(1, n+1)])


def iter_correcting_solution(A, b, iter=100):
    A, b = A.astype(np.float32), b.astype(np.float32)
    e = calculate_machine_unit()
    L, U = doolittle_method(Matrix.create_from_list(A))
    L, U = Matrix.create_from_list(L), Matrix.create_from_list(U)
    L_inv = np.array(L.inv())
    U_inv = np.array(U.inv())
    L, U = np.array(L), np.array(U)
    x = U_inv.dot(L_inv.dot(b))
    r = np.float64(b) - np.float64(A) @ np.float64(x)
    norm_r= norm(r)
    condition = norm(np.float64(b)) * e
    c = 0
    x = x.astype(np.float64)
    while norm_r > condition and c < iter:
        x += U_inv.dot(L_inv.dot(np.float32(r)))
        r = np.float64(b) - np.float64(A) @ np.float64(x)
        norm_r = norm(r)
        c += 1
    return x


def iter_corr_sol(A:np.ndarray, b:np.ndarray, iter:int=1000) -> np.ndarray:
    e = 1e-12
    A = np.copy(A).astype(np.float32)
    b = np.copy(b).astype(np.float32)
    n = len(A)
    A_inv = np.linalg.inv(A)

    x1 = A_inv.dot(b)
    x1 = x1.astype(np.float32)
    for i in range(iter):
        Ax = A.dot(x1)
        r = b - Ax
        if np.linalg.norm(r, ord=np.inf) < e * np.linalg.norm(x1, ord=np.inf):
            return x1
        x1 += A_inv.dot(r)
    return x1


if __name__ == '__main__':
    main()
