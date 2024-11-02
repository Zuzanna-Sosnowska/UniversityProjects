import numpy as np
import matplotlib.pyplot as plt


def generate_t_student(n, v):
    return np.random.standard_t(df=v, size=n)


def generate_normal(n, sigma):
    return np.random.normal(loc=0, scale=sigma, size=n)


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


def calculate_values_1(n, b0, b1, M, v):
    x = np.linspace(0, 10, n)
    b0_est = np.zeros(M)
    b1_est = np.zeros(M)
    for j in range(M):
        e = generate_t_student(n, v)
        y = b0 + b1 * x + e
        b0_est[j], b1_est[j] = calculate_b0_and_b1_estimator(x, y)
    return (np.mean(b0_est), np.mean(b1_est),
            b0, b1,
            np.var(b0_est), np.var(b1_est),
            theoretical_b0_variance(x, v), theoretical_b0_variance(x, v))


def calculate_values_2(n, b0, b1, M, sigma):
    x = np.linspace(0, 10, n)
    b0_est = np.zeros(M)
    b1_est = np.zeros(M)
    for j in range(M):
        e = generate_normal(n, sigma)
        y = b0 + b1 * x + e
        b0_est[j], b1_est[j] = calculate_b0_and_b1_estimator(x, y)
    return (np.mean(b0_est), np.mean(b1_est),
            b0, b1,
            np.var(b0_est), np.var(b1_est),
            theoretical_b0_variance(x, sigma), theoretical_b0_variance(x, sigma))


def main():
    n = 1000
    b0 = 5
    b1 = 2
    M = 5000
    v = np.linspace(5, 100, 20)
    u = len(v)
    b0_emp_mean = np.zeros(u)
    b1_emp_mean = np.zeros(u)
    b0_theor_mean = np.zeros(u)
    b1_theor_mean = np.zeros(u)

    b0_emp_var = np.zeros(u)
    b1_emp_var = np.zeros(u)
    b0_theor_var = np.zeros(u)
    b1_theor_var = np.zeros(u)

    for i in range(u):
        b0_emp_mean[i], b1_emp_mean[i], b0_theor_mean[i], b1_theor_mean[i], b0_emp_var[i], b1_emp_var[i], b0_theor_var[i], b1_theor_var[i] = calculate_values_1(n, b0, b1, M, v)

    plt.plot(np.linspace(0, 10, u), b0_emp_mean)
    plt.plot(np.linspace(0, 10, u), b0_theor_mean, color='r')
    plt.title(r'Średnia $b_0$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b1_emp_mean)
    plt.plot(np.linspace(0, 10, u), b1_theor_mean, color='r')
    plt.title(r'Średnia $b_1$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b0_emp_var)
    plt.plot(np.linspace(0, 10, u), b0_theor_var, color='r')
    plt.title(r'Wariancja $b_10$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b1_emp_var)
    plt.plot(np.linspace(0, 10, u), b1_theor_var, color='r')
    plt.title(r'Wariancja $b_1$')
    plt.show()


def main2():
    n = np.linspace(50, 1000, 20)
    b0 = 5
    b1 = 2
    M = 5000
    v = 5
    u = len(n)
    b0_emp_mean = np.zeros(u)
    b1_emp_mean = np.zeros(u)
    b0_theor_mean = np.zeros(u)
    b1_theor_mean = np.zeros(u)

    b0_emp_var = np.zeros(u)
    b1_emp_var = np.zeros(u)
    b0_theor_var = np.zeros(u)
    b1_theor_var = np.zeros(u)

    for i in range(u):
        x = np.linspace(0, 10, int(n[i]))
        b0_est = np.zeros(M)
        b1_est = np.zeros(M)
        for j in range(M):
            e = generate_t_student(int(n[i]), v)
            y = b0 + b1 * x + e
            b0_est[j], b1_est[j] = calculate_b0_and_b1_estimator(x, y)

        b0_emp_mean[i] = np.mean(b0_est)
        b1_emp_mean[i] = np.mean(b1_est)
        b0_theor_mean[i] = b0
        b1_theor_mean[i] = b1

        b0_emp_var[i] = np.var(b0_est)
        b1_emp_var[i] = np.var(b1_est)
        b0_theor_var[i] = theoretical_b0_variance(x, v)
        b1_theor_var[i] = theoretical_b1_variance(x, v)


    plt.plot(np.linspace(0, 10, u), b0_emp_mean)
    plt.plot(np.linspace(0, 10, u), b0_theor_mean)
    plt.title(r'Średnia $b_0$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b1_emp_mean)
    plt.plot(np.linspace(0, 10, u), b1_theor_mean)
    plt.title(r'Średnia $b_1$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b0_emp_var)
    plt.plot(np.linspace(0, 10, u), b0_theor_var)
    plt.title(r'Wariancja $b_10$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b1_emp_var)
    plt.plot(np.linspace(0, 10, u), b1_theor_var)
    plt.title(r'Wariancja $b_1$')
    plt.show()


def main3():
    n = 1000
    b0 = 5
    b1 = 2
    M = 5000
    # b0_emp_mean = np.zeros(u)
    # b1_emp_mean = np.zeros(u)
    # b0_theor_mean = np.zeros(u)
    # b1_theor_mean = np.zeros(u)
    #
    # b0_emp_var = np.zeros(u)
    # b1_emp_var = np.zeros(u)
    # b0_theor_var = np.zeros(u)
    # b1_theor_var = np.zeros(u)


if __name__ == '__main__':
    main()
    # main2()
