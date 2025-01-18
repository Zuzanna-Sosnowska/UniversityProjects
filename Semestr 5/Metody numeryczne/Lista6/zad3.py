import matplotlib.pyplot as plt
import numpy as np
import integrals


def main():
    a, b = 1, np.inf

    a2, b2 = 0, 1

    def f2(x):
        return 1 / 3 * np.power(np.power(x, 4 / 3) + 1, -1)

    integ = integrals.integrate_trapezoidal(f2, a2, b2, 6)
    print(integ)


if __name__ == '__main__':
    main()
