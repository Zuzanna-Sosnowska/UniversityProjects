import matplotlib.pyplot as plt
import numpy as np
import zad1
import zad2


def lcg_pi_approx(n=1000, seed=5):
    lst = zad1.LCG_generator(seed, 2*n) / (2**31 - 1)
    x_list = lst[:n]
    y_list = lst[n:]
    x = []
    y = []
    counter = 0
    for i in range(n):
        if x_list[i]**2 + y_list[i]**2 <= 1:
            x.append(x_list[i])
            y.append(y_list[i])
            counter += 1
    return x, y, x_list, y_list, 4 * counter/n


def van_der_corput_pi_approx(n=1000, base1=2, base2=3):
    x_list = zad2.van_der_Corput(n, base1)
    y_list = zad2.van_der_Corput(n, base2)
    x = []
    y = []
    counter = 0
    for i in range(n+1):
        if x_list[i] ** 2 + y_list[i] ** 2 <= 1:
            x.append(x_list[i])
            y.append(y_list[i])
            counter += 1
    return x, y, x_list, y_list, 4 * counter / n


def pi_approx(n=25):
    x_list = np.linspace(0, 1, n)
    y_list = np.linspace(0, 1, n)
    u_list = []
    v_list = []
    x_points = np.zeros(n**2)
    y_points = np.zeros(n**2)
    counter = 0
    c = 0
    for x in x_list:
        for y in y_list:
            x_points[c] = x
            y_points[c] = y
            c += 1
            if x**2 + y**2 <= 1:
                u_list.append(x)
                v_list.append(y)
                counter += 1
    return u_list, v_list, x_points, y_points, 4 * counter/n**2


if __name__ == '__main__':
    result = lcg_pi_approx()
    print(result[4])

    plt.scatter(result[2], result[3], color='blue')
    plt.scatter(result[0], result[1], color='red')
    plt.show()

    result = van_der_corput_pi_approx()
    print(result[4])

    plt.scatter(result[2], result[3], color='blue')
    plt.scatter(result[0], result[1], color='red')
    plt.show()

    result = pi_approx()
    print(result[4])
    plt.scatter(result[2], result[3], color='blue')
    plt.scatter(result[0], result[1], color='red')
    plt.show()
