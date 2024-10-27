import matplotlib.pyplot as plt
import numpy as np


def arithmetic_mean(data):
    return np.sum(data)/len(data)


def f_distribution(a, n=1000):
    u = np.random.uniform(0, 1, n)
    return np.power(u, 1/(a+1))


def a1_estimator(data):
    return 1/(1 - arithmetic_mean(data)) - 2


def a2_estimator(data):
    return - 1 - len(data) / np.sum(np.log(data))


def main():
    a = 2
    n = 1000
    a1 = np.zeros(n)
    a2 = np.zeros(n)
    for i in range(n):
        a1[i] = a1_estimator(f_distribution(a, n))
        a2[i] = a2_estimator(f_distribution(a, n))

    np.sort(a2)
    np.sort(a1)

    fig, ax = plt.subplots()

    ax.boxplot([a1, a2])
    ax.set_xticklabels(['Metoda momentów', 'Metoda największej wiarogodności'])
    ax.set_title('Porównanie boxplotów')
    ax.set_ylabel('Wartości')

    plt.show()


if __name__ == '__main__':
    main()
