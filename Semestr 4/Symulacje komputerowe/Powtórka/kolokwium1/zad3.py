import numpy as np


def estrisk(u, c, lambd, miu, T):
    times, steps = proces_odnowy(a=2/lambd, T=T)
    x = np.random.exponential(miu, steps)
    ct = c * times
    step_lst = np.zeros(2 * (steps + 1))
    for i in range(steps+1):
        step_lst[2 * i] = u + ct[i] - np.sum(x[:i])
        step_lst[2 * i + 1] = u + ct[i + 1] - np.sum(x[:i])
    return times, step_lst


def estrisk2(u, c, lambd, miu, T, M):
    z = 0
    for a in range(M):
        times, steps = proces_odnowy(a=2/lambd, T=T)
        x = np.random.exponential(miu, steps)
        ct = c * times
        capital = u
        for i in range(steps):
            capital += ct[i] - x[i]
            if capital <= 0:
                z += 1
                break
    return z / M


def proces_odnowy(T, a):
    I = 0
    t = 0
    times = []
    while t < T:
        t += np.random.uniform(0, a)
        if t >= T:
            break
        I += 1
        times.append(t)
    times.append(T)
    return times, I


def main():
    c = 3
    lambd = 1
    miu = 5
    T = 1
    u = 5
    M = 10 ** 4
    z = 0
    for i in range(M):
        x, y = estrisk(u=u, c=c, lambd=lambd, miu=miu, T=T)
        if np.min(y) <= 0:
            z += 1
    print(z/M)

    print(estrisk2(u=u, c=c, miu=miu, lambd=lambd, T=T, M=M))


if __name__ == '__main__':
    main()

