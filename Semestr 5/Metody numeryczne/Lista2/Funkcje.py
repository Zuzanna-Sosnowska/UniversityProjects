from matrix.Matrix import Matrix
from matrix.Vector import Vector
import copy


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


if __name__ == "__main__":
    A = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print(A)