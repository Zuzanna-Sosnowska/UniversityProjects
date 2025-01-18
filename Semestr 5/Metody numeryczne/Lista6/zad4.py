import matplotlib.pyplot as plt
import numpy as np
import integrals


def main():
    a, b = 0, np.pi/2

    def f(theta0, t): return np.power(1 - np.sin(theta0 / 2) ** 2 * np.sin(t) ** 2, -0.5)

    def h(theta0):
        return integrals.integrate_simpson(f=lambda t: f(theta0, t), a=a, b=b, n=1111)

    def h2(theta0):
        return integrals.integrate_trapezoidal(f=lambda t: f(theta0, t), a=a, b=b, n=1111)

    theta0 = np.array([15, 30, 45])

    # Wartość theta0 w radianach
    theta0 = theta0 * np.pi / 360

    int_list = h(theta0)
    int_list2 = h2(theta0)
    print(int_list)
    print(int_list2)


if __name__ == '__main__':
    main()
