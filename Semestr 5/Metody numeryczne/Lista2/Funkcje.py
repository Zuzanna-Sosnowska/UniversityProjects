from Matrix import Matrix, Vector
import copy


def calculate_upper_triangular_matrix(A: Matrix, b: Vector):
    A, b = copy.deepcopy(A), copy.deepcopy(b)
    n = len(A)
    for column in range(n):
        find_nullyfying_row = False
        for row in range(column, n):
            if A[row][column] != 0 and find_nullyfying_row == False:
                A.swap_rows(row, column)
                # swap_rows(A, row, column)
                # swap_elements(b, row, column)
                c = True
                continue
            if find_nullyfying_row:
                a = calculate_nullify_multiplier_for_index(
                    row_to_nullify=A[row],
                    base_row=A[column],
                    index=column
                )
                A[row] = A[row] - a * A[column]
                # a = multiply_and_change_rows(A[row], A[column], column)
                b[row] = b[row] - a * b[column]
                # change_elements(b, row, column, a)
        if not find_nullyfying_row:
            raise ValueError("Macierz osobliwa")


def calculate_nullify_multiplier_for_index(row_to_nullify, base_row, index):
    return row_to_nullify[index] / base_row[index]


# def gaussian_solver(A: Matrix, b: Vector) -> Vector:
#     A, b = copy.deepcopy(A), copy.deepcopy(b)
#     calculate_upper_triangular_matrix(A, b)
#     solutions = [0 for _ in range(len(A))]
#     solutions[-1] = b[-1] / A[-1][-1]
#     for i in range(len(A)-2, -1, -1):
#         # a_copy =  multiply_columns([A[j][i+1] for j in range(len(A))], solutions[i+1], i+1)
#         # subtract_columns(b, a_copy, i+1)
#         solutions[i] = b[i] / A[i][i]
#     return solutions


def main():
    A = Matrix.create_from_list(
        [[0, 0, 2, 1, 2],
         [0, 1, 0, 2, -1],
         [1, 2, 0, -2, 0],
         [0, 0, 0, -1, 1],
         [0, 1, -1, 1, -1]])

    b = Vector([1, 1, -4, -2, -1])

    print(A)
    print(b)

    print(calculate_upper_triangular_matrix(A, b))


if __name__ == "__main__":
    main()
