import matplotlib.pyplot as plt
import numpy as np


def plotPolynomial(x):
    pass


def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y


x = np.linspace(0, 9, 10)
coeffs = [1, 2, 3, 4, 5]
plt.plot(x, PolyCoefficients(x, coeffs))
plt.show()
