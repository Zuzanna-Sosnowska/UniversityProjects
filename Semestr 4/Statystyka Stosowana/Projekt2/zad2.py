import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy


def get_data(file):
    my_file = open(file, "r")
    data = my_file.read()

    data = data.replace(' ', '')
    data = data.split('\n')
    data = np.array([float(i) for i in data])
    return data


def arithmetical_mean(data):
    n = len(data)
    return sum(data) / n


def variance(data):
    n = len(data)
    return 1/(n-1) * np.sum(np.power(data - arithmetical_mean(data), 2))


def test_statistic(data, var):
    n = len(data)
    return (n-1) * variance(data) / var


def chi2_density(k, n=1000):
    x = np.linspace(0.85*k, 1.15*k, n)
    y = scipy.stats.chi2.pdf(x, k)
    return x, y


def chi2_dist_val(x, k):
    return scipy.stats.chi2.cdf(x, k)


def chi2_quantile(alpha, k):
    return scipy.stats.chi2.ppf(alpha, k)


def plot1(n, alpha):
    q1 = chi2_quantile(1 - alpha / 2, n - 1)
    q2 = chi2_quantile(alpha / 2, n - 1)
    x, y = chi2_density(n - 1)
    c1 = np.linspace(0.85 * n, q2, n)
    c2 = np.linspace(q1, 1.15 * n, n)
    plt.figure(figsize=(9, 7))
    plt.plot(x, y)
    plt.fill_between(c1, scipy.stats.chi2.pdf(c1, n-1), color='paleturquoise', label='obszar krytyczny')
    plt.fill_between(c2, scipy.stats.chi2.pdf(c2, n - 1), color='paleturquoise')
    plt.axvline(x=q1, color='teal', linestyle='--', label=r'$\chi^2_{1-\frac{\alpha}{2}, n-1} = $' + f'{q1}')
    plt.axvline(x=q2, color='orange', linestyle='--', label=r'$\chi^2_{\frac{\alpha}{2}, n-1} = $' + f'{q2}')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.title(r'Rozkład $\chi^2$ z $n-1$ stopniami swobody, $\alpha$ = ' + f'{alpha}' + '\n', fontsize=18, ha='center')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('zbior_krytyczny_a2')
    plt.show()


def plot2(n, alpha):
    q3 = chi2_quantile(alpha, n - 1)
    c3 = np.linspace(0.85 * n, q3, n)
    x, y = chi2_density(n - 1)
    plt.figure(figsize=(9, 7))
    plt.plot(x, y)
    plt.fill_between(c3, scipy.stats.chi2.pdf(c3, n - 1), color='lightcoral', label='Obszar krytyczny')
    plt.axvline(q3, color='red', linestyle='dashed', label=r'$\chi^2_{\alpha, n-1} = $' + f'{q3}')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.title(r'Rozkład $\chi^2$ z $n-1$ stopniami swobody' + '\n', fontsize=18, ha='center')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('zbior_krytyczny_2')
    plt.show()


def plot3(n, alpha):
    q4 = chi2_quantile(1 - alpha, n - 1)

    x, y = chi2_density(n - 1)
    c4 = np.linspace(q4, 1.15 * n, n)

    plt.figure(figsize=(9, 7))
    plt.plot(x, y)
    plt.fill_between(c4, scipy.stats.chi2.pdf(c4, n - 1), color='moccasin', label='Obszar krytyczny')
    plt.axvline(x=q4, color='orange', linestyle='--', label=r'$\chi^2_{1-\alpha, n-1} = $' + f'{q4}')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.title(r'Rozkład $\chi^2$ z $n-1$ stopniami swobody' + '\n', fontsize=18, ha='center')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('zbior_krytyczny_3')
    plt.show()


def first(n, m, mean, st_dev, alpha, ver=1):
    c = 0
    if ver == 1:
        for _ in range(m):
            x = np.random.normal(loc=mean, scale=st_dev, size=n)
            z = test_statistic(x, st_dev**2)
            if z >= chi2_quantile(1-alpha/2, n-1) or z <= chi2_quantile(alpha/2, n-1):
                c += 1
        return c / m
    if ver == 2:
        for _ in range(m):
            x = np.random.normal(loc=mean, scale=st_dev, size=n)
            z = test_statistic(x, st_dev**2)
            if z >= chi2_quantile(1-alpha, n-1):
                c += 1
        return c / m
    if ver == 3:
        for _ in range(m):
            x = np.random.normal(loc=mean, scale=st_dev, size=n)
            z = test_statistic(x, st_dev**2)
            if z <= chi2_quantile(alpha, n-1):
                c += 1
        return c / m


def second(n, m, mean, var, alpha, df, ver=1):
    c = 0
    if ver == 1:
        for _ in range(m):
            x = np.random.normal(loc=mean, scale=np.sqrt(var+df), size=n)
            z = test_statistic(x, var)
            if chi2_quantile(alpha/2, n-1) <= z <= chi2_quantile(1-alpha/2, n-1):
                c += 1
        return c / m
    if ver == 2:
        for _ in range(m):
            x = np.random.normal(loc=mean, scale=np.sqrt(var+df), size=n)
            z = test_statistic(x, var)
            if z <= chi2_quantile(1-alpha, n-1):
                c += 1
        return c / m
    if ver == 3:
        for _ in range(m):
            x = np.random.normal(loc=mean, scale=np.sqrt(var+df), size=n)
            z = test_statistic(x, var)
            if z >= chi2_quantile(alpha, n-1):
                c += 1
        return c / m


def main():
    var = 1.5
    alpha = 0.01

    plot1(1000, alpha)


if __name__ == '__main__':
    main()
