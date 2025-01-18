import matplotlib.pyplot as plt
import numpy as np
import integrals


def main():
    a, b = -1, 1

    def f1(x): return np.cos(2 * np.power(np.cos(x), -1))

    def f2(x): return np.cos(2 * np.arccos(x))


    simpson3_f1 = integrals.integrate_simpson(f1, a, b, 3)
    simpson5_f1 = integrals.integrate_simpson(f1, a, b, 5)
    simpson7_f1 = integrals.integrate_simpson(f1, a, b, 7)

    simpson3_f2 = integrals.integrate_simpson(f2, a, b, 3)
    simpson5_f2 = integrals.integrate_simpson(f2, a, b, 5)
    simpson7_f2 = integrals.integrate_simpson(f2, a, b, 7)

    print(simpson3_f1)
    print(simpson5_f1)
    print(simpson7_f1)
    print("\n")
    print(simpson3_f2)
    print(simpson5_f2)
    print(simpson7_f2)


if __name__ == '__main__':
    main()
