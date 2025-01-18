import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def theor_MA_autocor(h, theta):
    if h == 0:
        return 1
    elif h == 1 or h == -1:
        return theta / (1 + theta ** 2)
    else:
        return 0


def autocov(x, h):
    n = len(x)
    x_m = np.mean(x)
    h = abs(h)
    if h >= n:
        raise ValueError("Wrong h!")
    return (1 / n) * np.sum((x[:n - h] - x_m) * (x[h:] - x_m))


def autocor(x, h):
    return autocov(x, h) / autocov(x, 0)


def MA(n, theta, loc=0, scale=1):
    z = np.random.normal(loc=loc, scale=scale, size=n+1)
    return z[1:] + theta * z[:-1]


def m(t, a1, a2):
    return a1 * t + a2


def s(t, b1, b2):
    return b1 * np.sin(b2 * t)


def main():
    t0 = 0
    t = np.arange(t0, t0 + 10.01, 0.01)
    n = len(t)
    a1, a2 = 1.5, 5
    b1, b2 = 2, 3
    theta = 0.5
    sigma = 0.5
    Xt = MA(n=n, theta=theta, loc=0, scale=sigma)
    Yt = Xt + m(t, a1, a2) + s(t, b1, b2)

    a1_est, a2_est = np.polyfit(t, Yt, 1)
    Zt = Yt - m(t, a1_est, a2_est)

    N = len(t)

    params, params_covariance = curve_fit(f=s, xdata=t, ydata=Zt, p0=[max(Zt), 2 * np.pi / 2])

    b1_est, b2_est = params

    At = Zt - s(t=t, b1=b1_est, b2=b2_est)

    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, Yt, label="Oryginalne dane")
    plt.title("Oryginalne dane")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, Zt, label="usunięty trend liniowy")
    plt.title("Po usunięciu trendu liniowego")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, At, label="usunięty trend i sinusoida")
    plt.plot(t, Xt, label="dane sprzed dodania trendu i sinusoidy", color="red", zorder=1)
    plt.title("Po usunięciu trendu i sinusoidy")
    plt.legend()

    plt.tight_layout()
    plt.show()

    h = np.arange(0, 11, 1)
    Z_autocor = [autocor(At, lag) for lag in h]
    theor_autocor = [theor_MA_autocor(lag, theta) for lag in h]

    plt.scatter(h, Z_autocor, label="empiryczna")
    plt.scatter(h, theor_autocor, label="teoretyczna")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
