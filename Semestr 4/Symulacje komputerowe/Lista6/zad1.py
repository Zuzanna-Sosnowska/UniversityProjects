import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns


def poisson_process(lambd, T):
    t = 0
    step = 0
    times = [0]
    steps = [0]
    while t < T:
        t += np.random.exponential(1 / lambd)
        if t > T:
            break
        step += 1
        times.append(t)
        steps.append(step)
    return times, steps


def poisson_dist(lambd, n=100):
    x = np.linspace(0, n-1, n)
    y = np.zeros(n)
    val = 0
    for i in range(n):
        val += math.exp(-lambd) * lambd ** i / math.factorial(i)
        y[i] = val
    return x, y


def main():
    lambd = 2
    T = 10
    x, y = poisson_process(lambd, T)
    for i in range(len(x)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i]], color='black')
        plt.plot([x[i+1], x[i+1]], [y[i], y[i+1]], color='black', linestyle='--')
        plt.scatter(x[i], y[i], color='black')
        plt.scatter(x[i+1], y[i], color='black', facecolors='none')
    plt.show()

    n = 10000
    N_T = np.zeros(n)
    for i in range(n):
        N_T[i] = poisson_process(lambd, T)[1][-1]

    lambd = lambd * T
    x1, y1 = poisson_dist(lambd , 40)

    sns.ecdfplot(N_T)
    for i in range(2 * int(lambd) - 1):
        plt.scatter(x1[i], y1[i], color='r')
        plt.plot([x1[i], x1[i + 1]], [y1[i], y1[i]], color='r')
        plt.scatter(x1[i + 1], y1[i], facecolors='none', color='r')
    plt.show()


if __name__ == '__main__':
    main()
