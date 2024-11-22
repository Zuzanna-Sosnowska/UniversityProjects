from matrix.Matrix import Matrix
from matrix.Vector import Vector
import matplotlib.pyplot as plt
import zad2
import scipy
import numpy as np
import time


def main():
    a = 10
    m = 10
    n_lst = [10 * i for i in range(a, a + m)]
    accuracy = [10 ** (-i * 4) for i in range(4)]
    t_np = np.zeros(m)
    t_sp = np.zeros(m)
    t_gs = {a: np.zeros(m) for a in accuracy}

    for i, n in enumerate(n_lst):
        A = zad2.create_matrix_to_ex_2(n)
        b = zad2.create_vector_to_ex_2(n)
        t_np[i] = measure_solving_time((A, b), np.linalg.solve)
        t_sp[i] = measure_solving_time((A, b), scipy.linalg.solve)

        for acc in accuracy:
            t_gs[acc][i] = measure_solving_time((A, b, acc), zad2.gauss_seidle_method)
        print('a')

    plt.plot(n_lst, t_gs[accuracy[0]], label='Gauss seidler method', color='blue')
    plt.plot(n_lst, t_np, label='Numpy', color='red')
    plt.plot(n_lst, t_sp, label='Scipy', color='green')
    plt.title("Porównanie czasu rozwiązywania układu równań metodą Gaussa-Seidle'a")
    plt.xlabel('Rozmiar macierzy')
    plt.ylabel('Czas obliczania rozwiązań')
    plt.grid(True)
    plt.legend()
    plt.show()

    for acc in accuracy:
        plt.plot(n_lst, t_gs[acc], label=f'Accuracy = {acc}')
    plt.legend()
    plt.show()


def measure_solving_time(args, func, rep=10):
    times = np.zeros(rep)
    for i in range(rep):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        times[i] = end_time - start_time
    return np.mean(times)


if __name__ == '__main__':
    main()
