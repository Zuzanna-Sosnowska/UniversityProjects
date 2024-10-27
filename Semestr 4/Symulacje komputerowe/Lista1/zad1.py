import matplotlib.pyplot as plt
import numpy as np


def LCG_generator(seed, length, m=2**31 -1, a=16807, c=0):
    arr = []
    for i in range(length):
        seed = (a * seed + c) % m
        arr.append(seed)
    return np.array(arr)


if __name__ == '__main__':
    rand_nums = LCG_generator(12, 10000)
    rand_nums = rand_nums/(2**31 - 1)
    plt.hist(rand_nums, density=True)
    plt.show()
