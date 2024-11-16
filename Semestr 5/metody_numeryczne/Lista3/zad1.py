from matrix.Matrix import Matrix, Vector


def main():
    n = 5
    M = Matrix.create_from_list(hilbert_matrix(n))
    b = Vector([5, 4, 3, 2, 1])


def hilbert_matrix(n):
    return [[1 / (i + j - 1) for i in range(1, n+1)] for j in range(1, n+1)]


def iter_correcting_solution(A: Matrix, b: Vector):
    pass

    
