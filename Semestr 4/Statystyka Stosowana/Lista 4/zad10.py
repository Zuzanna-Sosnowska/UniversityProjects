import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def normal_dist(miu, sigma, n=1000):
    x = np.linspace(-5, 5, n)
    y = 1/(2*np.sqrt(np.pi)*sigma) * np.exp(-(x-miu)**2 / (2*sigma**2))
    return x, y


if __name__ == '__main__':
    n = 1000
    miu = 1
    sigma = 2
    u1 = np.zeros(n)
    u2 = np.zeros(n)
    for i in range(n):
        x = np.random.normal(loc=miu, scale=sigma, size=7)
        u1[i] = np.sum(x)/7
        u2[i] = (2*x[0]-x[5]+x[3])/2
    np.sort(u1)
    np.sort(u2)

    plt.boxplot([u1, u2], positions=[1, 1.5])
    plt.xticks([1, 1.5], ['u1', 'u2'])
    plt.show()

    x, y = normal_dist(miu, sigma)

    # plt.hist(u1, density=True)
    # plt.plot(x, y)
    # plt.show()
    #
    # plt.hist(u2, density=True)
    # plt.plot(x, y)
    # plt.show()

    sns.ecdfplot(u1)
    plt.show()

    sns.ecdfplot(u2)
    plt.show()
