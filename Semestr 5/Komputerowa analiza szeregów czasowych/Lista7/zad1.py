import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess


def yule_walker_method(x, p):
    gamma_p = np.array([autokowariancja(x, h+1) for h in range(p)])
    gamma_p = gamma_p.transpose()
    G_p = np.array([[autokowariancja(x, i-j) for j in range(1, p+1)] for i in range(1, p+1)])
    phi = np.linalg.inv(G_p) @ gamma_p
    sigma2 = autokowariancja(x, 0) - phi.transpose() @ gamma_p
    return phi, sigma2


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
    sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
    phi_est, sigma2_est = yule_walker_method(sample, 2)
    print(sigma2_est)

    M = 1000
    phi1_est_lst = np.zeros(M)
    phi2_est_lst = np.zeros(M)
    sigma2_est_lst = np.zeros(M)
    for i in range(M):
        sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
        phi_est, sigma2_est = yule_walker_method(sample, 2)
        phi1_est_lst[i] = phi_est[0]
        phi2_est_lst[i] = phi_est[1]
        sigma2_est_lst[i] = sigma2_est

    plt.boxplot([phi1_est_lst, phi2_est_lst], tick_labels=['phi 1', 'phi 2'])
    plt.show()


    plt.boxplot([sigma2_est_lst], tick_labels=['sigma 2'])
    plt.show()


if __name__ == '__main__':
    main()