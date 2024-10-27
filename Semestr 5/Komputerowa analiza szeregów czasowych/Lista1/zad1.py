import matplotlib.pyplot as plt
import numpy as np


def wykres_rozproszenia(x, y):
    plt.scatter(x, y)
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.title('Wykres rozproszenia')
    plt.grid(True)
    plt.show()


def average(x):
    return np.sum(x)/len(x)


def standard_deviation(x):
    n = len(x)
    return np.sqrt(1 / (n-1) * np.sum(np.power(x - average(x), 2)))


def korelacja_probkowa(x, y):
    if len(x) != len(y):
        raise ValueError('x and y must be the same length')
    n = len(x)
    x_sr = average(x)
    y_sr = average(y)
    std_x = standard_deviation(x)
    std_y = standard_deviation(y)
    return 1 / (n-1) * np.sum((x-x_sr)*(y-y_sr)/(std_x * std_y))


def y1_val(x, y, x_c):
    c1 = np.polyfit(x, y, 1)
    return c1[0] * x_c + c1[1]


def y2_val(x, y, x_c):
    c2 = np.polyfit(x, y, 2)
    return c2[0] * x_c **2 + c2[1] * x_c + c2[2]


def y3_val(x, y, x_c):
    c3 = np.polyfit(x, y, 3)
    return c3[0] * x_c ** 3 + c3[1] * x_c ** 2 + c3[2] * x_c + c3[3]


def y4_val(x, y, x_c):
    c4 = np.polyfit(x, y, 4)
    return c4[0] * x_c ** 4 + c4[1] * x_c ** 3 + c4[2] * x_c ** 2 + c4[3] * x_c + c4[4]


def y5_val(x, y, x_c):
    c5 = np.polyfit(x, y, 5)
    return c5[0] * x_c ** 5 + c5[1] * x_c ** 4 + c5[2] * x_c ** 3 + c5[3] * x_c ** 2 + c5[4] * x_c + c5[5]


def create_plot(x, y):
    x_c = np.linspace(0, 8, 10000)
    y1 = y1_val(x, y, x_c)
    y2 = y2_val(x, y, x_c)
    y3 = y3_val(x, y, x_c)
    y4 = y4_val(x, y, x_c)
    y5 = y5_val(x, y, x_c)

    plt.plot(x_c, y1, color='orange', label='wiel. st.1')
    plt.plot(x_c, y2, color='yellow', label='wiel. st.2')
    plt.plot(x_c, y3, color='red', label='wiel. st.3')
    plt.plot(x_c, y4, color='green', label='wiel. st.4')
    plt.plot(x_c, y5, color='blue', label='wiel. st.5')
    plt.scatter(x, y)
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.legend(loc='best')
    plt.title('Wykres rozproszenia')
    plt.grid(True)
    plt.show()


def main():
    data = np.loadtxt('../Lista1/zad1_lista1.txt')
    x = data[:, 0]
    y = data[:, 1]
    np.sort(x)
    np.sort(y)
    x = np.array(x)
    y = np.array(y)

    create_plot(x, y)

    y1 = y1_val(x, y, x)
    y2 = y2_val(x, y, x)
    y3 = y3_val(x, y, x)
    y4 = y4_val(x, y, x)
    y5 = y5_val(x, y, x)

    sr_blad_bezwzg = np.zeros(5)
    sr_blad_bezwzg[0] = 1 / len(x) * np.sum(np.abs(y - y1))
    sr_blad_bezwzg[1] = 1 / len(x) * np.sum(np.abs(y - y2))
    sr_blad_bezwzg[2] = 1 / len(x) * np.sum(np.abs(y - y3))
    sr_blad_bezwzg[3] = 1 / len(x) * np.sum(np.abs(y - y4))
    sr_blad_bezwzg[4] = 1 / len(x) * np.sum(np.abs(y - y5))
    print('Średni błąd bezwzględny:', sr_blad_bezwzg)

    sr_blad_kwadr = np.zeros(5)
    sr_blad_kwadr[0] = 1 / len(x) * np.sum(np.power(y - y1, 2))
    sr_blad_kwadr[1] = 1 / len(x) * np.sum(np.power(y - y2, 2))
    sr_blad_kwadr[2] = 1 / len(x) * np.sum(np.power(y - y3, 2))
    sr_blad_kwadr[3] = 1 / len(x) * np.sum(np.power(y - y4, 2))
    sr_blad_kwadr[4] = 1 / len(x) * np.sum(np.power(y - y5, 2))

    print('Średni błąd kwadratowy:', sr_blad_kwadr)

    y_mean = np.mean(y)
    suma = np.sum(np.power(y - y_mean, 2))

    r_2 = np.zeros(5)
    r_2[0] = np.sum(np.power(y1 - y_mean, 2)) / suma
    r_2[1] = np.sum(np.power(y2 - y_mean, 2)) / suma
    r_2[2] = np.sum(np.power(y3 - y_mean, 2)) / suma
    r_2[3] = np.sum(np.power(y4 - y_mean, 2)) / suma
    r_2[4] = np.sum(np.power(y5 - y_mean, 2)) / suma

    print('Współczynnik:', r_2)


if __name__ == '__main__':
    main()