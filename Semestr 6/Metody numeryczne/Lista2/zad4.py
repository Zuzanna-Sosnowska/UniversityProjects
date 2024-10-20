def multipy_matrix(A, B):
    if len(A) != len(B):
        raise ValueError("A and B must be the same length")


def main():
    A = [[0, 0, 2, 1, 2],
         [0, 1, 0, 2, -1],
         [1, 2, 0, -2, 0],
         [0, 0, 0, -1, 1],
         [0, 1, -1, 1, -1]]
    b = [1, 1, -4, -2, -1]