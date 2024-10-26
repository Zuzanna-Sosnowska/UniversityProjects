import scipy
import functions
import numpy as np


def main():
    A = [[2, -1, 0, 0, 0, 0],
         [-1, 2, -1, 0, 0, 0],
         [0, -1, 2, -1, 0, 0],
         [0, 0, -1, 2, -1, 0],
         [0, 0, 0, -1, 2, -1],
         [0, 0, 0, 0, -1, 5]]
    B = [[2, -1, 0, 0, 0, 0],
         [-1, 2, -1, 0, 0, 0],
         [0, -1, 2, -1, 0, 0],
         [0, 0, -1, 2, -1, 0],
         [0, 0, 0, -1, 2, -1],
         [0, 0, 0, 0, -1, 5]]

    print(np.array(functions.inverse_matrix(B)))
    print(scipy.linalg.inv(A))


if __name__ == '__main__':
     main()
