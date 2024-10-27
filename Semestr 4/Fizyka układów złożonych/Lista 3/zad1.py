import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def percolation(n, m, p=0.5):
    A = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            u = np.random.random()
            if u < p:
                A[i, j] = 1
    return A


def burning_method(A):
    last = []
    for i in range(A.shape[1]):
        if A[0, i] == 1:
            A[0, i] = 2
            last.append((0, i))
    x = 3
    stop = False
    while last:
        tmp = []
        for (i, j) in last:
            b = []
            if i > 0:
                b.append((i - 1, j))
            if i < A.shape[0] - 1:
                b.append((i + 1, j))
            if j > 0:
                b.append((i, j - 1))
            if j < A.shape[1] - 1:
                b.append((i, j + 1))
            for (k, l) in b:
                if A[k, l] == 1:
                    A[k, l] = x
                    if k == A.shape[0] - 1:
                        stop = True
                        break
                    tmp.append((k, l))
            if stop:
                break
        if stop:
            break
        last = tmp
        x += 1
    if stop:
        return x - 1
    return 0


if __name__ == '__main__':

    u = np.linspace(0, 1, 100)
    x = []
    for i in u:
        y = 0
        for j in range(100):
            a = burning_method(percolation(100, 100, i))
            if a != 0:
                y += 1
        x.append(y/100)

    plt.plot(u, x)
    plt.savefig('plot.png')
    plt.close()

    np.savetxt('os_x.txt', u, fmt='%4')
    np.savetxt('os_y.txt', x, fmt='%4')

    A = percolation(100, 100, 0.6)

    burning_method(A)
    plt.imshow(A, cmap='magma', interpolation='nearest')
    plt.show()
    plt.savefig('burning_method.png')
    plt.close()

