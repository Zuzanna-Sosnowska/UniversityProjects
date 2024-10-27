import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# podpunkt a)
def rozklad_f(k, lambd, n=1000):
    u = np.random.uniform(0, 1, n)
    return lambd * np.power(np.log(1/u), 1/k)


# podpunkt b)
def theor_dist(k, lambd, n=1000):
    x = np.linspace(0, 10, n)
    y = 1 - np.exp(-np.power((x/lambd), k))
    return x, y


def theor_density(k, lambd, n=1000):
    x = np.linspace(0, 10, n)
    y = np.exp(-np.power((x/lambd), k)) * k/lambd * np.power(x/lambd, k-1)
    return x, y


# podpunkt c)
def theor_max_dist(k, lambd, n=1000):
    x = np.linspace(0, 10, n)
    y = np.power(1 - np.exp(-np.power((x/lambd), k)), n)
    return x, y


# podpunkt d)
def arithmetic_mean(x):
    return np.sum(x) / len(x)


def lambda_estimator(x):
    a = arithmetic_mean(x)
    return np.sqrt(np.sum((x - a)**2) / (len(x) - 1))


def main():
    n = 1000
    k = 2
    lambd = 2

    """
    u = rozklad_f(k, lambd, n)
    x1, y1 = theor_dist(k, lambd, n)
    x2, y2 = theor_density(k, lambd, n)

    plt.hist(u, density=True)
    plt.plot(x2, y2)
    plt.show()

    sns.ecdfplot(u)
    plt.plot(x1, y1)
    plt.show()
    """

    """
    m = 500
    u = np.zeros(m)
    for i in range(m):
        t = rozklad_f(k, lambd, n)
        u[i] = np.max(t)

    x3, y3 = theor_max_dist(k, lambd, n)

    sns.ecdfplot(u)
    plt.plot(x3, y3)
    plt.show()
    """

    k = 1

    l1 = np.zeros(100)
    l2 = np.zeros(100)
    for a in range(1, 101):
        q1 = []
        q2 = []
        for i in range(n):
            u = rozklad_f(k, lambd, a * 10)
            q1.append(arithmetic_mean(u))
            q2.append(lambda_estimator(u))
        l1[a-1] = arithmetic_mean(q1)
        l2[a-1] = arithmetic_mean(q2)

    plt.plot([10 * a for a in range(1, 101)], l1)
    plt.axhline(y=lambd, color='r')
    plt.show()

    plt.plot([10 * a for a in range(1, 101)], l2)
    plt.axhline(y=lambd, color='g')
    plt.show()

    # u = rozklad_f(k, lambd, 10)
    # print(arithmetic_mean(u))
    # print(lambda_estimator(u))


if __name__ == '__main__':
    main()
