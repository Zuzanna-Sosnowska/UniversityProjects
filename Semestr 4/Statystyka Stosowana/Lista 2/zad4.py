import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import zad3


def boxplot(data):
    plt.boxplot(data)
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('HousePrices.csv')
    data = np.array(df.loc[:, "price"].astype(float))
    boxplot(data)
