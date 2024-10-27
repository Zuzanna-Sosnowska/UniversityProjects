import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def arcsin_dist(n=1000):
    x = np.linspace(0, 1, n)
    y = 2 / np.pi * np.arcsin(np.sqrt(x))
    return x, y


def arcsin_density(n=1000):
    x = np.linspace(0.005, 0.995, n)
    y = 1 / (np.pi * np.sqrt(x * (1 - x)))
    return x, y


def wiener1(n):
    times = np.sort(np.concatenate((np.random.uniform(0, 1, n - 2), np.array([0, 1]))))
    w = 0
    T = 0
    for i in range(n - 1):
        delta_w = np.random.normal(0, np.sqrt(times[i + 1] - times[i]))
        w += delta_w
        if w > 0:
            T += times[i + 1] - times[i]
    return T


def wiener2(n):
    times = np.sort(np.concatenate((np.random.uniform(0, 1, n - 2), np.array([0, 1]))))
    w = 0
    T = 0
    for i in range(n - 1):
        delta_w = np.random.normal(0, np.sqrt(times[i + 1] - times[i]))
        w_next = w + delta_w
        if w * w_next < 0:
            T = times[i] - w / ((w - w_next) / (times[i] - times[i + 1]))
        w = w_next
    return T


def wiener3(n):
    times = np.sort(np.concatenate((np.random.uniform(0, 1, n - 2), np.array([0, 1]))))
    w = 0
    max = 0
    t = 0
    for i in range(n - 1):
        delta_w = np.random.normal(0, np.sqrt(times[i + 1] - times[i]))
        w += delta_w
        if w > max:
            max = w
            t = times[i]
    return t


def wiener(n):
    times = np.sort(np.concatenate((np.random.uniform(0, 1, n - 2), np.array([0, 1]))))
    w = 0
    max = 0
    t1, t2, t3 = 0, 0, 0
    for i in range(n - 1):
        delta_w = np.random.normal(0, np.sqrt(times[i + 1] - times[i]))
        w_next = w + delta_w
        if w * w_next < 0:
            t2 = times[i] - w / ((w - w_next) / (times[i] - times[i + 1]))
        w = w_next
        if w > 0:
            t1 += times[i + 1] - times[i]
        if w > max:
            max = w
            t3 = times[i]
    return t1, t2, t3


def first_arcsin_law(m, n):
    return [wiener1(n) for _ in range(m)]


def second_arcsin_law(m, n):
    return [wiener2(n) for _ in range(m)]


def third_arcsin_law(m, n):
    return [wiener3(n) for _ in range(m)]


def arcsin_law(m, n):
    t1, t2, t3 = np.zeros(m), np.zeros(m), np.zeros(m)
    for i in range(m):
        t1[i], t2[i], t3[i] = wiener(n)
    return t1, t2, t3



if __name__ == '__main__':
    m = 10000
    n = 10000
    # t1 = first_arcsin_law(m=m, n=n)
    # t2 = second_arcsin_law(m=m, n=n)
    # t3 = third_arcsin_law(m=m, n=n)
    t1, t2, t3 = arcsin_law(m=m, n=n)

    plt.hist(t1, bins=30, density=True)
    plt.plot(*arcsin_density(), color='r')
    plt.title("Weryfikacja I prawa arcusa sinusa")
    plt.show()

    plt.hist(t2, bins=30, density=True)
    plt.plot(*arcsin_density(), color='r')
    plt.title("Weryfikacja II prawa arcusa sinusa")
    plt.show()

    plt.hist(t3, bins=30, density=True)
    plt.plot(*arcsin_density(), color='r')
    plt.title("Weryfikacja III prawa arcusa sinusa")
    plt.show()

    sns.ecdfplot(t1)
    plt.plot(*arcsin_dist(), color='r')
    plt.title("Porównanie dystrybuanty teoretycznej i empirycznej dla \n I prawa arcusa sinusa")
    plt.show()

    sns.ecdfplot(t2)
    plt.plot(*arcsin_dist(), color='r')
    plt.title("Porównanie dystrybuanty teoretycznej i empirycznej dla \n II prawa arcusa sinusa")
    plt.show()

    sns.ecdfplot(t3)
    plt.plot(*arcsin_dist(), color='r')
    plt.title("Porównanie dystrybuanty teoretycznej i empirycznej dla \n III prawa arcusa sinusa")
    plt.show()
