import scipy
import functions
import numpy as np
import copy


def main():
    A = [[2, -1, 0, 0, 0, 0],
         [-1, 2, -1, 0, 0, 0],
         [0, -1, 2, -1, 0, 0],
         [0, 0, -1, 2, -1, 0],
         [0, 0, 0, -1, 2, -1],
         [0, 0, 0, 0, -1, 5]]
    B = copy.deepcopy(A)
    print(np.array(functions.inverse_matrix(B)), '\n')
    print(scipy.linalg.inv(A))


if __name__ == '__main__':
     main()
