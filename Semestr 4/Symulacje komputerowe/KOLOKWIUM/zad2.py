import numpy as np


def FUN(a, b, dt, N):
    t = np.zeros(N)
    for i in range(N):
        x, y = generate_start_point(b)
        time = 0
        while True:
            time += dt
            x += np.sqrt(dt) * np.random.normal(0, 1)
            y += np.sqrt(dt) * np.random.normal(0, 1)
            if x ** 2 / a + y ** 2 / (b*(1+time)) > 1:
                t[i] = time
                break
    return np.mean(t)


def generate_start_point(b):
    while True:
        x1 = np.random.uniform(0, b/2)
        y1 = np.random.uniform(0, b/2)
        if x1 ** 2 + y1 ** 2 <= (b/2) ** 2:
            return x1, y1


a = 0.75
b = 0.5
dt = 10 ** (-4)
N = 10 ** 3
print(FUN(a=a, b=b, dt=dt, N=N))
