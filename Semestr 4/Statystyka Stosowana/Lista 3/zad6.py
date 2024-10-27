import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def exp_dist(lambd):
    return np.random.exponential(1/lambd)


def max_dist(x, y):
    return max(x, y)


def min_dist(x, y):
    return min(x, y)


def z_dist(z):
    return (np.exp(3*z)-np.exp(2*z)-np.exp(z)+1)/np.exp(3*z)


def w_dist(w):
    return 1 - np.exp(-3*w)


n = 1000
a = np.linspace(0, 10, n)
z = z_dist(a)
w = w_dist(a)
z_list = []
w_list = []
for i in range(n):
    z_list.append(max_dist(exp_dist(1.0), exp_dist(2.0)))
    w_list.append(min_dist(exp_dist(1.0), exp_dist(2.0)))

sns.ecdfplot(z_list)
plt.plot(a, z)
plt.show()

sns.ecdfplot(w_list)
plt.plot(a, w)
plt.show()
