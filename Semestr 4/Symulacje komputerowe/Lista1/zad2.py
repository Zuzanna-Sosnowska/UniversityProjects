import matplotlib.pyplot as plt
import numpy as np


def van_der_Corput(n, base):
    arr = []
    for i in range(n+1):
        counter = 0
        a = 0
        while i != 0:
            counter += 1
            a += (i % base) * base**(-counter)
            i = i // base
        arr.append(a)
    return np.array(arr)


if __name__ == '__main__':
    arr = van_der_Corput(10000, 12)

    plt.hist(arr, density=True)
    plt.show()
