import numpy as np


def wyznaczanie_punktu_zmiany_rezimu():
    pass


def b0_and_b1_est(x, y):
    b1 = np.sum((x - np.mean(x)) * y) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b1, b0


def c_statistic(x):
    return np.sum(np.power(x, 2))


def main():
    N = 1000
    L = 400
    sigma1 = 1
    sigma2 = 5
    x1 = np.random.normal(0, sigma1, L)
    x2 = np.random.normal(0, sigma2, N-L)
    x = [*x1, *x2]
    for k in range(2, N-1):
        b0_k, b1_k = b0_and_b1_est(x, k)
        print('k')



if __name__ == '__main__':
    main()
