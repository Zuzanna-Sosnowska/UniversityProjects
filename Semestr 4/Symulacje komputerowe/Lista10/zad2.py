import numpy as np
import matplotlib.pyplot as plt


def complex_poisson_process(lambd, T, step_func, params):
    t = 0
    I = 0
    N_t = np.random.poisson(lambd * T)
    times = np.random.uniform(0, T, N_t)
    times.sort()
    steps = np.zeros(N_t)
    for i in range(1, N_t):
        I += step_func(*params)
        steps[i] = I[0]
    return times, steps


def main():
    a = ['green', 'red', 'blue', 'yellow', 'orange']
    counter = 1
    plt.figure(figsize=(10, 6))
    for j in a:
        lambd = 2
        T = 20
        x, y = complex_poisson_process(lambd, T, np.random.standard_cauchy, [1])
        for i in range(len(x)-1):
            plt.plot([x[i], x[i+1]], [y[i], y[i]], color=j)
            plt.plot([x[i+1], x[i+1]], [y[i], y[i+1]], color=j)
            # plt.scatter(x[i], y[i], color=j)
            # plt.scatter(x[i+1], y[i], color=j, facecolors='none')
    plt.title('Wykres złożonego procesu Poissona ze skokami z rozkładu C(0, 1)')
    plt.grid(True)
    plt.show()

    a = ['green', 'red', 'blue', 'yellow', 'orange']
    counter = 1
    plt.figure(figsize=(10, 6))
    for j in a:
        lambd = 2
        T = 20
        x, y = complex_poisson_process(lambd, T, np.random.normal, [0, 1, 1])
        for i in range(len(x) - 1):
            plt.plot([x[i], x[i + 1]], [y[i], y[i]], color=j)
            plt.plot([x[i + 1], x[i + 1]], [y[i], y[i + 1]], color=j)
            # plt.scatter(x[i], y[i], color=j)
            # plt.scatter(x[i+1], y[i], color=j, facecolors='none')
    plt.title('Wykres złożonego procesu Poissona ze skokami z rozkładu N(0, 1)')
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    main()
