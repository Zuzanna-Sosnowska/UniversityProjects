import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 1000
    sigma = 1
    a = 2
    x = MA(n=n, a=a, loc=0, scale=sigma)
    h_lst = np.arange(-101, 101, 1)
    emp_autocov = np.zeros(len(h_lst))
    emp_autocor = np.zeros(len(h_lst))
    theor_autocov = np.zeros(len(h_lst))
    theor_autocor = np.zeros(len(h_lst))
    for i, h in enumerate(h_lst):
        emp_autocov[i] = autocov(x, h)
        emp_autocor[i] = autocor(x, h)
        theor_autocov[i] = theor_MA_autocov(h, sigma, a)
        theor_autocor[i] = theor_MA_autocor(h, sigma, a)

    plt.plot(h_lst, emp_autocov, label='wartości estymowane')
    plt.scatter(h_lst, theor_autocov, color='red', label='wartości teoretyczne')
    plt.title("Porównanie teoretycznych i estymowanych wartości funkcji autokowariancji")
    plt.legend()
    plt.show()

    plt.plot(h_lst, emp_autocor, label='wartości estymowane')
    plt.scatter(h_lst, theor_autocor, color='red', label='wartości teoretyczne')
    plt.title("Porównanie teoretycznych i estymowanych wartości funkcji autokorelacji")
    plt.legend()
    plt.show()


def theor_MA_autocov(h, sigma, a):
    if h == 0:
        return sigma ** 2 * (1 + a ** 2)
    elif h == 1 or h == -1:
        return sigma ** 2 * a
    else:
        return 0


def theor_MA_autocor(h, sigma, a):
    if h == 0:
        return 1
    elif h == 1 or h == -1:
        return a / (1 + a ** 2)
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


def MA(n, a, loc, scale):
    z = np.random.normal(loc=loc, scale=scale, size=n+1)
    return z[1:] + a * z[:-1]


if __name__ == '__main__':
    main()
