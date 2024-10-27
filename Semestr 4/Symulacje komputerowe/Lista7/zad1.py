import matplotlib.pyplot as plt
import numpy as np
import scipy
import seaborn as sns
import math


def lambda_func(t):
    return 0.1 * t


def find_sup(func, interval, n=1000):
    x = np.linspace(interval[0], interval[1], n)
    y = func(x)
    return np.max(y)


def non_uniform_poiss_process(lambda_func, T, n=1000):
    t = 0
    I = 0
    times = [0]
    steps = [0]
    lambd = find_sup(lambda_func, [0, T], n)
    while t < T:
        u1 = np.random.uniform(0, 1)
        t = t - 1 / lambd * np.log(u1)
        if t > T:
            break
        u2 = np.random.uniform(0, 1)
        if u2 <= lambda_func(t) / lambd:
            I += 1
            steps.append(I)
            times.append(t)
    return times, steps


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
        N_t[i] = non_uniform_poiss_process(lambda_func, T, n)[1][-1]
    return N_t


def main():
    T = 15
    x, y = non_uniform_poiss_process(lambda_func, T)
    for i in range(len(x)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i]], color='black')
        plt.plot([x[i+1], x[i+1]], [y[i], y[i+1]], color='black', linestyle='--')
        plt.scatter(x[i], y[i], color='black')
        plt.scatter(x[i+1], y[i], color='black', facecolors='none')
    plt.show()

    lambd = scipy.integrate.quad(lambda_func, 0, T)[0]
    N_t = calculate_Nt(lambda_func, T)
    x1, y1 = poisson_dist(lambd, n=30)

    sns.ecdfplot(N_t)
    for i in range(len(x1)-1):
        plt.plot([x1[i], x1[i+1]], [y1[i], y1[i]], color='black')
        plt.plot([x1[i+1], x1[i+1]], [y1[i], y1[i+1]], color='black', linestyle='--')
        plt.scatter(x1[i], y1[i], color='black')
        plt.scatter(x1[i+1], y1[i], color='black', facecolors='none')
    plt.show()



if __name__ == '__main__':
    main()
