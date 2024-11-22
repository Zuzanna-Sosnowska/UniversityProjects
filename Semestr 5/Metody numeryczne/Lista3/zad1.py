from functions import doolittle_method, calculate_machine_unit
from matrix.Matrix import Matrix
from matrix.Vector import Vector
from numpy import float32
import numpy as np


def main():
    n = 5
    A = hilbert_matrix(n)
    b = Vector(np.array([5, 4, 3, 2, 1]).astype(float32))
    print(iter_correcting_solution(A, b, iter=1))
    print(iter_correcting_solution(A, b, iter=2))
    print(iter_correcting_solution(A, b, iter=3))
    print(iter_correcting_solution(A, b, iter=4))
    print(iter_correcting_solution(A, b, iter=5))
    print(iter_correcting_solution(A, b, iter=6))
    print(np.linalg.solve(np.array(A).astype(float), np.array(b).astype(float)))


def hilbert_matrix(n:int)-> Matrix:
    return Matrix.create_from_list([[float32(1 / (i + j - 1)) for i in range(1, n + 1)] for j in range(1, n + 1)])


def iter_correcting_solution(A: Matrix, b: Vector, iter=100) -> Vector:
    u = calculate_machine_unit()
    A_inv = A.inv()
    x = A_inv.multiply_matrix_by_vector(b)
    r = b - A.multiply_matrix_by_vector(x)
    norm_r: np.float32 = r.norm()
    condition: np.float32 = b.norm() * u
    i = 0
    while norm_r > condition and i < iter:
        x += A_inv.multiply_matrix_by_vector(r)
        r = b - A.multiply_matrix_by_vector(x)
        norm_r = r.norm_inf()
        i += 1
    print(norm_r)
    return x


if __name__ == "__main__":
    main()
