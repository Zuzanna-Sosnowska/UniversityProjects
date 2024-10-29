import numpy as np


def generate_t_student(n, v):
    return np.random.standard_t(df=v, size=n)


def calculate_b0_and_b1_estimator(x, y):
    x_m = np.mean(x)
    y_m = np.mean(y)
    b1_est = np.sum((x - x_m) * (y - y_m)) / np.sum((x - x_m) ** 2)
    b0_est = y_m - b1_est * x_m
    return b0_est, b1_est


def variance(x, obciążenie=True):
    if obciążenie:
        return 1 / len(x) * np.sum((x - np.mean(x)) ** 2)
    else:
        return 1 / (len(x) - 1) * np.sum((x - np.mean(x)) ** 2)


def theoretical_b0_variance(x, v):
    n = len(x)
    x_m = np.mean(x)
    return (1 / n + x_m ** 2 / np.sum((x - x_m) ** 2)) * (v / (v - 2))


def theoretical_b1_variance(x, v):
    n = len(x)
    x_m = np.mean(x)
    return 1 / np.sum((x - x_m) ** 2) * (v / (v - 2))


def main():
    n = 1000
    b0 = 5
    b1 = 2
    M = 5000
    v = 5

    x = np.linspace(0, 10, n)
    b0_est = np.zeros(M)
    b1_est = np.zeros(M)
    for i in range(M):
        e = generate_t_student(n, v)
        y = b0 + b1 * x + e
        b0_est[i], b1_est[i] = calculate_b0_and_b1_estimator(x, y)

    sr_est_b0 = np.mean(b0_est)
    sr_est_b1 = np.mean(b1_est)
    var_est_b0 = np.var(b0_est)
    var_est_b1 = np.var(b1_est)

    theor_b0_var = theoretical_b0_variance(x, v)
    theor_b1_var = theoretical_b1_variance(x, v)

    print('Średnia wartość empiryczna estymatora b_0 i jego wartość teoretyczna:')
    print(sr_est_b0, b0, '\n\n')

    print('Średnia wartość empiryczna estymatora b_1 i jego wartość teoretyczna:')
    print(sr_est_b1, b1, '\n\n')

    print('Wariancja empiryczna estymatora b_0 i jego wartość teoretyczna:')
    print(var_est_b0, theor_b0_var, '\n\n')

    print('Wariancja empiryczna estymatora b_1 i jego wartość teoretyczna:')
    print(var_est_b1, theor_b1_var, '\n\n')


if __name__ == '__main__':
    main()
