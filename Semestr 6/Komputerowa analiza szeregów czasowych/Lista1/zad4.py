import matplotlib.pyplot as plt
import numpy as np
import zad3


def main():
    data = np.loadtxt('zad4_lista1.txt')
    x = data[:,0]
    y = data[:,1]

    b0, b1 = zad3.prosta_regresji(x, y)
    y2 = b0 + b1 * x

    # plt.scatter(x,y)
    # plt.plot(x,y2, color='red')
    # plt.show()

    residue = np.abs(y - y2)

    e_sr = np.mean(residue)
    print(e_sr)
    print(np.max(residue))
    print(np.min(residue))

    # plt.scatter(x, y)
    # plt.plot(x, y2, color='red')
    # for i in range(len(x)):
    #     plt.plot([x[i], x[i]],[y[i], y2[i]], color='orange')
    # plt.show()


if __name__ == '__main__':
    main()
