import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def normal_distribution(n=1000):
    return np.random.normal(loc=0, scale=1, size=n)


def normal_dist_density(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)


def ln_normal_dist_density(x):
    return 1 /x*normal_dist_density(np.log(x))


if __name__ == '__main__':
    # podpunkt c)
    x = np.loadtxt(r".\tekst.txt")
    y = np.exp(x)
    plt.plot(x)
    plt.plot(y)
    plt.show()

    # podpunkt d)
    sns.histplot(x, stat='count')
    plt.show()
    sns.histplot(y, stat='count')
    plt.show()

    # podpunkt e)
    sorted_x = np.sort(x)
    sorted_y = np.sort(y)
    sns.histplot(x, stat='density')
    plt.plot(sorted_x, normal_dist_density(sorted_x), color='red')
    plt.show()
    sns.histplot(y, stat='density')
    plt.plot(sorted_y, ln_normal_dist_density(sorted_y), color='yellow')
    plt.show()

    # podpunkt f)
    x = normal_distribution()
    sns.kdeplot(x)
    x = np.sort(x)
    plt.plot(x, normal_dist_density(x), color='green')
    plt.show()

