import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gmean, hmean
import zad1


def arithmetic_mean(data):
    return np.sum(data)/len(data)


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


if __name__ == '__main__':
    df = pd.read_csv('HousePrices.csv')
    data = np.array(df.loc[:, "price"].astype(float))

    print(arithmetic_mean(data))
    print(np.mean(data))

    print(geometric_mean(data))
    print(gmean(data))

    print(harmonic_mean(data))
    print(hmean(data))

    x_list = [k for k in range(len(data)//2 - 1)]
    y1_list = [cut_mean(data, k) for k in range(len(data)//2 - 1)]
    y2_list = [windsor_mean(data, k) for k in range(len(data)//2 - 1)]

    plt.plot(x_list, y1_list)
    plt.axhline(y=arithmetic_mean(data), color='r', linestyle='-')
    plt.axhline(y=zad1.median(data), color='g', linestyle='-')
    plt.show()

    plt.plot(x_list, y2_list)
    plt.axhline(y=arithmetic_mean(data), color='r', linestyle='-')
    plt.axhline(y=zad1.median(data), color='g', linestyle='-')
    plt.show()
