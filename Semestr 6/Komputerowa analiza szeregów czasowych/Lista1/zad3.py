import matplotlib.pyplot as plt
import numpy as np
import zad2


def prosta_regresji(x, y):
    b1 = np.sum((x - np.mean(x))*(y - np.mean(y))) / np.sum(np.power(x - np.mean(x), 2))
    b0 = np.mean(y) - b1 * np.mean(x)
    return b0, b1


def main():
    x = np.loadtxt('../Lista1/zad2_lista1.txt')
    y = np.loadtxt('../Lista1/zad3_lista1.txt')
    x = np.array(x)
    y = np.array(y)

    b01, b11 = prosta_regresji(x, y)
    x1 = np.linspace(-1, 10, 1000)
    y1 = b01 + b11 * x1

    plt.plot(x1, y1, color='red', label='prosta regresji')
    plt.scatter(x, y, label='dane')
    plt.title('Prosta regresji dla danych')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    base = 11
    x = zad2.simple_moving_average(x, base)
    y = zad2.simple_moving_average(y, base)
    # y = y[5:len(y)-5]

    b02, b12 = prosta_regresji(x, y)
    x2 = np.linspace(-1, 3.5, 1000)
    y2 = b02 + b12 * x2

    plt.plot(x2, y2, color='green', label='prosta regresji')
    plt.scatter(x, y, label='dane')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(f'Prosta regresji dla danych po wygładzeniu \n prostą średnią ruchomą o podstawie {base}')
    plt.show()



if __name__ == '__main__':
    main()
