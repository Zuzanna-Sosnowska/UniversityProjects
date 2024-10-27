import numpy as np
import matplotlib.pyplot as plt


def pareto(x_0, alfa, n=1000):
    u = np.random.uniform(0, 1, n)
    return np.power(u, -1/alfa) * x_0


def estimate_x0(x):
    return np.min(x)


def estimate_alpha(x):
    x0 = estimate_x0(x)
    n = len(x)
    return n/np.sum(np.log(x/x0))


if __name__ == '__main__':
    x0 = 2
    alpha = 5
    n = 1000
    m = 1000
    alpha_arr = []
    x0_arr = []
    for i in range(m):
        a = pareto(x0, alpha, n)
        x0_arr.append(estimate_x0(a))
        alpha_arr.append(estimate_alpha(a))

    np.sort(alpha_arr)
    np.sort(x0_arr)

    plt.boxplot(alpha_arr)
    plt.axhline(y=alpha, color='r')
    plt.show()

    plt.boxplot(x0_arr)
    plt.axhline(y=x0, color='r')
    plt.show()
