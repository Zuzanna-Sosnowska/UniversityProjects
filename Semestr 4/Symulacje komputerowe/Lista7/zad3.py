import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy
import math


def inverse_dist(lambda_func, c, T):
    u = np.random.uniform(0, 1)
    return scipy.optimize.fsolve(func=lambda x: scipy.integrate.quad(func=lambda_func, a=0, b=x)[0] - c*u, x0=T,
                          fprime=lambda_func)[0]


def non_uniform_poisson_process2(lambda_func, T):
    mT = scipy.integrate.quad(lambda_func, 0, T)[0]
    n = np.random.poisson(mT)
    times = np.array([inverse_dist(lambda_func, mT, T) for _ in range(n)])
    times.sort()
    return times, n


def lambda_func1(x, a=0.2):
    return a * x


def lambda_func2(x, a=0.1):
    return a * x + a


def poisson_dist(lambd, n=100):
    x = np.linspace(0, n-1, n)
    y = np.zeros(n)
    val = 0
    for i in range(n):
        val += math.exp(-lambd) * lambd ** i / math.factorial(i)
        y[i] = val
    return x, y


def calculate_Nt(lambda_func, T, n=1000):
    N_t = np.zeros(n)
    for i in range(n):
        N_t[i] = non_uniform_poisson_process2(lambda_func, T)[1][-1]
    return N_t


def main():
    T1 = 10
    T2 = 15
    x1, N1 = non_uniform_poisson_process2(lambda_func1, T1)
    x2, N2 = non_uniform_poisson_process2(lambda_func2, T2)
    N = N1 + N2
    x2 = x2 + T1
    x = np.concatenate((x1, x2))
    y = np.linspace(0, N - 1, N)

    for i in range(len(x)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i]], color='black')
        plt.plot([x[i+1], x[i+1]], [y[i], y[i+1]], color='black', linestyle='--')
        plt.scatter(x[i], y[i], color='black')
        plt.scatter(x[i+1], y[i], color='black', facecolors='none')
    plt.show()


if __name__ == '__main__':
    main()
