#
# def gaussian_solver(A, b):
#     solutions = [0 for _ in range(len(A))]
#     solutions[-1] = b[-1] / A[-1][-1]
#     b_copy = b.copy()
#     for i in range(len(A)-2, -1, -1):
#         a_copy =  multiply_columns([A[j][i+1] for j in range(len(A))], solutions[i+1])
#         subtract_columns(b_copy, a_copy)
#         solutions[i] = b_copy[i] / A[i][i]
#     return solutions
#
#
# def upper_triangular_matrix(A):
#     n = len(A)
#     for j in range(n):
#         c = False
#         for i in range(j, n):
#             if A[i][j] != 0 and c == False:
#                 swap_rows(A, i, j)
#                 c = True
#                 continue
#             if c:
#                 change_rows(A[i], A[j], j)
#         if not c:
#             raise ValueError("Macierz osobliwa")
#
#
# def det(A):
#     upper_triangular_matrix(A)
#     det = 1
#     for i in range(len(A)):
#         det *= A[i][i]
#     return det
#
#
# def identity_matrix(n):
#     I = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 I[i][j] = 1
#             else:
#                 I[i][j] = 0
#     return I
#
#
# def inverse_matrix(A):
#     n = len(A)
#     I = identity_matrix(n)
#     for j in range(n):
#         c = False
#         for i in range(j, n):
#             if A[i][j] != 0 and c == False:
#                 swap_rows(A, i, j)
#                 swap_rows(I, i, j)
#                 c = True
#                 continue
#             if c:
#                 a = change_rows(A[i], A[j], j)
#                 change_rows(I[i], I[j], a)
#         if not c:
#             raise ValueError("Macierz osobliwa")
#
#     for j in range(n-1, -1, -1):
#         for i in range(n-1, j, -1):
#             a = change_rows(A[i], A[j], j)
#             change_rows(I[i], I[j], a)
#         I[j][j] /= A[j][j]
#         A[j][j] /= A[j][j]
#
#     return I

