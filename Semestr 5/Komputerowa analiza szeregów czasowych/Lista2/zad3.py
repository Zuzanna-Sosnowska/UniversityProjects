import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


def calculate_b1_and_b0_estimator(x, y):
    b1 = np.sum((x - np.mean(x)) * y) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b1, b0


def generate_b1_and_b0_est(n, x, miu, sigma, b0, b1):
    b1_est = np.zeros(n)
    b0_est = np.zeros(n)
    for j in range(n):
        e = np.random.normal(miu, sigma, n)
        y = b0 + b1 * x + e
        b1_est[j], b0_est[j] = calculate_b1_and_b0_estimator(x=x, y=y)
    return b1_est, b0_est


def normal_density_plot(miu, sigma, n):
    x = np.linspace(miu - 4*sigma, miu + 4*sigma, n)
    y = (1 / (np.sqrt(2*np.pi)*sigma)) * np.exp(-(x - miu)**2/(2*sigma**2))
    return x, y


def main():
    n = 1000
    miu = 0
    sigma = 2
    b1 = 5
    b0 = 2
    x = np.linspace(0, 10, n)
    b1_emp_dist, b0_emp_dist = generate_b1_and_b0_est(n, x, miu, sigma, b0, b1)
    theor_var_b1 = sigma ** 2 / np.sum(np.power(x - np.mean(x), 2))
    theor_var_b0 = sigma ** 2 * (1/n + np.mean(np.power(x, 2)) / np.sum(np.power(x - np.mean(x), 2)))
    b1_stdev = np.sqrt(theor_var_b1)
    b0_stdev = np.sqrt(theor_var_b0)

    plt.hist(b0_emp_dist, density=True)
    plt.plot(*normal_density_plot(b0, b0_stdev, n), color='r')
    plt.title('Porównanie histogramu z teoretyczną gęstością \n dla rozkładu estymatora b0')
    plt.show()

    x_b0 = np.linspace(b0-4*b0_stdev, b0+4*b0_stdev, n)
    y_b0 = stats.norm.cdf(x_b0, b0, b0_stdev)

    sns.ecdfplot(b0_emp_dist)
    plt.plot(x_b0, y_b0, color='r')
    plt.title('Porównanie dystrybuanty teoretycznej dla \n rozkładu estymatora b0')
    plt.show()

    plt.hist(b1_emp_dist, density=True)
    plt.plot(*normal_density_plot(b1, b1_stdev, n), color='r')
    plt.title('Porównanie histogramu z teoretyczną gęstością \n dla rozkładu estymatora b1')
    plt.show()

    x_b1 = np.linspace(b1 - 4 * b1_stdev, b1 + 4 * b1_stdev, n)
    y_b1 = stats.norm.cdf(x_b1, b1, b1_stdev)

    sns.ecdfplot(b1_emp_dist)
    plt.plot(x_b1, y_b1, color='r')
    plt.title('Porównanie dystrybuanty teoretycznej dla \n rozkładu estymatora b1')
    plt.show()

    print('Test Kołmogorowa-Smirnowa dla b0:', stats.kstest(b0_emp_dist, 'norm', args=(b0, b0_stdev)))
    print('Test Kołmogorowa-Smirnowa dla b1:', stats.kstest(b1_emp_dist, 'norm', args=(b1, b1_stdev)))


if __name__ == '__main__':
    main()
