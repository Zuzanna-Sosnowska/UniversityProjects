import numpy as np


def wiener(R, dt, n=1000):
    t = np.zeros(n)
    for i in range(n):
        x = 0
        y = 0
        time = 0
        while True:
            time += dt
            x += np.sqrt(dt) * np.random.normal(0, 1)
            y += np.sqrt(dt) * np.random.normal(0, 1)
            if x ** 2 + y ** 2 > R:
                t[i] = time
                break
    return np.mean(t)


def main():
    print(wiener(0.5, 10 ** (-4), 10 ** 4))


if __name__ == '__main__':
    main()
