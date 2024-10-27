import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

option = 1
dataset_name = "EM2015.csv" if option == 1 else "EM2023.csv"
x = pd.read_csv(dataset_name, encoding='latin1', sep=';', low_memory=False,
                header=0, skiprows=[1, 2], decimal=',')
x.columns = [i for i in range(1, len(x.columns) + 1)]
print(x)

a = x.loc[:, 90 if option == 1 else 91].to_numpy()
b = x.loc[:, 87 if option == 1 else 88].to_numpy().astype(int)
print(b)

c = []
for i in range(len(b)):
    if a[i] is not None:
        for _ in range(b[i]):
            c.append(a[i])

plt.hist(c, density=True, bins=20)
plt.show()

sns.ecdfplot(c)
plt.show()
