from math import gcd as gcd
import matplotlib.pyplot as plt
import time
import numpy as np


def coprime(a, b):
    return gcd(a, b) == 1


def find_coprime(a):
    if a == 1:
        raise "Number must be grater than 2"
    for i in range(int(np.power(a, 0.5)), a):
        if coprime(a, i):
            return i
    return None


def ACORN(N, k, M, Lag):
    N += Lag
    a = find_coprime(M)
    seed = [a for i in range(k)]
    x = [seed[0] for _ in range(N)]
    for i in range(k):
        x[0] = (seed[i] + x[0]) % M
        for j in range(1, N):
            x[j] = (x[j - 1] + x[j]) % M
    return [x[i] / M for i in range(Lag, N)]


if __name__ == '__main__':
    N = 1000
    k = 9
    M = 2 ** 89 - 1
    Lag = 10 ** 3

    x1 = ACORN(N=N, k=k - 1, M=M, Lag=Lag)
    x2 = ACORN(N=N, k=k, M=M, Lag=Lag)
    x = ACORN(N=10 * N, k=k, M=M, Lag=Lag)

    plt.scatter(x1, x2)
    plt.title(r"Wykres ciągu $Y_n^{k-1} \rightarrow Y_n^k$", fontsize=20, pad=25)
    plt.xlabel(r"$Y_n^{k-1}$")
    plt.ylabel(r"$Y_n^k$")
    plt.grid(True)
    plt.show()

    plt.hist(x, density=True)
    plt.axhline(y=1, color='r')
    plt.title(rf"Unormowany histogram dla ciągu $Y_n^k$ z parametrem k={k}, N={N}", fontsize=16, pad=25)
    plt.xlabel("Wartości")
    plt.ylabel("Prawdopodobieństwo uzyskania wartości")
    plt.grid(True)
    plt.show()


