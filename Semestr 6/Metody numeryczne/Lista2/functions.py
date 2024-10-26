def calculate_upper_triangular_matrix(A, b):
    n = len(A)
    for column in range(n):
        c = False
        for row in range(column, n):
            if A[row][column] != 0 and c == False:
                swap_rows(A, row, column)
                swap_elements(b, row, column)
                c = True
                continue
            if c:
                a = multiply_and_change_rows(A[row], A[column], column)
                change_elements(b, row, column, a)
        if not c:
            raise ValueError("Macierz osobliwa")


def upper_triangular_matrix(A):
    n = len(A)
    for j in range(n):
        c = False
        for i in range(j, n):
            if A[i][j] != 0 and c == False:
                swap_rows(A, i, j)
                c = True
                continue
            if c:
                multiply_and_change_rows(A[i], A[j], j)
        if not c:
            raise ValueError("Macierz osobliwa")


def swap_rows(A, i, j):
    row_copy = A[j]
    A[j] = A[i]
    A[i] = row_copy


def multiply_and_change_rows(row1, row2, j):
    if len(row1) != len(row2):
        raise ValueError("Rows must have same length")
    a = row1[j] / row2[j]
    for i in range(j, len(row1)):
        row1[i] = row1[i] - a * row2[i]
    return a


def change_rows(row1, row2, a):
    if len(row1) != len(row2):
        raise ValueError("Rows must have same length")
    for i in range(len(row1)):
        row1[i] = row1[i] - a * row2[i]


def swap_elements(b, i, j):
    number_copy = b[i]
    b[i] = b[j]
    b[j] = number_copy

def change_elements(b, i, j, a):
    b[i] = b[i] - a * b[j]


def subtract_columns(b, a, j):
    for i in range(j):
        b[i] = b[i] - a[i]


def multiply_columns(a, c, j):
    a_copy = a.copy()
    for i in range(j):
        a_copy[i] = a[i] * c
    return a_copy


def gaussian_solver(A, b):
    calculate_upper_triangular_matrix(A, b)
    solutions = [0 for _ in range(len(A))]
    solutions[-1] = b[-1] / A[-1][-1]
    for i in range(len(A)-2, -1, -1):
        a_copy =  multiply_columns([A[j][i+1] for j in range(len(A))], solutions[i+1], i+1)
        subtract_columns(b, a_copy, i+1)
        solutions[i] = b[i] / A[i][i]
    return solutions


def det(A):
    upper_triangular_matrix(A)
    det = 1
    for i in range(len(A)):
        det *= A[i][i]
    return det


def multiply_matrix_by_vector(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix must have same length")
    product = [0] * len(A)
    for i in range(len(A)):
        product[i] = sum(A[i] * B[i] for i in range(len(A)))
    return product


def identity_matrix(n):
    I = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I[i][j] = 1
            else:
                I[i][j] = 0
    return I


def multiply_row(row, a):
    for i in range(len(row)):
        row[i] = a * row[i]


def inverse_matrix(A):
    n = len(A)
    I = identity_matrix(n)
    for j in range(n):
        c = False
        for i in range(j, n):
            if A[i][j] != 0 and c == False:
                swap_rows(A, i, j)
                swap_rows(I, i, j)
                c = True
                continue
            if c:
                a = multiply_and_change_rows(A[i], A[j], j)
                change_rows(I[i], I[j], a)
        if not c:
            raise ValueError("Macierz osobliwa")

    for j in range(n-1, -1, -1):
        for i in range(j):
            a = multiply_and_change_rows(A[i], A[j], j)
            change_rows(I[i], I[j], a)
    for j in range(n):
        multiply_columns(I[j], 1 / A[j][j])
        A[j][j] /= A[j][j]

    return I, A
