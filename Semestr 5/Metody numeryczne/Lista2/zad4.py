import scipy
import functions

def main():
    A = [[0, 0, 2, 1, 2],
         [0, 1, 0, 2, -1],
         [1, 2, 0, -2, 0],
         [0, 0, 0, -1, 1],
         [0, 1, -1, 1, -1]]
    b = [1, 1, -4, -2, -1]

    print(functions.gaussian_solver(A, b))
    print(scipy.linalg.solve(A, b))


if __name__ == '__main__':
    main()
