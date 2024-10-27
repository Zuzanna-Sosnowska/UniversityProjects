import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def arithmetical_mean(x):
    return np.sum(x)/len(x)


def rozklad_f(theta, n=1000):
    u = np.random.uniform(0, 1, n)
    return theta / np.sqrt(u)


def theor_dist(theta, n):
    x = np.linspace(theta, 30*theta, n)
    y = 1 - theta**2 / x**2
    return x, y


def theor_density(theta, n):
    x = np.linspace(theta+0.5, theta+10, n)
    y = (2 * theta**2) / np.power(x, 3)
    return x, y


def theta_estim1(x):
    return np.min(x)


def theta_estim2(x):
    return 0.5 * arithmetical_mean(x)


def theor_max_dist(theta, a, n):
    x = np.linspace(theta, a, n)
    y = np.power(1 - theta**2 / x**2, n)
    return x, y


def theor_max_density(theta, n):
    x = np.linspace(theta, 260, n)
    y = n * np.power(1 - theta**2 / x**2, n-1) * (2 * theta**2) / np.power(x, 3)
    return x, y


def main():
    theta = 1
    n = 1000
    u = rozklad_f(theta, n)
    x1, y1 = theor_dist(theta, n)
    x2, y2 = theor_density(theta, n)

    # Generowanie Dystrybuant

    # sns.ecdfplot(u, label='empiryczna')
    # plt.plot(x1, y1, label='teoretyczna')
    # plt.title('Porównanie dystrybuant')
    # plt.legend()
    # plt.show()

    # plt.hist(u, density=True, label='empiryczna, reprezentowana przez histogram')
    # plt.plot(x2, y2, label='teoretyczna')
    # plt.title("Porównanie gęstości")
    # plt.legend()
    # plt.show()

    # Testowanie poprawności działania estymatorów

    m = 500
    # a = np.linspace(1, 20*m, m)
    # t1 = np.zeros(m)
    # t2 = np.zeros(m)
    # for i in range(m):
    #     u = rozklad_f(theta, (i+1)*20)
    #     t1[i] = theta_estim1(u)
    #     t2[i] = theta_estim2(u)
    #
    # plt.plot(a, t1, label='wartość estymatora')
    # plt.axhline(y=theta, color='r', linestyle='--', label='rzeczywista wartość parametru')
    # plt.title('Wartość estymatora wyznaczonego metodą NW \n w zależności od długości próby')
    # plt.xlabel('Długość próby')
    # plt.ylabel('Warość estymatora')
    # plt.legend()
    # plt.show()
    #
    # plt.plot(a, t2, label='wartość estymatora')
    # plt.axhline(y=theta, color='r', linestyle='--', label='rzeczywista wartość parametru')
    # plt.title('Wartość estymatora wyznaczonego metodą momentów \n w zależności od długości próby')
    # plt.xlabel('Długość próby')
    # plt.ylabel('Warość estymatora')
    # plt.legend()
    # plt.show()

    # Testowanie poprawności wyznaczonych rozkładów teoretycznych statystyki U_max

    m = 1000

    u = np.zeros(m)
    for i in range(m):
        q = rozklad_f(theta, n)
        u[i] = np.max(q)

    a = sns.ecdfplot(u, label='empiryczna').lines[0].get_xdata()

    x3, y3 = theor_max_dist(theta, a[-1], n)
    x4, y4 = theor_max_density(theta, n)

    plt.plot(x3, y3, 'r', label='teoretyczna')
    plt.title('Porównanie dystrybuant')
    plt.legend()
    plt.show()

    # plt.hist(u, density=True, label='empiryczna')
    sns.distplot(u, label='empiryczna')
    plt.plot(x4, y4, 'r', label='teoretyczna')
    plt.title('Porównanie gęstości')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
