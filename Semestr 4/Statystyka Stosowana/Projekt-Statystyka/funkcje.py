import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


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


def arithmetic_mean(x):
    return np.sum(x)/len(x)


def geometric_mean(data):
    return np.exp(np.log(data).mean())


def harmonic_mean(data):
    return len(data)/(np.sum(1/data))


def cut_mean(data, k):
    data = np.sort(data)
    return 1/(len(data)-2*k) * np.sum(data[k:len(data)-k])


def windsor_mean(data, k):
    n = len(data)
    data = np.sort(data)
    return (1/n) * ((k+1)*data[k] + np.sum(data[k+1:n-k-1]) + (k+1)*data[n-k-1])


def variance(x, ver=True):
    average = arithmetic_mean(x)
    if ver:
        return np.sum(np.power(x - average, 2))/len(x)
    else:
        return np.sum(np.power(x - average, 2))/(len(x) - 1)


def standard_deviations(x, ver=True):
    return np.sqrt(variance(x, ver))


def average_dev_mean(x):
    return 1/len(x) * np.sum(np.abs(x - arithmetic_mean(x)))


def coeff_of_variation(x, ver=True):
    return standard_deviations(x)/arithmetic_mean(x)


def skewness_coefficient(x, ver=True):
    n = len(x)
    u = arithmetic_mean(x)
    sigma = standard_deviations(x)
    if ver:
        return n/((n-1)*(n-2)) * np.sum(np.power((x - u)/sigma, 3))
    else:
        return (1/n * np.sum(np.power((x - u), 3)))/(np.power(1/n * np.sum(np.power((x - u), 2)), 1.5))


def kurtosis(x):
    n = len(x)
    u = arithmetic_mean(x)
    k1 = (1/n * np.sum(np.power(x-u, 4)))/np.power((1/n * np.sum(np.power(x-u, 2))), 2)
    return (n-1)/((n-2)*(n-3)) * ((n+1) * k1 -3 * (n-1)) + 3


def boxplot(data):
    plt.boxplot(data)
    plt.show()


if __name__ == '__main__':
    pass
    # dataset_1 = "EM2015.csv"
    # dataset_2 = "EM2023.csv"
    # x_1 = pd.read_csv(dataset_1, encoding='latin1', sep=';', low_memory=False,
    #                 header=0, skiprows=[1, 2], decimal=',')
    # x_2 = pd.read_csv(dataset_2, encoding='latin1', sep=';', low_memory=False,
    #                 header=0, skiprows=[1, 2], decimal=',')
    # x_1.columns = [i for i in range(1, len(x_1.columns) + 1)]
    # x_2.columns = [i for i in range(1, len(x_2.columns) + 1)]
    #
    # # średni wynik w poszczególnych szkołach  z matury - matematyka, poziom podstawowy, formuła 2015
    # a_1 = x_1[x_1[68].notnull() & x_1[71].notnull()].loc[:, 71].to_numpy()
    # # liczba zdających w poszczególnych szkołach w formule 2015
    # b_1 = x_1[x_1[68].notnull() & x_1[71].notnull()].loc[:, 68].to_numpy().astype(int)
    #
    # a_2 = x_2[x_2[88].notnull() & x_2[91].notnull()].loc[:, 91].to_numpy()
    # b_2 = x_2[x_2[88].notnull() & x_2[91].notnull()].loc[:, 88].to_numpy().astype(int)
    #
    # print(a_2)

    # print(median(a_1))
    # print(median(b_1))
    #
    # print(arithmetic_mean(a_1))
    # print(arithmetic_mean(b_1))
    #
    # print(median(a_2))
    # print(median(b_2))
    #
    # print(arithmetic_mean(a_2))
    # print(arithmetic_mean(b_2))
    #
    # sns.kdeplot(a_1, color='navy')
    # sns.kdeplot(a_2, color='orange')
    # plt.legend(['EM2015', 'EM2023'], loc='best')
    # plt.show()
