import numpy as np


def main():
    n = 5
    A = hilbert_matrix(n)
    b = np.array([np.float32(5-i) for i in range(n)])
    print(iter_correcting_solution(A, b))


def hilbert_matrix(n):
    return np.array([[np.float32(1 / (i+j-1)) for i in range(1, n+1)] for j in range(1, n+1)])


def doolittle_method(A, b):
    n = len(A)
    U = np.array([np.zeros(n) for i in range(n)])
    L = np.array([np.zeros(n) for i in range(n)])
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    return L, U


def norm(x):
    return np.sum(np.abs(x))


def iter_correcting_solution(A, b):
    e = calculate_machine_unit()
    L, U = doolittle_method(A, b)
    x = np.matmul(np.matmul(np.linalg.inv(U), np.linalg.inv(L)), b)
    r = b - A * x
    norm_r= norm(r)
    condition = np.float32(norm(b) * e)
    c = 0
    while norm_r > condition:
        x = x + np.matmul(np.matmul(np.linalg.inv(U), np.linalg.inv(L)), r)
        r = b - A * x
        norm_r = norm(r)
        c += 1
    print(c)
    return x


def calculate_machine_unit():
    u = 1
    while 1 + u != 1:
        u /= 2
    return 2 * u


if __name__ == '__main__':
    main()
