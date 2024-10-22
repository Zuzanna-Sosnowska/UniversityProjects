import matplotlib.pyplot as plt
import numpy as np


def main():
    data = np.loadtxt('zad4_lista1.txt')
    x = data[:,0]
    y = data[:,1]

    x = x[:990]
    y = y[:990]
    print(len(x))


if __name__ == '__main__':
    main()
