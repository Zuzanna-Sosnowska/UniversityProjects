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


def main():
    n_lst = [100 * i for i in range(1, 11)]
    phi = 0.1
    sigma2 = 0.5
    ar = np.array([1, -phi])
    ma = np.array([1])

    m = 100

    phi_yw_boxplots = []
    phi_nw_boxplots = []
    sigma2_yw_boxplots = []
    sigma2_nw_boxplots = []
    for n in n_lst:
        phi_yw_lst = np.zeros(m)
        phi_nw_lst = np.zeros(m)
        sigma2_yw_lst = np.zeros(m)
        sigma2_nw_lst = np.zeros(m)
        for i in range(m):
            ar_process = ArmaProcess(ar, ma)
            sample = ar_process.generate_sample(nsample=n, scale=np.sqrt(sigma2))
            phi_yw_lst[i], sigma2_yw_lst[i] = yule_walker_method(sample, 1)
            phi_nw_lst[i], sigma2_nw_lst[i] = estymator_NW(sample)
        phi_yw_boxplots.append(phi_yw_lst)
        phi_nw_boxplots.append(phi_nw_lst)
        sigma2_yw_boxplots.append(sigma2_yw_lst)
        sigma2_nw_boxplots.append(sigma2_nw_lst)

    # plt.boxplot(phi_nw_boxplots, labels=n_lst)
    # plt.boxplot(phi_yw_boxplots, labels=n_lst)
    # plt.show()
    #
    # plt.boxplot(sigma2_nw_boxplots, labels=n_lst)
    # plt.boxplot(sigma2_yw_boxplots, labels=n_lst)
    # plt.show()

    # Plot phi boxplots obok siebie
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
    ax[0].boxplot(phi_nw_boxplots, labels=n_lst, patch_artist=True,
                  boxprops=dict(facecolor='blue', color='blue'), medianprops=dict(color='black'))
    ax[0].set_title("phi_nw_boxplots (Blue)")
    ax[1].boxplot(phi_yw_boxplots, labels=n_lst, patch_artist=True,
                  boxprops=dict(facecolor='red', color='red'), medianprops=dict(color='black'))
    ax[1].set_title("phi_yw_boxplots (Red)")
    for a in ax:
        a.set_xlabel("Sample size (n)")
        a.set_ylabel("Phi")
    plt.tight_layout()
    plt.show()

    # Plot sigma^2 boxplots obok siebie
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
    ax[0].boxplot(sigma2_nw_boxplots, labels=n_lst, patch_artist=True,
                  boxprops=dict(facecolor='blue', color='blue'), medianprops=dict(color='black'))
    ax[0].set_title("sigma2_nw_boxplots (Blue)")
    ax[1].boxplot(sigma2_yw_boxplots, labels=n_lst, patch_artist=True,
                  boxprops=dict(facecolor='red', color='red'), medianprops=dict(color='black'))
    ax[1].set_title("sigma2_yw_boxplots (Red)")
    for a in ax:
        a.set_xlabel("Sample size (n)")
        a.set_ylabel("Sigma^2")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
