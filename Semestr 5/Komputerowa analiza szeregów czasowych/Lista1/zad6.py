import matplotlib.pyplot as plt
import numpy as np
import zad3


def main():
    data = np.loadtxt('zad6_lista1.txt')
    x = data[:,0]
    y = data[:,1]

    y1 = np.log(y)

    b0, b1 = zad3.prosta_regresji(x, y1)

    x_1 = np.linspace(-3.5, 3.5, 10000)
    y_1 = b0 + b1 * x_1

    plt.scatter(x, y1)
    plt.plot(x_1, y_1, color='red')
    plt.title(r'Regresja liniowa dla przetransformowanych danych')
    plt.grid(True)
    plt.show()

    a = np.exp(b0)
    b = b1

    y_2 = a * np.exp(b*x_1)

    plt.scatter(x, y)
    plt.plot(x_1, y_2, color='red')
    plt.title('Krzywa dopasowania dla wejściowych danych')
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    main()
