import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# podpunkt a)
def rozklad_f(theta, n=1000):
    u = np.random.uniform(0, 1, n)
    return np.power(u, theta)


def theor_dist(theta, n=1000):
    x = np.linspace(0, 1, n)
    y = np.power(x, 1/theta)
    return x, y


def theor_density(theta, n=1000):
    x = np.linspace(0.01, 1, n)
    y = 1/theta * np.power(x, (1-theta)/theta)
    return x, y


def theta_estim1(x):
    return -1/len(x) * np.sum(np.log(x))


def arithmetical_mean(x):
    return np.sum(x)/len(x)


def theta_estim2(x):
    return 1/(arithmetical_mean(x)) - 1


def theor_max_dist(theta, n=1000):
    x = np.linspace(0.99, 1, n)
    y = np.power(np.power(x, 1/theta), n)
    return x, y


def theor_max_density(theta, n=1000):
    x = np.linspace(0.99, 1, n)
    y = n * np.power(np.power(x, 1/theta), n-1) * 1/theta * np.power(x, (1-theta)/theta)
    return x, y


def main():
    theta = 5
    n = 10000
    u = rozklad_f(theta, n)
    x1, y1 = theor_dist(theta, n)
    x2, y2 = theor_density(theta, n)

    # sns.ecdfplot(u, label="empiryczna")
    # plt.plot(x1, y1, label="teoretyczna")
    # plt.title("Wykresy reprezentujące dystrybuantę")
    # plt.legend()
    # plt.show()
    #
    # plt.hist(u, density=True, label="empiryczna")
    # plt.plot(x2, y2, color='orange', label="teoretyczna")
    # plt.title("Wykresy reprezentujące gęstość")
    # plt.legend()
    # plt.show()

    theta = 8
    m = 1000
    # t1 = np.zeros(m)
    # t2 = np.zeros(m)
    # for i in range(m):
    #     u = rozklad_f(theta, (i+1)*100)
    #     t1[i] = theta_estim1(u)
    #     t2[i] = theta_estim2(u)
    #
    # plt.plot([1+i for i in range(m)], t1, label='estymowane wartości, w zależności do długości próby')
    # plt.axhline(y=theta, color='r', linestyle='--', label=r'rzeczywista wartość $\theta$')
    # plt.title(r'Wartość parametru $\theta$ wyznaczona metodą największej wiarogodności')
    # plt.legend()
    # plt.show()
    #
    # plt.plot([1 + i for i in range(m)], t2, label='estymowane wartości, w zależności do długości próby')
    # plt.axhline(y=theta, color='r', linestyle='--', label=r'rzeczywista wartość $\theta$')
    # plt.title(r'Wartość parametru $\theta$ wyznaczona metodą momentów')
    # plt.legend()
    # plt.show()

    u_max = np.zeros(m)
    for i in range(m):
        u = rozklad_f(theta, n)
        u_max[i] = np.max(u)

    x, y = theor_max_dist(theta, n)
    a, b = theor_max_density(theta, n)

    sns.ecdfplot(u_max, label='empiryczna')
    plt.plot(x, y, label='teoretyczna')
    plt.title(r'Dystrybuanta statystyki $U_{max}$')
    plt.legend()
    plt.show()

    plt.hist(u_max, density=True)
    plt.plot(a, b, label='teoretyczna')
    plt.title(r'Gęstość statystyki $U_{max}$')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
