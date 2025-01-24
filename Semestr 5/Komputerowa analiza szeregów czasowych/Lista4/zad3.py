import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 1000
    x = np.random.normal(loc=0,scale=2,size=n)
    h = np.arange(0, 11, 1)
    emp_autocov = np.zeros(len(h))
    emp_autocor = np.zeros(len(h))
    theor_autocor = np.zeros(len(h))
    theor_autocov = np.zeros(len(h))
    for i, j in enumerate(h):
        emp_autocov[i] = autokowariancja(x, j)
        emp_autocor[i] = autokorelacja(x, j)
        theor_autocor[i] = theoretical_autocor(j)
        theor_autocov[i] = theoretical_autocov(j)

    plt.plot(h,emp_autocov, color='magenta')
    plt.plot(h,theor_autocov)
    plt.title('Empiryczna wartość funkcji autokowariancji')
    plt.show()

    plt.plot(h,emp_autocor, color='magenta')
    plt.plot(h,theor_autocor)
    plt.title("Empiryczna wartość funkcji autokorelacji")
    plt.show()


def main2():
    M = 10
    n_lst = np.arange(10, 1001, 10)
    h = np.arange(0, 10, 1)
    e_lst = {j: j for j in np.arange(0, M, 1)}
    for j in range(M):
        e = np.zeros(len(n_lst))
        for i, n in enumerate(n_lst):
            x = np.random.normal(loc=0,scale=2,size=n)
            e[i] = error(x, h)
        e_lst[j] = e

    plt.scatter(n_lst, e)
    plt.show()

    # to jest źle
    fig, ax = plt.subplots()
    ax.boxplot(e_lst.values())
    ax.set_xticklabels(e_lst.keys())
    plt.show()


def autokowariancja(x, h):
    n = len(x)
    x_m = np.mean(x)
    h = abs(h)
    if h >= n:
        raise ValueError("Opóźnienie h nie może być większe lub równe długości danych")
    return (1 / n) * np.sum((x[:n - h] - x_m) * (x[h:] - x_m))


def autokorelacja(x, h):
    return autokowariancja(x, h) / autokowariancja(x, 0)


def theoretical_autocov(h):
    if h == 0:
        return 4
    return 0


def theoretical_autocor(h):
    if h == 0:
        return 1
    return 0


def error(x, h_lst):
    e = 0
    for h in h_lst:
        e += np.abs(autokowariancja(x, h) - theoretical_autocov(h))
    return e


if __name__ == '__main__':
    main2()
