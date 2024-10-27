import functions
import scipy
import numpy as np

def main():
    A = [[3.50, 2.77, -0.76, 1.80],
         [-1.80, 2.68, 3.44, -0.09],
         [0.27, 5.07, 6.90, 1.61],
         [1.71, 5.45, 2.68, 1.71]]
    b = [7.31, 4.23, 13.85, 11.55]

    print(functions.gaussian_solver(A, b))
    print(scipy.linalg.solve(A, b))


if __name__ == '__main__':
    main()
