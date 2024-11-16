import matplotlib.pyplot as plt
import numpy as np
import time


def w(x):
    return 6 * x**4 + 5 * x**3 - 13 * x**2 + x + 1


def horner(x):
    return x * (x * (x * (6 * x + 5) - 13) + 1) + 1


def measure_time(f, x):
    start = time.time()
    f(x)
    end = time.time()
    return end - start



if __name__ == '__main__':
    dx = 0.0001
    x = np.arange(-10, 10, dx)
    a = measure_time(w, x)
    b = measure_time(horner, x)
    print(a, b)




