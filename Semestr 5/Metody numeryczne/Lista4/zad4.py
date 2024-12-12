import matplotlib.pyplot as plt
import numpy as np
import zad1
from scipy.constants import R
from scipy.optimize import root_scalar


def G_function(T, T0=4.44418):
    return -R * T * 2.5 * np.log(T / T0)


def gibbs_free_energy(T, T0=4.44418):
    return -R * T * np.log((T / T0) ** (5 / 2)) + 1e5


def main():
    T0 = 4.44418
    G = -1e5
    t = np.linspace(10, 10000, 100000)
    g = G_function(t) - 1e5
    result = root_scalar(gibbs_free_energy, bracket=[10, 10000], method='brentq')
    if result.converged:
        print(f"Temperatura T wynosi: {result.root} K")
    else:
        print("Nie znaleziono rozwiązania.")
    solution = zad1.brent(lambda x: G_function(x) - G, 10, 10000)
    print(solution)

    plt.plot(t, g-G)
    plt.scatter(solution, G_function(solution))
    plt.show()


if __name__ == '__main__':
    main()

