import scipy
import numpy as np
from matrix.Matrix import Matrix


def main():
    A = Matrix.create_from_list(
        [[2, -1, 0, 0, 0, 0],
         [-1, 2, -1, 0, 0, 0],
         [0, -1, 2, -1, 0, 0],
         [0, 0, -1, 2, -1, 0],
         [0, 0, 0, -1, 2, -1],
         [0, 0, 0, 0, -1, 5]])

    print(A.inv())
    print(np.array(A.inv()))
    print(scipy.linalg.inv(A))
    print(np.linalg.inv(A))


if __name__ == '__main__':
     main()
