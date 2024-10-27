import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as ss


def normal_dist_density(x, miu, sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-miu)**2/(2*sigma**2))


def u_dist(u, F, miu, sigma, n=1000):
    return np.power(F(u, loc=miu, scale=sigma), n)


def u_density(u, f, F, miu, sigma, n=1000):
    return n * np.power(F(u, loc=miu, scale=sigma), n-1) * f(u, miu, sigma)


def f(x, miu, sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-miu)**2 /(2*sigma**2))


def g(x, miu, sigma):
    return 1/(np.sqrt(2*np.pi)*sigma*x)*np.exp(-(np.log(x)-miu)**2 /(2*sigma))


def theor_pareto_dist(x, lamb=1, alfa=3):
    return 1 - np.power((lamb / (lamb + x)), alfa)


def theor_pareto_density(x, lamb=1, alfa=3):
    return alfa / (lamb + x) * np.power((lamb / (lamb + x)), alfa)


def emp_pareto(lamb=1, alfa=3, n=1000):
    return lamb*(1 / (np.random.rand(n)) ** (1 / alfa) - 1)


def normal():
    miu = 2
    sigma = 1
    n = 1000
    arr = []

    # Rozkład statystyki U = max{X_1,..., X_n}, gdzie X ~ N(miu, sigma)

    # Empiryczne wyznaczanie dystrybuanty i gęstości
    for i in range(n):
        u = np.random.normal(miu, sigma, n)
        arr.append(np.max(u))

    x = np.linspace(0, 10, 1000)
    y1 = u_dist(x, ss.norm.cdf, miu, sigma, n)
    y2 = u_density(x, f, ss.norm.cdf, miu, sigma, n)

    sns.ecdfplot(arr)
    plt.plot(x, y1, color='orange')
    plt.title(r'Dystrybuanta statystyki $U = \max\{X_1, ..., X_n\}$, gdzie $X \sim N(\mu, \sigma)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['dyst. emp.', 'dyst. teor.'])
    plt.grid(True)
    plt.show()

    sns.histplot(arr, stat='density')
    plt.plot(x, y2, color='orange')
    plt.title(r'Gęstość statystyki $U = \max\{X_1, ..., X_n\}$, gdzie $X \sim N(\mu, \sigma)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['gęstość teor.', 'gęstość emp.'])
    plt.grid(True)
    plt.show()


def lognormal():
    miu = 2
    sigma = 1
    n = 1000
    arr = []
    for i in range(n):
        u = np.random.lognormal(miu, sigma, n)
        arr.append(np.max(u))

    x = np.linspace(0.1, 1000, 1000)
    y1 = np.power(ss.lognorm.cdf(x, 1, loc=miu, scale=np.exp(miu)), n)
    y2 = n * np.power(ss.lognorm.cdf(x, 1, loc=miu, scale=np.exp(miu)), n-1) * ss.lognorm.pdf(x, 1, loc=miu, scale=np.exp(miu))

    sns.ecdfplot(arr)
    plt.plot(x, y1, color='green')
    plt.title(r'Dystrybuanta statystyki $U = \max\{X_1, ..., X_n\}$, gdzie $X \sim \log N(\mu, \sigma)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['dyst. emp.', 'dyst. teor.'])
    plt.grid(True)
    plt.show()

    sns.histplot(arr, stat='density')
    plt.plot(x, y2, color='green')
    plt.title(r'Gęstość statystyki $U = \max\{X_1, ..., X_n\}$, gdzie $X \sim \log N(\mu, \sigma)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['gęstość teor.', 'gęstość emp.'])
    plt.grid(True)
    plt.show()


def pareto():
    lambd = 1
    alfa = 3
    n = 1000
    arr = []
    for i in range(n):
        u = emp_pareto(lambd, alfa, n)
        arr.append(np.max(u))

    x = np.linspace(0, 100, 1000)
    y1 = np.power(theor_pareto_dist(x, lambd, alfa), n)
    y2 = n * np.power(theor_pareto_dist(x, lambd, alfa), n-1) * theor_pareto_density(x, lambd, alfa)

    sns.ecdfplot(arr)
    plt.plot(x, y1, color='yellow')
    plt.show()

    sns.histplot(arr, stat='density')
    plt.plot(x, y2, color='yellow')
    plt.show()


if __name__ == '__main__':
    normal()
    lognormal()
    pareto()
