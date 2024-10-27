import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# zadanie 2
def emp_pareto(lamb=1, alfa=3, n=1000):
    return lamb*(1 / (np.random.rand(n)) ** (1 / alfa) - 1)


def theor_pareto_dist(x, lamb=1, alfa=3):
    return 1 - np.power((lamb / (lamb + x)), alfa)


def theor_pareto_density(x, lamb=1, alfa=3):
    return alfa / (lamb + x) * np.power((lamb / (lamb + x)), alfa)


if __name__ == '__main__':
    x = emp_pareto()
    sorted_x = np.sort(x)
    # zad 3
    # dystrybuanta empiryczna
    sns.ecdfplot(x)
    # dystrybuanta teoretyczna
    plt.plot(sorted_x, theor_pareto_dist(sorted_x))
    plt.show()

    # zad 4
    # gęstość empiryczna
    sns.histplot(x, stat='density')
    # gęstość teoretyczna
    plt.plot(sorted_x, theor_pareto_density(sorted_x), color='red')
    plt.show()
