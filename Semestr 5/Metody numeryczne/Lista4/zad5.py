import numpy as np


def newton_method(f, df, g, dg, x0, tol=1.0e-9):
    if f(*x0) == 0 and g(*x0) == 0:
        return x0
    x = x0
    while True:
        x = x - np.linalg.inv(np.array([df(*x), dg(*x)])) @ np.array([f(*x), g(*x)])
        if norm(np.array([f(*x), g(*x)])) <= tol:
            break
    return x


def norm(x):
    return np.sqrt(np.sum(x**2))


def main():
    def f(x, y):
        return np.tan(x) - y - 1

    def df(x, y):
        return [1 / np.power(np.cos(x), 2), -1]

    def g(x, y):
        return np.cos(x) - 3 * np.sin(y)

    def dg(x, y):
        return [-np.sin(x), -3 * np.cos(y)]

    sol = newton_method(f, df, g, dg, np.zeros(2))
    print(sol)
    print(f(*sol), g(*sol))


if __name__ == '__main__':
    main()
