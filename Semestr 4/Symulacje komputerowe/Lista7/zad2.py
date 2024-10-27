import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy
import math


def non_uniform_poisson_process1(lambda_func, T):
    t = 0
    I = 0
    times = [0]
    steps = [0]
    while t < T:
        u = np.random.uniform(0, 1)
        t = t - np.log(u)
        times.append(scipy.optimize.fsolve(func= lambda x: scipy.integrate.quad(func=lambda_func, a=0, b=x)[0] - t, x0=T, fprime=lambda_func)[0])
        I += 1
        steps.append(I)
    return times, steps


def inverse_dist(lambda_func, c, T):
    u = np.random.uniform(0, 1)
    return scipy.optimize.fsolve(func=lambda x: scipy.integrate.quad(func=lambda_func, a=0, b=x)[0] - c*u, x0=T,
                          fprime=lambda_func)[0]



def non_uniform_poisson_process2(lambda_func, T):
    mT = scipy.integrate.quad(lambda_func, 0, T)[0]
    n = np.random.poisson(mT)
    times = np.array([inverse_dist(lambda_func, mT, T) for _ in range(n)])
    times.sort()
    return times, np.linspace(0, n, n+1)


def lambda_func(x, a=0.2):
    return a * x


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
    T = 10
    # x, y = non_uniform_poisson_process2(lambda_func=lambda_func, T=T)
    # for i in range(len(x)-1):
    #     plt.plot([x[i], x[i+1]], [y[i], y[i]], color='black')
    #     plt.plot([x[i+1], x[i+1]], [y[i], y[i+1]], color='black', linestyle='--')
    #     plt.scatter(x[i], y[i], color='black')
    #     plt.scatter(x[i+1], y[i], color='black', facecolors='none')
    #
    # plt.show()

    lambd = scipy.integrate.quad(lambda_func, 0, T)[0]
    N_t = calculate_Nt(lambda_func, T)
    x1, y1 = poisson_dist(lambd, n=20)

    sns.ecdfplot(N_t)
    for i in range(len(x1) - 1):
        plt.plot([x1[i], x1[i + 1]], [y1[i], y1[i]], color='black')
        plt.plot([x1[i + 1], x1[i + 1]], [y1[i], y1[i + 1]], color='black', linestyle='--')
        plt.scatter(x1[i], y1[i], color='black')
        plt.scatter(x1[i + 1], y1[i], color='black', facecolors='none')
    plt.show()

if __name__ == '__main__':
    main()