import matplotlib.pyplot as plt
import numpy as np
import pickle


def compute_min_and_max(f, a, b, n=1000):
    min_value, max_value = float("inf"), float("-inf")
    for i in range(n):
        res = f(a + (b-a)*i/n)
        if min_value > res:
            min_value = res
        if max_value < res:
            max_value = res
    return min_value, max_value


def density_interval(f, a, b, n):
    x = [(a + (b-a)*i/n, a + (b-a)*(i+1)/n) for i in range(n-1)]
    y = []
    for (i, j) in x:
        y.append(compute_min_and_max(f, i, j))
    return x, y


def h(x, alpha=2):
    return (1+alpha) * np.power(x, alpha)


def ziggurat(x_data, y_data, h, alpha=2, g=np.random.uniform, n=1000):
    i = 0
    lst = []
    j = 0
    while i < n:
        x = g()
        u = np.random.uniform(0, 1)

        f, F = (0, 0)

        for j in range(len(x_data)):
            if x_data[j][0] <= x <= x_data[j][1]:
                f, F = y_data[j]

        if u * x < f:
            lst.append(x)
            i += 1
            j += 1

        elif u * x > F:
            j += 1
            continue

        elif u <= h(x, alpha):
            lst.append(x)
            i += 1
        j += 1
    return lst, i/j


# x, y = density_interval(h,0, 1, 10)
# with open('dane.pkl', 'wb') as plik:
#     pickle.dump(x, plik)
#     pickle.dump(y, plik)


with open('dane.pkl', 'rb') as plik:
    x1 = pickle.load(plik)
    y1 = pickle.load(plik)

lst, i = ziggurat(x1, y1, h, alpha=2, g=np.random.uniform, n=1000)

print(i)

plt.hist(lst, density=True)
plt.show()
