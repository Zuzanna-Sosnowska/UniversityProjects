import matplotlib.pyplot as plt
import numpy as np
import integrals
import scipy.integrate as integrate


def main():
    a, b = 1, np.pi

    def f(x): return np.log(x) / (np.power(x, 2) - 2 * x + 2)

    nodes2, weights2 = np.polynomial.legendre.leggauss(2)
    nodes4, weights4 = np.polynomial.legendre.leggauss(4)

    int1 = integrals.GaussLegendre(f, a, b, weights=weights2, nodes=nodes2)
    int2 = integrals.GaussLegendre(f, a, b, weights=weights4, nodes=nodes4)

    sp_int = integrate.quad(f, a, b)[0]

    print(int1, int2)
    print(sp_int)


if __name__ == '__main__':
    main()
