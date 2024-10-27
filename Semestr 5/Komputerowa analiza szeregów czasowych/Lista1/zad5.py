import matplotlib.pyplot as plt
import numpy as np
import zad3

def main():
    data = np.loadtxt('zad4_lista1.txt')
    x = data[:,0]
    y = data[:,1]

    x1 = x[:990]
    y1= y[:990]

    x2 = x[990:]
    y2 = y[990:]

    b0, b1 = zad3.prosta_regresji(x1, y1)

    y_1 = b0 + b1 * x1
    y_2 = b0 + b1 * x2

    e1 = y1 - y_1
    e2 = y2 - y_2

    plt.scatter(x1, y1, label='zbiór treningowy')
    plt.plot(x1, y_1, color='red')
    plt.scatter(x2, y2, color='green', label='zbiór testowy')
    plt.legend()
    plt.title('Prosta regresji')
    plt.show()

    plt.scatter(np.linspace(991, 1000, 1000-990), e2)
    plt.title('Wartości błędów dla zbioru testowego')
    plt.show()

    print('Średni błąd bezwzględny dla zbioru treningowego:', np.mean(np.abs(e1)))
    print('Średni błąd bezwzględny dla zbioru testowego:', np.mean(np.abs(e2)))
    print('Średni błąd kwadratowy dla zbioru treningowego:', np.mean(np.power(e1,2)))
    print('Średni błąd kwadratowy dla zbioru testowego:', np.mean(np.power(e2,2)))


if __name__ == '__main__':
    main()
