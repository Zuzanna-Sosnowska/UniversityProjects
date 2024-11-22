import numpy as np
import matplotlib.pyplot as plt


def main():
    B = create_matrix_to_ex_4()
    x_k = np.array([1.0 for _ in range(20)])
    x_0_norm = norm_2(x_k)

    k = 100
    norm2_x_k_divided_by_norm2_x_0 = np.zeros(k + 1)
    for i in range(k + 1):
        norm2_x_k = norm_2(x_k)
        norm2_x_k_divided_by_norm2_x_0[i] = norm2_x_k / x_0_norm
        x_k = B @ x_k

    plt.plot(np.arange(k+1), norm2_x_k_divided_by_norm2_x_0, marker='o')
    plt.axvline(x=26, linestyle='--', color='red')
    plt.xlabel("Iteracje k")
    plt.ylabel(r"$\eta_k = \frac{\|x^{(k)}\|_2}{\|x^{(0)}\|_2}$")
    plt.title("Zmiana $\eta_k$ w zależności od iteracji")
    plt.grid()
    plt.show()

    print(find_min_k(norm2_x_k_divided_by_norm2_x_0) - 1)


def find_min_k(norm2_lst):
    for i in range(len(norm2_lst)):
        if norm2_lst[i] < 1:
            return i


def create_matrix_to_ex_4():
    B = np.zeros((20, 20))
    for i in range(19):
        B[i][i] = 0.025 * (i + 1)
        B[i][i + 1] = 5.0
    B[19][19] = 0.025 * 20
    return B

def norm_2(x):
    return np.sqrt(np.sum(np.power(x, 2)))



if __name__ == '__main__':
    main()

