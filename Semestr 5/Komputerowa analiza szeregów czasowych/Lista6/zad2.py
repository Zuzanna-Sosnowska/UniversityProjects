import matplotlib.pyplot as plt
import numpy as np
import zad1


def main():
    N = 100
    phi = 0.2
    sigma2 = 0.4
    sigma = np.sqrt(sigma2)
    X0 = 0
    T = 1000
    h_max = 50
    h_lst = np.arange(0, h_max + 1, 1)
    autocov_lst = []
    autocor_lst = []

    for i in range(N):
        X = zad1.AR1(T, phi, 0, sigma)
        autocov = np.zeros(h_max+1)
        autocor = np.zeros(h_max+1)
        for j, h in enumerate(h_lst):
            autocov[j] = zad1.autocov(X, h)
            autocor[j] = zad1.autocor(X, h)
        autocov_lst.append(autocov)
        autocor_lst.append(autocor)

    q_005_autocov = []
    q_005_autocor = []
    q_095_autocov = []
    q_095_autocor = []
    theor_autocov = np.zeros(h_max+1)
    theor_autocor = np.zeros(h_max+1)
    for i in range(h_max+1):
        q_005_autocov.append(np.quantile([autocov_lst[j][i] for j in range(N)], 0.05))
        q_005_autocor.append(np.quantile([autocor_lst[j][i] for j in range(N)], 0.05))
        q_095_autocov.append(np.quantile([autocor_lst[j][i] for j in range(N)], 0.95))
        q_095_autocor.append(np.quantile([autocor_lst[j][i] for j in range(N)], 0.95))

        theor_autocov[i] = zad1.theor_autocov_AR1(h_lst[i], phi, sigma2)
        theor_autocor[i] = zad1.theor_autocor_AR1(phi, h_lst[i])

    plt.figure(figsize=(10, 6))
    plt.plot(h_lst, q_005_autocov, color='blue', label='przedziały ufności')
    plt.plot(h_lst, q_095_autocov, color='blue')
    plt.plot(h_lst, theor_autocov, color='red', label='teoretyczne wartości funkcji autokowariancji')
    plt.plot(h_lst, autocov, color='green', label='empiryczne wartości funkcji autokowariancji')
    plt.xlabel("Opóźnienie (h)")
    plt.ylabel("Autokowariancja")
    plt.title("Przedziały ufności dla autokowariancji")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(h_lst, q_095_autocor, color='blue', label='przedziały ufności')
    plt.plot(h_lst, q_005_autocor, color='blue')
    plt.plot(h_lst, theor_autocor, color='red', label='teoretyczne wartości funkcji autokorelacji')
    plt.plot(h_lst, autocor, color='green', label='empiryczne wartości funkcji autokorelacji')
    plt.xlabel("Opóźnienie (h)")
    plt.ylabel("Autokorelacja")
    plt.title("Przedziały ufności dla autokorelacji")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
