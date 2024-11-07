import scipy
import Funkcje
from Matrix import Matrix, Vector

def main():
    A = [[0, 0, 2, 1, 2],
         [0, 1, 0, 2, -1],
         [1, 2, 0, -2, 0],
         [0, 0, 0, -1, 1],
         [0, 1, -1, 1, -1]]
    A = Matrix.create_from_list(A)
    b = Vector([1, 1, -4, -2, -1])

    print(Funkcje.gaussian_solver(A, b))
    print(scipy.linalg.solve(A, b))

    solutions = Funkcje.gaussian_solver(A, b)
    print(solutions)

if __name__ == '__main__':
    main()
