import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as stattools
import numpy as np


def MA1(n, theta, loc=0, scale=1):
    z = np.random.normal(loc=loc, scale=scale, size=n+1)
    return z[1:] + theta * z[:-1]


def theor_PACF(k, theta):
    if k == 0:
        return 1
    if k >= 1:
        return - (- theta) ** k / np.sum([theta ** (2*i) for i in range(k+1)])


def main():
    theta = 2
    sigma2 = 0.5
    n = 1000
    N = 100
    y = np.arange(0, 20, 1)

    lst = []
    for i in range(N):
        x = MA1(n, theta, loc=0, scale=np.sqrt(sigma2))
        est_PACF = stattools.pacf(x, 19)
        lst.append(est_PACF)

    q_005 = []
    q_095 = []
    for k in range(20):
        q =  np.sort([elems[k] for elems in lst])
        q_005.append(q[4])
        q_095.append(q[-5])


    th_PACF = np.array([theor_PACF(yi, theta) for yi in y])


    plt.plot(y, est_PACF, color='red', label='estimated')
    plt.plot(y, th_PACF, color='orange', label='theoretical')
    plt.fill_between(y, q_005, q_095, color='lightblue')
    plt.legend(loc='best')
    plt.grid(True)
    plt.title("PACF")
    plt.show()


if __name__ == '__main__':
    main()
