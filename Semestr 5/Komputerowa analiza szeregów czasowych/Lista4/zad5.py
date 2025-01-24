import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from zad4 import MA, autocov, autocor, theor_MA_autocov, theor_MA_autocor


def quadrant_autocov(x, h):
    n = len(x)
    if h >= n:
        raise ValueError("Przesunięcie h musi być mniejsze od długości danych.")
    x_m = np.median(x)
    total = 0
    for i in range(n - h):
        total += np.sign((x[i] - x_m) * (x[i + h] - x_m))
    return total / (n - h)


def quadrant_autocor(x, h):
    return np.sin(0.5 * np.pi * quadrant_autocov(x, h))


def main():
    n = 5000
    sigma = 1
    theta = 2
    p = 0.1
    a = 20
    b = 10
    e = 0
    x = MA(n=n, a=theta, loc=0, scale=sigma)
    ksi = np.random.choice([a, -a, 0], p=[p/2, p/2, 1-p], size=n)
    y = x + ksi
    h_lst = np.arange(0, b, 1)

    teor = np.array([theor_MA_autocor(h=h, sigma=sigma, a=theta) for h in h_lst])
    q_estx = np.array([quadrant_autocor(x=x, h=h) for h in h_lst])
    q_esty = np.array([quadrant_autocor(x=y, h=h) for h in h_lst])
    autokorx = np.array([autocor(x=x, h=h) for h in h_lst])
    autokory = np.array([autocor(x=y, h=h) for h in h_lst])


    plt.plot(x)
    plt.show()

    plt.plot(y)
    plt.show()

    plot1(teor, q_estx, q_esty, autokorx, autokory, h_lst)


def main2():
    n = 1000
    m = 100
    sigma = 1
    theta = 2
    b = 10
    h = 1
    p_lst = np.arange(0.01, 0.16, 0.01)
    a_lst = np.arange(1, 11, 1)
    e1_lst = []
    e2_lst = []
    for a in a_lst:
        e1_l = []
        e2_l = []
        for p in p_lst:
            e1 = 0
            e2 = 0
            for i in range(m):
                x = MA(n=n, a=theta, loc=0, scale=sigma)
                ksi = np.random.choice([a, -a, 0], p=[p / 2, p / 2, 1 - p], size=n)
                y = x + ksi
                e1 += np.abs(theor_MA_autocor(h=h, sigma=sigma, a=theta) - autocor(x=y, h=h))
                e2 += np.abs(theor_MA_autocor(h=h, sigma=sigma, a=theta) - quadrant_autocor(x=y, h=h))
            e1_l.append(e1/m)
            e2_l.append(e2/m)
        e1_lst.append(e1_l)
        e2_lst.append(e2_l)

    fig, axs = plt.subplots(ncols=2, figsize=(16, 10))

    for i, data in enumerate([e1_lst, e2_lst]):
        sns.heatmap(
            data,
            ax=axs[i],
            cbar=True,
            vmin=0,
            vmax=0.3,
        )

    plt.show()


def plot1(teor, q_estx, q_esty, autokorx, autokory, h_lst):
    plt.scatter(h_lst, teor, color='blue', label='teor')
    plt.plot(h_lst, q_estx, color='red', label='q-estimator')
    plt.plot(h_lst, autokorx, color='green', label='autocor')
    plt.legend()
    plt.grid(True)
    plt.title("Funkcja autokorelacji dla MA(1) (bez dodatkowego szumu)")
    plt.show()

    plt.scatter(h_lst, teor, color='blue', label='teor')
    plt.plot(h_lst, q_esty, color='red', label='q-estimator')
    plt.plot(h_lst, autokory, color='green', label='autocor')
    plt.legend()
    plt.grid(True)
    plt.title("Funkcja autokorelacji dla MA(1) z dodatkowym szumem")
    plt.show()


if __name__ == '__main__':
    main2()
