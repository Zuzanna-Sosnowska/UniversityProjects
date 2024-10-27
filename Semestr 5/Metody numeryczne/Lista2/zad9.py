import scipy
import functions
import numpy as np
import copy


def main():
    A = [[1, 3, -9, 6, 4],
         [2, -1, 6, 7, 1],
         [3, 2, -3, 15, 5],
         [8, -1, 1, 4, 2],
         [11, 1, -2, 18, 7]]
    B = copy.deepcopy(A)
    C = copy.deepcopy(A)

    print(np.array(functions.inverse_matrix(A)), '\n')
    print(scipy.linalg.inv(B), '\n')
    print(np.linalg.inv(C))


if __name__ == '__main__':
    main()
