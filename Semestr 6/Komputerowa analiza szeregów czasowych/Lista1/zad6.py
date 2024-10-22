import matplotlib.pyplot as plt
import numpy as np


def main():
    data = np.loadtxt('zad6_lista1.txt')
    x = data[:,0]
    y = data[:,1]

    plt.scatter(x,y)
    plt.show()


if __name__ == '__main__':
    main()
