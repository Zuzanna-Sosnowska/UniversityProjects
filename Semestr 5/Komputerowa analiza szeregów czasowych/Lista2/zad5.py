import numpy as np
import matplotlib.pyplot as plt


def calculate_b1_and_b0_estimator(x, y):
    b1 = np.sum((x - np.mean(x)) * y) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b1, b0


def wyznaczanie_punktu_zmiany_rezimu(x):
    n = len(x)
    c = np.zeros(n)
    val = 0
    for i in range(n):
        val += np.power(x[i], 2)
        c[i] = val
    v = np.zeros(n-3)
    for k in range(2, n-1):
        stat_1 = c[:k]
        stat_2 = c[k:]
        a1 = np.arange(1, k+1, 1)
        a2 = np.arange(k+1, n+1, 1)
        b1_est_stat_1, b0_est_stat_1 = calculate_b1_and_b0_estimator(a1, stat_1)
        b1_est_stat_2, b0_est_stat_2 = calculate_b1_and_b0_estimator(a2, stat_2)
        v[k-2] = (np.sum(np.power(stat_1 - (b0_est_stat_1 + b1_est_stat_1 * a1), 2)) +
                  np.sum(np.power(stat_2 - (b0_est_stat_2 + b1_est_stat_2 * a2), 2)))
    return v


def plots():
    N = 1000
    L = 400
    sigma1 = 1
    sigma2 = 5
    x1 = np.random.normal(0, sigma1, L)
    x2 = np.random.normal(0, sigma2, N - L)
    x = np.array([*x1, *x2])

    v = wyznaczanie_punktu_zmiany_rezimu(x)
    L_emp = np.argmin(v)
    print(L_emp)

    plt.plot(x)
    plt.title(r"Wykres dla danych z rozkładu normalnego z $\sigma_{1}^2 = 1$ i $\sigma_{2}^2 = 5$")
    plt.axvline(L, color='red', label="Ustalony punkt zmiany reżimu")
    plt.axvline(L_emp, color='yellow', label="Punkt zmiany reżimu wyznaczony z wykorzystaniem prostej MNK")
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

    c = np.zeros(N)
    val = 0
    for j in range(N):
        val += np.power(x[j], 2)
        c[j] = val

    plt.plot(c)
    plt.title(r"Wykres statystyki $C_j$")
    plt.axvline(L_emp, color='yellow')
    plt.axvline(L, color='red')
    plt.grid(True)
    plt.show()

    plt.plot(v)
    plt.title(r"Wykres wyznaczonego błędu $V(k)$")
    plt.axvline(L_emp, color='yellow')
    plt.axvline(L, color='red')
    plt.grid(True)
    plt.show()


def boxplots(L):
    M = 100
    N = 1000
    sigma_lst = [1.5, 2, 2.5, 3, 5]
    sigma1 = 1
    x1 = np.random.normal(0, sigma1, L)
    data = {}
    for sigma2 in sigma_lst:
        k_lst = np.zeros(M)
        for i in range(M):
            x2 = np.random.normal(0, sigma2, N - L)
            x = np.array([*x1, *x2])
            k = np.argmin(wyznaczanie_punktu_zmiany_rezimu(x))
            k_lst[i] = k
        data[sigma2] = k_lst

    fig, ax = plt.subplots()
    ax.boxplot(data.values())
    ax.set_xticklabels(data.keys())
    plt.show()


def main():
    plots()

    # boxplots(L=400)
    # boxplots(L=50)

if __name__ == '__main__':
    main()
