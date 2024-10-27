import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def arithmetic_mean(data):
    return np.sum(data)/len(data)


def x_distribution(theta, n=1000):
    u = np.random.uniform(0, 1, n)
    return theta - np.log(u)


def density_plot(theta, n=1000):
    x = np.linspace(theta, theta*3, n)
    y = np.exp(-(x-theta))
    return x, y


def dist_plot(theta, n=1000):
    x = np.linspace(theta, theta*3, n)
    y = 1 - np.exp(-(x-theta))
    return x, y


if __name__ == '__main__':
    n = 1000
    theta = 2
    # x1, y1 = density_plot(theta, n)
    # v = x_distribution(theta, n)
    # plt.hist(v, density=True)
    # plt.plot(x1, y1)
    # plt.show()
    #
    # x2, y2 = dist_plot(theta, n)
    #
    # sns.ecdfplot(v)
    # plt.plot(x2, y2)
    # plt.show()

    u1 = np.zeros(n)
    u2 = np.zeros(n)
    for i in range(n):
        u1[i] = np.min(x_distribution(theta, n))
        u2[i] = arithmetic_mean(x_distribution(theta, n)) - 1

    np.sort(u2)
    np.sort(u1)

    fig, ax = plt.subplots()

    ax.boxplot([u1, u2])
    ax.set_xticklabels(['Metoda największej wiarogodności', 'Metoda momentów'])
    ax.set_title('Porównanie boxplotów')
    ax.set_ylabel('Wartości')

    plt.show()
