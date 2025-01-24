import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess
import numpy as np


def autokowariancja(x, h):
    n = len(x)
    x_m = np.mean(x)
    h = abs(h)
    if h >= n:
        raise ValueError("Opóźnienie h nie może być większe lub równe długości danych")
    return (1 / n) * np.sum((x[:n - h] - x_m) * (x[h:] - x_m))


def yule_walker_method(x, p):
    gamma_p = np.array([autokowariancja(x, h+1) for h in range(p)])
    gamma_p = gamma_p.transpose()
    G_p = np.array([[autokowariancja(x, i-j) for j in range(1, p+1)] for i in range(1, p+1)])
    phi = np.linalg.inv(G_p) @ gamma_p
    sigma2 = autokowariancja(x, 0) - phi.transpose() @ gamma_p
    return phi, sigma2


def estymator_NW(x):
    n = len(x)
    phi_est = np.sum(x[1:] * x[:-1]) / np.sum(np.power(x[:-1], 2))
    sigma2_est = 1 / n * np.sum(np.power(x[1:] - phi_est * x[:-1], 2))
    return phi_est, sigma2_est


def FPE(x, p):
    phi, sigma2 = yule_walker_method(x, p)
    n = len(x)
    return sigma2 * (n + p) / (n - p)


def main():
    n_lst = [50, 500, 1000]

    phi1 = 0.2
    phi2 = 0.4
    sigma2 = 1

    p_lst = np.arange(1, 11, 1)
    ar_process = ArmaProcess([1, -phi1, -phi2], [1])

    M = 100

    lst = []
    for n in n_lst:
        p_est_lst = []
        for i in range(M):
            sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
            fpe_lst = []
            for p in p_lst:
                fpe = FPE(sample, p)
                fpe_lst.append(fpe)
            p_est = np.argmin(fpe_lst)
            p_est_lst.append(p_est)
        lst.append(p_est_lst)

    lst1 = lst[0]
    lst2 = lst[1]
    lst3 = lst[2]

    x1 = np.zeros(len(p_lst))
    x2 = np.zeros(len(p_lst))
    x3 = np.zeros(len(p_lst))

    for i in range(len(p_lst)):
        x1[i] = lst1.count(i)
        x2[i] = lst2.count(i)
        x3[i] = lst3.count(i)

    plt.bar(p_lst, x1, color='green')
    plt.title('n=50')
    plt.show()

    plt.bar(p_lst, x2, color='blue')
    plt.title('n=500')
    plt.show()

    plt.bar(p_lst, x3, color='red')
    plt.title('n=1000')
    plt.show()


def part_2():
    n_lst = [50, 500, 1000]
    n = 2000
    phi1 = 0.2
    phi2 = 0.4
    sigma2 = 1

    ar_process = ArmaProcess([1, -phi1, -phi2], [1])
    p_lst = np.arange(1, 11, 1)
    M = 100

    fpe = np.zeros(len(p_lst))
    for i, p in enumerate(p_lst):
        sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
        fpe[i] = FPE(sample, p)
    p_est = np.argmin(fpe)

    phi, sigma2 = yule_walker_method(sample, p_est)
    ar_est_process = ArmaProcess([1] + [-phi_p for phi_p in phi], [1])

    N = 1000
    t_lst = np.arange(0, 1, 0.1)
    q_lst = np.zeros_like(t_lst)
    for i in range(N):
        est_sample = ar_est_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
        for j, t in enumerate(t_lst):
            q_lst[j] = np.quantile(est_sample, t)

    plt.plot(est_sample)
    for q in q_lst:
        plt.axhline(y=q, color='green')
    plt.show()


if __name__ == '__main__':
    part_2()
