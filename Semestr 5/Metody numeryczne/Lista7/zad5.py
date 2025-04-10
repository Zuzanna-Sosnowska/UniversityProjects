import numpy as np
import matplotlib.pyplot as plt
import differential_equations as ode


def shooting_method(func, b_cond, a_part, h=10 ** 5 + 1, epsilon=0.001, method=ode.euler_method):
    """
    :param func: funkcja f(x, y)
    :param b_cond: warunkek brzegowy zadany w postaci: [(x_0, y(x_0)), (x_1, y(x_1))]
    :param rng: przedział, dla jakiego chcemy mieć tablicę wartości funkcji x
    :param a_part: przedział, z którego będziemy szukać odpowiedniego parametru c
    :param h: podział przedziału (krok)
    :param epsilon: parametr, który określa nam dokładność, z jaką chcemy rozwiązać warunek brzegowy
    :return: c, gdzie c jest wartością y'(x_0)
    """
    # sprawdzanie wartości na krańcach przedziału. Szukanie c metodą bisekcji
    n = int(b_cond[1][0] / h + 1)
    a = method(func = func, point = [np.array([b_cond[0][0], b_cond[0][0]]), np.array([b_cond[0][1], a_part[0]])], h=h, n=n)[1][-1][0] - b_cond[1][1]
    b = method(func = func, point = [np.array([b_cond[0][0], b_cond[0][0]]), np.array([b_cond[0][0], a_part[1]])], h = h, n = n)[1][-1][0] - b_cond[1][1]

    if a * b >= 0:
        raise Exception("Dobierz inny przedział a_part")
    while True:
        c = (a_part[1] + a_part[0]) / 2
        p = method(func=func, point=[np.array([b_cond[0][0], b_cond[0][0]]), np.array([b_cond[0][0], c])], h = h, n = n)
        q = p[1][-1][0] - b_cond[1][1]
        if abs(q) <= epsilon:
            return c
        else:
            if a * q > 0:
                a_part = (c, a_part[1])
            elif a * q < 0:
                a_part = (a_part[0], c)


def main():
    h = 0.01
    boundary_conditions = [(0, 0), (np.pi / 2, 1)]

    def f1(x, y):
        y1, y2 = y
        return y2

    def f2(x, y):
        y1, y2 = y
        return - (1 + 0.2 * x) * y1 ** 2

    f_vector = [f1, f2]
    func = lambda x, y: np.array([f(x[i], y) for i, f in enumerate(f_vector)])
    parting = (-1, 3)

    c = shooting_method(func=func, b_cond = boundary_conditions, a_part=parting, h=h, epsilon=0.01, method=ode.runge_kutta_4th_order)
    print(c)
    initial_conditions = [np.array([0, 0]), np.array([0, c])]

    x_max = 3.0
    n = int(x_max / h + 1)

    x_vals, y_vals = ode.runge_kutta_4th_order(func=func, point=initial_conditions, h=h, n=n)

    x = [vect[0] for vect in x_vals]
    y = [vect[0] for vect in y_vals]

    plt.plot(x, y, label=rf"Rozwiązanie dla $y'(0) \approx$ {round(c, 3)}")
    plt.title("Rozwiązanie równania różniczkowego z zagadnieniem brzegowym")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
