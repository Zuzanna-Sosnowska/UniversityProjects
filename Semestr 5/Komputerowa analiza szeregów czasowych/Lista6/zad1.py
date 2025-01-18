import numpy as np
import matplotlib.pyplot as plt


def AR1(n, phi, loc=0.0, scale=1.0):
    Z = np.random.normal(loc=loc, scale=scale, size=n)
    X = np.zeros(n)
    for t in range(1, n):
        X[t] = phi * X[t-1] + Z[t]
    return X


def theor_autocov_AR1(h, phi, sigma2):
    return (sigma2 / (1 - phi**2)) * (phi**abs(h))


def theor_autocor_AR1(phi, h):
    return np.power(phi, abs(h))


def autocov(x, h):
    n = len(x)
    x_m = np.mean(x)
    h = abs(h)
    return (1 / n) * np.sum((x[:n - h] - x_m) * (x[h:] - x_m))


def autocor(x, h):
    return autocov(x, h) / autocov(x, 0)


def main():
    phi = 0.2
    sigma2 = 0.4
    X0 = 0
    T = 1000
    X = AR1(T, phi, loc=0, scale=np.sqrt(sigma2))

    max_lag = 50
    lags = np.arange(max_lag + 1)
    acf_theoretical = theor_autocov_AR1(lags, phi, sigma2)
    acc_theoretical = theor_autocor_AR1(phi, lags)
    acf_emp = np.zeros(len(lags))
    acc_emp = np.zeros(len(lags))
    for i, h in enumerate(lags):
        acf_emp[i] = autocov(X, h)
        acc_emp[i] = autocor(X, h)


    # Wizualizacja wyników
    plt.figure(figsize=(10, 6))
    plt.plot(lags, acf_emp, label="Empiryczna ACF", marker='o')
    plt.plot(lags, acf_theoretical, label="Teoretyczna ACF", marker='o')
    plt.xlabel("Opóźnienie (h)")
    plt.ylabel("Autokowariancja")
    plt.title("Porównanie empirycznej i teoretycznej funkcji autokowariancji")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(lags, acc_emp, label="Empiryczna", marker='o')
    plt.plot(lags, acc_theoretical, label="Teoretyczna", marker='o')
    plt.xlabel("Opóźnienie (h)")
    plt.ylabel("Autokorelacja")
    plt.title("Porównanie empirycznej i teoretycznej funkcji autokorelacji")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
