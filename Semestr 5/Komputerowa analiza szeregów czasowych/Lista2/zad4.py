import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


def calculate_b1_and_b0_estimator(x, y):
    b1 = np.sum((x - np.mean(x)) * y) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b1, b0


def var_estimator(y, y_r):
    s2 = 1 / (len(y) - 2) * np.sum(np.power(y - y_r, 2))
    return s2


def SE_b0(x, y, y_r):
    s = np.sqrt(var_estimator(y, y_r))
    return s * np.sqrt(1/len(x) + np.power(np.mean(x), 2) / np.sum(np.power(x - np.mean(x), 2)))


def SE_b1(x, y, y_r):
    s = np.sqrt(var_estimator(y, y_r))
    return s / np.sqrt(np.sum(np.power(x - np.mean(x), 2)))


def generate_w1_w0(n, x, miu, sigma, b0, b1):
    w1 = np.zeros(n)
    w2 = np.zeros(n)
    for j in range(n):
        e = np.random.normal(miu, sigma, n)
        y = b0 + b1 * x + e
        y_r = b0 + b1 * x
        b1_est, b0_est = calculate_b1_and_b0_estimator(x=x, y=y)
        w1[j] = (b0_est - b0) / SE_b0(x, y, y_r)
        w2[j] = (b1_est - b1) / SE_b1(x, y, y_r)
    return w1, w2


def main():
    n = 1000
    miu = 0
    sigma = 2
    b1 = 5
    b0 = 2
    x = np.linspace(0, 10, n)
    w1, w2 = generate_w1_w0(n, x, miu, sigma, b0, b1)

    x = np.linspace(-3, 3, n)
    y_density = stats.t.pdf(x, df=n-2)
    y_distr = stats.t.cdf(x, df=n-2)

    plt.hist(w1, density=True)
    plt.plot(x, y_density, color='r')
    plt.title('Porównanie histogramu z teoretyczną gęstością dla rozkładu w1')
    plt.show()

    sns.ecdfplot(w1)
    plt.plot(x, y_distr, color='r')
    plt.title('Porównanie dystrybuanty teoretycznej dla \n rozkładu estymatora w1')
    plt.show()

    plt.hist(w2, density=True)
    plt.plot(x, y_density, color='r')
    plt.title('Porównanie histogramu z teoretyczną gęstością \n dla rozkładu estymatora w2')
    plt.show()

    sns.ecdfplot(w2)
    plt.plot(x, y_distr, color='r')
    plt.title('Porównanie dystrybuanty teoretycznej dla \n rozkładu estymatora w2')
    plt.show()

    print('Test Kołmogorowa-Smirnowa dla b0:', stats.kstest(w1, 't', args=(n-2, 0, 1)))
    print('Test Kołmogorowa-Smirnowa dla b1:', stats.kstest(w2, 't', args=(n-2, 0, 1)))


if __name__ == '__main__':
    main()
