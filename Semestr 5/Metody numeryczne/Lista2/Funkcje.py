from Matrix import Matrix, Vector
import copy
import numpy as np


def calculate_upper_triangular_matrix(A: Matrix, b: Vector):
    A, b = copy.deepcopy(A), copy.deepcopy(b)
    n = A.number_of_rows()
    for column in range(n):
        find_nullifying_row = False
        for row in range(column, n):
            if A[row][column] != 0 and find_nullifying_row == False:
                A.swap_rows(row, column)
                b[row], b[column] = b[column], b[row]
                find_nullifying_row = True
                continue
            if find_nullifying_row:
                multiplier = row_nullify_multiplier_for_column(
                    row_to_nullify=A[row],
                    base_row=A[column],
                    column=column
                )
                A[row] = A[row] - multiplier * A[column]
                b[row] = b[row] - multiplier * b[column]
        if not find_nullifying_row:
            raise ValueError("Macierz osobliwa")
    return A, b


def row_nullify_multiplier_for_column(row_to_nullify, base_row, column):
    return row_to_nullify[column] / base_row[column]


def gaussian_solver(A: Matrix, b: Vector) -> Vector:
    A, b = calculate_upper_triangular_matrix(A, b)
    solutions = Vector([0 for _ in range(A.number_of_rows())])
    for column in range(A.number_of_columns()-1, -1, -1):
        for row in range(column-1, -1, -1):
            multiplier = row_nullify_multiplier_for_column(
                row_to_nullify=A[row],
                base_row=A[column],
                column=column
            )
            A[row] = A[row] - multiplier * A[column]
            b[row] = b[row] - multiplier * b[column]
        solutions[column] = b[column] / A[column][column]
    return solutions


def main():
    A = Matrix.create_from_list(
        [[0, 0, 2, 1, 2],
         [0, 1, 0, 2, -1],
         [1, 2, 0, -2, 0],
         [0, 0, 0, -1, 1],
         [0, 1, -1, 1, -1]])

    b = Vector([1, 1, -4, -2, -1])
    A1, b1 = calculate_upper_triangular_matrix(A, b)
    print(gaussian_solver(A, b))
    print('\n')
    print(np.linalg.solve(A, b))


if __name__ == "__main__":
    main()
