import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def calculate_b1_and_b0_estimator(x, y):
    b1 = np.sum((x - np.mean(x)) * y) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b1, b0


def variance_est(x, y, b0, b1):
    residuals = y - (b0 + b1 * x)
    return np.sum(np.power(residuals, 2)) / (len(x) - 2)


def SE_beta_0(x, var_residual):
    n = len(x)
    return np.sqrt(var_residual * (1 / n + (np.mean(x)) ** 2 / np.sum(np.power(x - np.mean(x), 2))))


def SE_beta_1(x, var_residual):
    return np.sqrt(var_residual / np.sum(np.power(x - np.mean(x), 2)))


def przedzialy_ufnosci_nieznana_wariancja(b0, b1, sigma_lst, n_lst, alpha, M):
    b0_list = []
    b1_list = []

    for sigma in sigma_lst:
        b0_lst = []
        b1_lst = []
        b0_przedzial_ufnosci_ze_znana_wariancja = []
        b1_przedzial_ufnosci_ze_znana_wariancja = []
        b0_przedzial_ufnosci_z_nieznana_wariancja = []
        b1_przedzial_ufnosci_z_nieznana_wariancja = []
        for n in n_lst:
            x = np.arange(1, n + 1, 1)
            counter_b0 = 0
            counter_b1 = 0
            for _ in range(M):
                e = np.random.normal(0, sigma, n)
                y = b0 + b1 * x + e

                b1_est, b0_est = calculate_b1_and_b0_estimator(x, y)
                norm_critical = stats.norm.ppf(1 - alpha / 2)
                c_b1 = (b1_est - norm_critical * sigma / np.sqrt(np.sum(np.power(x - np.mean(x), 2))),
                        b1_est + norm_critical * sigma / np.sqrt(np.sum(np.power(x - np.mean(x), 2))))
                c_b0 = (b0_est - norm_critical * sigma * np.sqrt(1 / len(x) + np.power(np.mean(x), 2) / np.sum(np.power(x - np.mean(x), 2))),
                        b0_est + norm_critical * sigma * np.sqrt(1 / len(x) + np.power(np.mean(x), 2) / np.sum(np.power(x - np.mean(x), 2))))

                var_residual = variance_est(x, y, b0_est, b1_est)
                se_b0 = SE_beta_0(x, var_residual)
                se_b1 = SE_beta_1(x, var_residual)

                t_critical = stats.t.ppf(1 - alpha / 2, n - 2)
                ci_b0 = (b0_est - t_critical * se_b0, b0_est + t_critical * se_b0)
                ci_b1 = (b1_est - t_critical * se_b1, b1_est + t_critical * se_b1)

                if ci_b0[0] <= b0 <= ci_b0[1]:
                    counter_b0 += 1
                if ci_b1[0] <= b1 <= ci_b1[1]:
                    counter_b1 += 1

            b0_lst.append(counter_b0 / M)
            b1_lst.append(counter_b1 / M)

            b0_przedzial_ufnosci_ze_znana_wariancja.append(c_b0[1] - c_b0[0])
            b1_przedzial_ufnosci_ze_znana_wariancja.append(c_b1[1] - c_b1[0])
            b0_przedzial_ufnosci_z_nieznana_wariancja.append(ci_b0[1] - ci_b0[0])
            b1_przedzial_ufnosci_z_nieznana_wariancja.append(ci_b1[1] - ci_b1[0])


        b0_list.append(b0_lst)
        b1_list.append(b1_lst)


    for idx, list in enumerate(b0_list):
        plt.plot(n_lst, list, marker='o', label=f'σ = {sigma_lst[idx]}')
    plt.axhline(1 - alpha, color='red', linestyle='--', label='1-α')
    plt.title(f'Pokrycie dla β₀ przy nieznanej wariancji (α = {alpha})')
    plt.xlabel('Liczba obserwacji (n)')
    plt.ylabel('Pokrycie')
    plt.yticks(np.linspace(0.7, 1.1, 12))
    plt.legend()
    plt.grid()
    plt.show()

    for idx, list in enumerate(b1_list):
        plt.plot(n_lst, list, marker='o', label=f'σ = {sigma_lst[idx]}')
    plt.axhline(1 - alpha, color='red', linestyle='--', label='1-α')
    plt.title(f'Pokrycie dla β₁ przy nieznanej wariancji (α = {alpha})')
    plt.xlabel('Liczba obserwacji (n)')
    plt.ylabel('Pokrycie')
    plt.yticks(np.linspace(0.7, 1.1, 12))
    plt.legend()
    plt.grid()
    plt.show()

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    # Wykres dla β₀
    ax[0].plot(n_lst, b0_przedzial_ufnosci_ze_znana_wariancja, label='Znana wariancja', marker='o')
    ax[0].plot(n_lst, b0_przedzial_ufnosci_z_nieznana_wariancja, label='Nieznana wariancja', marker='o')
    ax[0].set_title(f'Długość przedziału ufności dla parametru β₀ (α = {alpha})')
    ax[0].set_xlabel('n (liczba obserwacji)')
    ax[0].set_ylabel('Długość przedziału ufności')
    ax[0].legend()
    ax[0].grid(True, linestyle='--', alpha=0.7)

    # Wykres dla β₁
    ax[1].plot(n_lst, b1_przedzial_ufnosci_ze_znana_wariancja, label='Znana wariancja', marker='o')
    ax[1].plot(n_lst, b1_przedzial_ufnosci_z_nieznana_wariancja, label='Nieznana wariancja', marker='o')
    ax[1].set_title(f'Długość przedziału ufności dla parametru β₁ (α = {alpha})')
    ax[1].set_xlabel('n (liczba obserwacji)')
    ax[1].set_ylabel('Długość przedziału ufności')
    ax[1].legend()
    ax[1].grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


def main():
    beta_0 = 2
    beta_1 = 5
    sigma_values = [0.01, 0.5, 1]
    n_values = range(10, 101, 10)
    M = 1000
    alfa_lst = [0.01, 0.05]

    for alfa in alfa_lst:
        przedzialy_ufnosci_nieznana_wariancja(
            b0=beta_0, b1=beta_1, sigma_lst=sigma_values, n_lst=n_values, alpha=alfa, M=M
        )


if __name__ == "__main__":
    main()

