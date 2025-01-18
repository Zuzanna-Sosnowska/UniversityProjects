import matplotlib.pyplot as plt
import numpy as np
import integrals
import scipy.integrate as integrate


def main():
    v = [0, 1.0, 1.8, 2.4, 3.5, 4.4, 5.1, 6.0]
    P = [0, 4.7, 12.2, 19.0, 31.8, 40.1, 43.8, 43.2]
    m = 2000
    v1 = 1
    v2 = 6
    points = list(zip(v, P))
    phi_coeffs = integrals.polynomial_approximation(points, 3)
    phi = integrals.polynomial(phi_coeffs)
    v_range = np.linspace(v1, v2, 1000)

    plt.plot(v_range, phi(v_range))
    plt.scatter(v, P)
    plt.show()

    def f(v): return v / phi(v)

    # Obliczenie czasów
    delta_t_trapezoidal = m * integrals.integrate_trapezoidal(f, v1, v2, 1000)
    delta_t_simpson = m * integrals.integrate_simpson(f, v1, v2, 1000)

    # Wyniki
    print(f"Czas potrzebny (metoda trapezów): {delta_t_trapezoidal:.2f} s")
    print(f"Czas potrzebny (metoda simpsona): {delta_t_simpson:.2f} s")


if __name__ == '__main__':
    main()

