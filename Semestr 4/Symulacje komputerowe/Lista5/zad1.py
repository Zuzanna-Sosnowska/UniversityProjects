import matplotlib.pyplot as plt
import numpy as np
import random
import time


def box_muller(n=50000):
    u = np.random.uniform(low=0, high=1, size=n)
    v = np.random.uniform(low=0, high=1, size=n)

    x = np.power(-2 * np.log(u), 0.5) * np.cos(2 * np.pi * v)
    y = np.power(-2 * np.log(u), 0.5) * np.sin(2 * np.pi * v)
    return x, y


def polar_method(n=50000):
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(n):
        u = random.uniform(-1, 1)
        v = random.uniform(-1, 1)
        r = v*v + u*u
        while r > 1:
            u = random.uniform(-1, 1)
            v = random.uniform(-1, 1)
            r = u*u + v*v
        x[i] = np.sqrt(-2 * np.log(r) / r) * u
        y[i] = np.sqrt(-2 * np.log(r) / r) * v
    return x, y


def time_plot(f, n):
    lst = []
    execution_times = []

    for i in range(n):
        start_time = time.time()
        f((i + 1) * 10000)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        lst.append(i + 1)
    return lst, execution_times


def main():
    # Testowanie, czy metoda działa (sprawdzamy, czy gęstość empiryczna jest równa gęstości teoretycznej)

    # x_1 = np.linspace(-4, 4, 50000)
    # y_1 = 1/np.sqrt(2*np.pi)*np.exp(-x_1**2/2)
    #
    # x, y = polar_method(n=50000)
    #
    # sns.displot(x, bins=30, stat='density')
    # plt.plot(x_1, y_1, color='red')
    # plt.show()
    #
    # sns.displot(y, bins=30, stat='density')
    # plt.plot(x_1, y_1, color='red')
    # plt.show()

    n = 30
    u1, t1 = time_plot(box_muller, n)
    u2, t2 = time_plot(polar_method, n)

    t = [t1[i]/t2[i] for i in range(len(t1))]

    plt.plot(u1, t1, color='red')
    plt.plot(u2, t2, color='blue')
    plt.title('Porównanie wydajności algorytmu Boxa-Mullera i Marsaglii')
    plt.xlabel(r'Ilość generowanych zmiennych losowych $\cdot 10^4$')
    plt.ylabel(r'Czas działania funkcji $[s]$')
    plt.legend(['boxmuller', 'marsaglia'])
    plt.show()

    plt.plot(u1, t)
    plt.title('Iloraz czasu vs ilość wygenetowanych zm. los.')
    plt.xlabel(r'$t_1/t_2$')
    plt.ylabel(r'ilość zm. los $\cdot 10^4$')
    plt.show()


if __name__ == '__main__':
    main()
