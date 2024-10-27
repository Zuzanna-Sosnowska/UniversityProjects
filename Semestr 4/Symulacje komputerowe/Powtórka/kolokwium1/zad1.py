import numpy as np
import matplotlib.pyplot as plt


def p(x):
    return 1 / (x * (x + 1))


def f_distribution(n=1000):
    u = np.random.uniform(0, 1, n)
    return np.ceil(u/(1-u))


def main():
    n = 10 ** 4
    a = f_distribution(n)
    b = [i for i in a if i <= 20]
    x = np.linspace(1.1, 20, 20)
    y = p(x)

    plt.hist(b, density=True)
    plt.plot(x, y, color='r')
    plt.show()


if __name__ == '__main__':
    main()
