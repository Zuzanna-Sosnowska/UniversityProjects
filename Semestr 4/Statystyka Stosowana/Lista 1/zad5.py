import matplotlib.pyplot as plt
import numpy as np
import zad234 as par
import seaborn as sns


# podpunkt b)
def emp_burro(lamb=1, alfa=3, tau=2, n=1000):
    x = par.emp_pareto(lamb, alfa, n)
    return np.power(x, 1/tau)


def burro_density(x, lamb=1, alfa=3, tau=2):
    return alfa * tau / (lamb + np.power(x, tau)) * np.power((lamb/(lamb + np.power(x, tau))), alfa)\
        * np.power(x, tau - 1)


def burro_dist(x, lamb=1, alfa=3, tau=2):
    return 1 - np.power((lamb/(lamb + np.power(x, tau))), alfa)


if __name__ == '__main__':
    # podpunkt c)
    x = emp_burro()
    x_sorted = np.sort(x)
    sns.kdeplot(x)
    plt.plot(x_sorted, burro_density(x_sorted), color='red')
    plt.show()

    # podpunkt d)
    sns.ecdfplot(x)
    plt.plot(x_sorted, burro_dist(x_sorted), color='red')
    plt.show()
