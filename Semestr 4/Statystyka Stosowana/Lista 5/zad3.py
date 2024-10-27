import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def arithm_mean(x):
    n = len(x)
    return np.sum(x) / n


def alfa_estim(x):
    n = len(x)
    return (arithm_mean(x))**2 / (1/n * np.sum((x - arithm_mean(x))**2))


def beta_estim(x):
    n = len(x)
    return arithm_mean(x)/(1/n * np.sum((x - arithm_mean(x))**2))


if __name__ == '__main__':
    alfa = 4
    beta = 5
    n = 500
    N = 100
    M = 1000
    a = np.zeros(M)
    b = np.zeros(M)
    y = np.linspace(0, M, M)
    for j in range(M):
        alfa_est = np.zeros(N)
        beta_est = np.zeros(N)
        for i in range(N):
            x = np.random.gamma(size=n, shape=alfa, scale=1/beta)
            alfa_est[i] = alfa_estim(x)
            beta_est[i] = beta_estim(x)
        b[j] = 1/N * np.sum(beta_est - beta)
        a[j] = 1/N * np.sum(alfa_est - alfa)

    a_sr = arithm_mean(a)
    b_sr = arithm_mean(b)
    plt.plot(y, a)
    plt.title("Błąd alfa")
    plt.axhline(y=a_sr, color='r')
    plt.show()
    plt.plot(y, b)
    plt.title("Błąd beta")
    plt.axhline(y=b_sr, color='r')
    plt.show()

