import numpy as np
from scipy import stats


def median(x):
    x = np.sort(x)
    a = len(x)
    if a == 0:
        return None
    elif a % 2 == 1:
        return x[(a + 1) // 2 - 1]
    else:
        return (x[a // 2 - 1] + x[a // 2]) / 2


def quartile(x, n=2):
    x = np.sort(x)
    length = len(x)
    if n == 2:
        return median(x)
    elif n == 1:
        return median(x[:length // 2])
    elif n == 3:
        if length % 2 == 0:
            return median(x[length // 2:])
        else:
            return median(x[length // 2 + 1:])


def range_from_the_test(x):
    x = np.sort(x)
    return x[len(x)-1] - x[0]


def interquartile_range(x):
    return quartile(x, n=3) - quartile(x, n=1)


def arithmetic_average(x):
    return np.sum(x)/len(x)


def variance(x, ver=True):
    average = arithmetic_average(x)
    if ver:
        return np.sum(np.power(x - average, 2))/len(x)
    else:
        return np.sum(np.power(x - average, 2))/(len(x) - 1)


def standard_deviations(x):
    return np.sqrt(variance(x))


if __name__ == '__main__':

    x = np.random.normal(loc=2, scale=2, size=2000)
    print(f'mediana: {median(x)}, {np.median(x)}')

    print(f'drugi kwartyl: {quartile(x, 2)}, {np.quantile(x, 0.5, method='midpoint')}')

    print(f'pierwszy kwartyl: {quartile(x, 1)}, {np.quantile(x, 0.25, method='midpoint')}')
    print(f'trzeci kwartyl: {quartile(x, 3)}, {np.quantile(x, 0.75, method='midpoint')}')

    print(f'rozstęp z próby: {range_from_the_test(x)}, ----')

    print(f'rozstęp międzykwartylowy: {interquartile_range(x)}, {stats.iqr(x, interpolation='midpoint')}')

    print(f'wariancja: {variance(x, False)}, {np.var(x, ddof=1)}')

    print(f'odchylenie standardowe: {standard_deviations(x)}, {np.std(x, ddof=1)}')
