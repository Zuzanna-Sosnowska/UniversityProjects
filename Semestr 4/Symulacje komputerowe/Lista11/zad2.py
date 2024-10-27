import matplotlib.pyplot as plt
import numpy as np


def wiener(a, b, dt, n=1000):
    t = np.zeros(n)
    for i in range(n):
        w = 0
        time = 0
        while True:
            time += dt
            w += np.sqrt(dt) * np.random.normal(0, 1)
            if w >= b or w <= a:
                t[i] = time
                break
    return t


if __name__ == '__main__':
    t = wiener(-1, 1, 0.001)
    plt.hist(t)
    plt.show()
