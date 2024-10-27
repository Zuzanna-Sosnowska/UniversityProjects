import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# ecdfplot
# histplot
# displot
# kdeplot


def theor_y_density(sigma, n):
    x = np.linspace(0, 10, n)
    y = 2 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-x ** 2 / (2 * sigma ** 2))
    return x, y


def theor_y_distribution(miu, sigma, n):
    x = np.linspace(0, 10, n)
    y = stats.norm.cdf(miu + x, miu, sigma) - stats.norm.cdf(miu - x, miu, sigma)
    return x, y


def random_y(miu=0, sigma=1, n=1000):
    return np.abs(np.random.normal(miu, sigma, n) - miu)


if __name__ == '__main__':
    n = 10000
    miu = 2
    sigma = 3
    y = random_y(miu=miu, sigma=sigma, n=n)

    x1, y1 = theor_y_density(sigma, n)
    x2, y2 = theor_y_distribution(miu=miu, sigma=sigma, n=n)

    plt.hist(y, label='empiryczna gęstość', density=True, bins=50)
    plt.plot(x1, y1, label='teoretyczna gęstość', color='red')
    plt.title('Porównanie gęstości')
    plt.legend()
    plt.show()

    sns.ecdfplot(y, label='empiryczna dystybuanta')
    plt.plot(x2, y2, label='teoretyczna dystybuanta', color='red')
    plt.title('Porównanie dystybuant')
    plt.legend()
    plt.show()



