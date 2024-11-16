import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


def calculate_b1_and_b0_estimator(x, y):
    b1 = np.sum((x - np.mean(x)) * y) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b1, b0


def przedzialy_ufnosci(alfa):
    sigma_lst = [0.01, 0.5, 1]
    N = [10 * i for i in range(1, 11)]
    M = 1000
    b0 = 2
    b1 = 5
    b0_list = []
    b1_list = []
    for sigma in sigma_lst:
        b0_lst = []
        b1_lst = []
        for n in N:
            x = np.arange(1, n + 1, 1)
            counter_b0 = 0
            counter_b1 = 0
            for j in range(M):
                e = np.random.normal(0, sigma, n)
                y = b0 + b1 * x + e
                b1_est, b0_est = calculate_b1_and_b0_estimator(x, y)
                if b1_est - stats.norm.ppf(1 - alfa / 2) * sigma / np.sqrt(
                        np.sum(np.power(x - np.mean(x), 2))) < b1 < b1_est + stats.norm.ppf(
                        1 - alfa / 2) * sigma / np.sqrt(np.sum(np.power(x - np.mean(x), 2))):
                    counter_b1 += 1
                if b0_est - stats.norm.ppf(1 - alfa / 2) * sigma * np.sqrt(
                        1 / len(x) + np.power(np.mean(x), 2) / np.sum(
                                np.power(x - np.mean(x), 2))) < b0 < b0_est + stats.norm.ppf(
                        1 - alfa / 2) * sigma * np.sqrt(
                        1 / len(x) + np.power(np.mean(x), 2) / np.sum(np.power(x - np.mean(x), 2))):
                    counter_b0 += 1
            b0_lst.append(counter_b0 / M)
            b1_lst.append(counter_b1 / M)
        b0_list.append(b0_lst)
        b1_list.append(b1_lst)

    c = 0
    for list in b0_list:
        plt.plot(np.arange(1, len(list) + 1, 1), list, label=str(sigma_lst[c]))
        c += 1
    plt.show()

    c = 0
    for list in b1_list:
        plt.plot(np.arange(1, len(list) + 1, 1), list, label=str(sigma_lst[c]))
        c += 1
    plt.show()


def main():
    alfa_lst = [0.01, 0.05]
    przedzialy_ufnosci(alfa_lst[0])
    przedzialy_ufnosci(alfa_lst[1])


if __name__ == "__main__":
    main()
