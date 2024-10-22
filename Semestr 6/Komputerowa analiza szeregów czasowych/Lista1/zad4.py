import matplotlib.pyplot as plt
import numpy as np
import zad3


def main():
    data = np.loadtxt('zad4_lista1.txt')
    x = data[:,0]
    y = data[:,1]

    b0, b1 = zad3.prosta_regresji(x, y)
    y2 = b0 + b1 * x

    plt.scatter(x,y)
    plt.plot(x,y2, color='red')
    plt.show()

    e = y - y2

    plt.scatter(np.linspace(0, len(e), len(e)), e)
    plt.show()

    e_sr = np.mean(e)
    print(e_sr)
    print(np.max(e))

    lst = []
    for i in range(len(e)):
        if e[i] > 100 or e[i] < -100:
            lst.append(i)

    plt.scatter(x, y)
    plt.scatter(x[lst], y[lst], color='yellow')
    plt.plot(x, y2, color='red')
    plt.show()

    new_x = []
    new_y = []
    for i in range(len(x)):
        if i not in lst:
            new_x.append(x[i])
            new_y.append(y[i])

    b00, b11 = zad3.prosta_regresji(new_x, new_y)
    y_2 = b00 + b11 * x

    plt.scatter(new_x, new_y)
    plt.plot(x, y_2, color='red')
    plt.show()

    # plt.scatter(x, y)
    # plt.plot(x, y2, color='red')
    # for i in range(len(x)):
    #     plt.plot([x[i], x[i]],[y[i], y2[i]], color='orange')
    # plt.show()


if __name__ == '__main__':
    main()
