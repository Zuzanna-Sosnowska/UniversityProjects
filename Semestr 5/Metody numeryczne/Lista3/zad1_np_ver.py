from functions import doolittle_method, norm
import numpy as np
import scipy


def main():
    n = 5
    A = hilbert_matrix(n)
    b = np.array([5-i for i in range(n)])
    print(iter_corr_sol(A, b, iter=4))
    print(np.linalg.solve(A, b))
    print(scipy.linalg.solve(A, b))


def hilbert_matrix(n:int)->np.ndarray:
    """
    Funkcja zwraca macierz Hilberta o określonym wymiarze.
    :param n: rozmiar macierzy Hilberta
    :return: Obiekt klacy np.ndarray, który jest macierzą Hilberta
    """
    return np.array([[1 / (i+j-1) for i in range(1, n+1)] for j in range(1, n+1)])


def iter_correcting_solution(A, b):
    A, b = A.astype(np.float32), b.astype(np.float32)
    e = 1e-14
    L, U = doolittle_method(A)
    L_inv = np.linalg.inv(L)
    U_inv = np.linalg.inv(U)
    x = U_inv.dot(L_inv.dot(b))
    r = np.float64(b) - np.float64(A) @ np.float64(x)
    norm_r= norm(r)
    condition = norm(np.float64(b)) * e
    c = 0
    x = x.astype(np.float64)
    while norm_r > condition:
        x += U_inv.dot(L_inv.dot(np.float32(r)))
        r = np.float64(b) - np.float64(A) @ np.float64(x)
        norm_r = norm(r)
        c += 1
    print(norm_r)
    print(c)
    return x


def iter_corr_sol(A:np.ndarray, b:np.ndarray, iter:int=100) -> np.ndarray:
    e = 1e-12
    A = np.copy(A).astype(np.float32)
    b = np.copy(b).astype(np.float32)
    n = len(A)
    A_inv = np.linalg.inv(A)

    x1 = A_inv.dot(b)
    x1 = x1.astype(np.float64)
    for i in range(iter):
        Ax = A.dot(x1)
        r = b - Ax
        if np.linalg.norm(r, ord=np.inf) < e * np.linalg.norm(x1, ord=np.inf):
            return x1
        x1 += A_inv.dot(r)
    return x1


if __name__ == '__main__':
    main()
