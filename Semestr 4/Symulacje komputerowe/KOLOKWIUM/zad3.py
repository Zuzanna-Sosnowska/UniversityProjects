import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy
import math


def inverse_dist(lambda_func, c, T):
    u = np.random.uniform(0, 1)
    return scipy.optimize.fsolve(func=lambda x: scipy.integrate.quad(func=lambda_func, a=0, b=x)[0] - c*u, x0=T,
                          fprime=lambda_func)[0]


def non_uniform_poisson_process(lambda_func, T):
    mT = scipy.integrate.quad(lambda_func, 0, T)[0]
    n = np.random.poisson(mT)
    times = np.array([inverse_dist(lambda_func, mT, T) for _ in range(n)])
    times.sort()
    return times, np.linspace(0, n, n+1)


def Cox_process(sigma, dt, T):
    n = int(T/dt)
    times, steps = np.zeros(n), np.zeros(n)
    for i in range(n):
        times[i], steps[i] = dt*i, non_uniform_poisson_process(wiener, dt*i)
    return times, steps


def ESTRISK(u, c, sigma, miu, T, dt, M):
    z = 0
    for a in range(M):
        times, steps = Cox_process(sigma, dt, T)
        x = np.random.exponential(miu, steps)
        ct = c * times
        capital = u
        for i in range(steps):
            capital += ct[i] - x[i]
            if capital <= 0:
                z += 1
                break
    return z / M


def wiener(T, sigma=2):
    return sigma * np.abs(np.random.normal(0, 1) * np.sqrt(T))

if __name__ == '__main__':
    u = 5
    c = 3
    T = 1
    sigma = 2
    miu = 5
    M = 10 ** 4
    dt = 10 ** (-4)
    z = ESTRISK(u=u, c=c, T=T, sigma=sigma, miu=miu, M=M, dt=dt)
    print(z)
