import matplotlib.pyplot as plt
import numpy as np


def homogeneous_risk_process(lambd, T, beta, u, theta):
    times, steps = poiss_process(lambd=lambd, T=T)
    x = np.random.exponential(beta, steps)
    ct = (1 + theta) / beta * lambd * times
    step_lst = np.zeros(2*(steps+1))
    for i in range(steps+1):
        step_lst[2*i] = u + ct[i] - np.sum(x[:i])
        step_lst[2*i+1] = u + ct[i+1] - np.sum(x[:i])
    return times, step_lst


def poiss_process(lambd, T):
    n = np.random.poisson(T * lambd)
    times = np.sort(np.random.uniform(0, T, n))
    return np.concatenate((np.array([0]), times, np.array([T]))), n


def exponential_distribution(lambd=1, n=1):
    u = np.random.uniform(0, 1, n)
    return - 1 / lambd * np.log(u)


def main():
    theta = 0.5
    lambd = 1
    beta = 1
    T = 3
    u = 5
    N = 1000
    # x, y = homogeneous_risk_process(lambd=lambd, T=T, beta=beta, u=u, theta=theta)
    # for i in range(len(x)-1):
    #     plt.plot([x[i], x[i+1]], [y[2*i], y[2*i+1]], color='blue')
    #     if i < len(x) - 2:
    #         plt.plot([x[i+1], x[i+1]], [y[2*i+1], y[2*(i+1)]], color='blue', linestyle='--')
    # plt.show()

    M = 1000
    z = 0
    for i in range(M):
        x, y = homogeneous_risk_process(lambd=lambd, T=T, beta=beta, u=u, theta=theta)
        if np.min(y) < 0:
            z += 1
    print(z/M)


if __name__ == '__main__':
    main()
