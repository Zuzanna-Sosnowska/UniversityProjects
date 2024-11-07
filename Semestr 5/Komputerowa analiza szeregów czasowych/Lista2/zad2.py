import numpy as np
import matplotlib.pyplot as plt


def generate_normal(n, sigma):
    return np.random.normal(loc=0, scale=sigma, size=n)


def calculate_b1_estimator(x, y):
    return np.sum(x * y) / np.sum(x ** 2)


def theoretical_b1_variance(x, sigma):
    return sigma ** 2 / np.sum(x ** 2)


def main():
    n = 1000
    b1 = 2
    M = 5000
    sigma = np.linspace(1, 30, 30)
    u = len(sigma)

    b1_emp_mean = np.zeros(u)
    b1_theor_mean = np.zeros(u)

    b1_emp_var = np.zeros(u)
    b1_theor_var = np.zeros(u)

    for i in range(u):
        x = np.linspace(0, 10, n)
        b1_est = np.zeros(M)
        for j in range(M):
            e = generate_normal(n, sigma[i])
            y = b1 * x + e
            b1_est[j] = calculate_b1_estimator(x, y)

        b1_emp_mean[i] = np.mean(b1_est)
        b1_theor_mean[i] = b1

        b1_emp_var[i] = np.var(b1_est)
        b1_theor_var[i] = theoretical_b1_variance(x, sigma[i])


    plt.plot(np.linspace(0, 10, u), b1_emp_mean)
    plt.plot(np.linspace(0, 10, u), b1_theor_mean, color='r')
    plt.title(r'Średnia $b_1$')
    plt.show()

    plt.plot(np.linspace(0, 10, u), b1_emp_var)
    plt.plot(np.linspace(0, 10, u), b1_theor_var, color='r')
    plt.title(r'Wariancja $b_1$')
    plt.show()


def main2():
    n = np.linspace(50, 1000, 20)
    b1 = 2
    M = 5000
    sigma = 1
    u = len(n)

    b1_emp_mean = np.zeros(u)
    b1_theor_mean = np.zeros(u)

    b1_emp_var = np.zeros(u)
    b1_theor_var = np.zeros(u)

    for i in range(u):
        x = np.linspace(0, 10, int(n[i]))
        b0_est = np.zeros(M)
        b1_est = np.zeros(M)
        for j in range(M):
            e = generate_normal(int(n[i]), sigma)
            y = b1 * x + e
            b1_est[j] = calculate_b1_estimator(x, y)

        b1_emp_mean[i] = np.mean(b1_est)
        b1_theor_mean[i] = b1

        b1_emp_var[i] = np.var(b1_est)
        b1_theor_var[i] = theoretical_b1_variance(x, sigma)


    plt.plot(np.linspace(50, 1000, u), b1_emp_mean)
    plt.plot(np.linspace(50, 1000, u), b1_theor_mean, color='g')
    plt.title(r'Średnia $b_1$')
    plt.show()

    plt.plot(np.linspace(50, 1000, u), b1_emp_var)
    plt.plot(np.linspace(50, 1000, u), b1_theor_var, color='g')
    plt.title(r'Wariancja $b_1$')
    plt.show()


if __name__ == '__main__':
    main()
    main2()
