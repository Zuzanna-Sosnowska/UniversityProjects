import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess


def autocov(phi1, phi2, sigma2, k):
    if k == 1:
        return phi1 * sigma2/ (1 - phi2 - phi1 ** 2 - phi1 ** 2 * phi2 - phi2 ** 2 * (1 - phi2))
    if k == 0:
        return sigma2 * (1 - phi2) / (1 - phi2 - phi1 ** 2 - phi1 ** 2 * phi2 - phi2 ** 2 * (1 - phi2))
    if k >= 2:
        return phi1 * autocov(phi1, phi2, sigma2, k-1) + phi2 * autocov(phi2, phi1, sigma2, k-2)


def autokowariancja(x, h):
    n = len(x)
    x_m = np.mean(x)
    h = abs(h)
    if h >= n:
        raise ValueError("Opóźnienie h nie może być większe lub równe długości danych")
    return (1 / n) * np.sum((x[:n - h] - x_m) * (x[h:] - x_m))


def main():
    n = 1000
    ar = np.array([1, -0.2, -0.4])
    ma = np.array([1])
    sigma2 = 0.5
    n = 1000

    ar_process = ArmaProcess(ar, ma)

    k_lst = np.arange(0, 21, 1)

    sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
    ac1 = [autocov(0.2, 0.4, sigma2, k) for k in k_lst]
    ac2 = [autokowariancja(sample, k) for k in k_lst]

    plt.plot(k_lst, ac1, label='obliczona ze wzoru')
    plt.plot(k_lst, ac2, label='obliczone dla próby')
    plt.legend()
    plt.grid(True)
    plt.show()

    # M = 1000
    # autocov1 = []
    # autocov2 = []

    # for i in range(M):
    #     sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
    #     ac1 = [autocov(0.2, 0.4, sigma2, k) for k in k_lst]
    #     ac2 = [autokowariancja(sample, k) for k in k_lst]
    #     autocov1.append(ac1)
    #     autocov2.append(ac2)


if __name__ == '__main__':
    main()
