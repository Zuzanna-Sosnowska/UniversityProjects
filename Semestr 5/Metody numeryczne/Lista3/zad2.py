from matrix.Matrix import Matrix
from matrix.Vector import Vector


def main():
    A = create_matrix_to_ex_2(20)
    print(A)
    b = create_vector_to_ex_2(20)
    print(b)


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


def gauss_seidle_method(A:Matrix, b:Vector):
    pass


if __name__ == '__main__':
    main()
