import numpy as np
import matplotlib.pyplot as plt
import differential_equations as ode


def first_trajectory():
    gravity_const = 9.81  # przyspieszenie ziemskie
    rho = 1.2  # gęstość powietrza
    cw = 0.35  # współczynnik oporu powietrza

    def f1(x, y):
        return y[1]

    def f2(x, y, m):
        return 0

    def g1(x, y):
        return y[1]

    def g2(x, y, m):
        return - gravity_const

    cases = [
        (0.145, 10, 45),
        (0.145, 10, 60),
        (0.40, 10, 45),
        (0.145, 20, 45),
        (0.145, 20, 45),
    ]

    for i, (m, v0, angle) in enumerate(cases):
        alpha = angle * np.pi / 180
        t_max = 2 / gravity_const * v0 * np.sin(alpha)
        v0x = v0 * np.cos(alpha)
        v0y = v0 * np.sin(alpha)

        f_vector = [f1, lambda x, y: f2(x, y, m)]
        func1 = lambda x, y: np.array([f(x[i], y) for i, f in enumerate(f_vector)])
        initial_cond1 = [np.array([0, 0]), np.array([0, v0x])]

        g_vector = [g1, lambda x, y: g2(x, y, m)]
        func2 = lambda x, y: np.array([g(x[i], y) for i, g in enumerate(g_vector)])
        initial_cond2 = [np.array([0, 0]), np.array([0, v0y])]

        dt = 0.01
        n = int(t_max / dt + 1)
        tx_vals, x_vals = ode.runge_kutta_4th_order(func=func1, point=initial_cond1, h=dt, n=n)
        ty_vals, y_vals = ode.runge_kutta_4th_order(func=func2, point=initial_cond2, h=dt, n=n)

        x = [vect[0] for vect in x_vals]
        y = [vect[0] for vect in y_vals]

        plt.plot(x, y, label=fr'$m =$ {m}, $v_0 =$ {v0}, $\alpha =$ {angle} $\degree$')
    plt.title("Trajektorie rzutu ukośnego piłki bez oporów ruchu")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def second_trajectory():
    gravity_const = 9.81
    rho = 1.2
    cw = 0.35

    def drag_force(vx, vy, A):
        V = np.sqrt(vx ** 2 + vy ** 2)
        Fd_x = -0.5 * cw * rho * A * V * vx / m
        Fd_y = -0.5 * cw * rho * A * V * vy / m
        return Fd_x, Fd_y

    def f_1(t, p, m, A):
        x1, x2, y1, y2 = p
        return x2

    def f_2(t, p, m, A):
        x1, x2, y1, y2 = p
        return drag_force(vx=x2, vy=y2, A=A)[0] / m

    def f_3(t, p, m, A):
        x1, x2, y1, y2 = p
        return y2

    def f_4(t, p, m, A):
        x1, x2, y1, y2 = p
        return - gravity_const + drag_force(vx=x2, vy=y2, A=A)[1] / m


    cases = [
        (10, 45, 0.145, 0.0042),
        (10, 60, 0.145, 0.0042),
        (10, 45, 0.4, 0.0042),
        (20, 45, 0.145, 0.0042),
        (20, 45, 0.145, 0.03),
    ]


    for v0, angle, m, A in cases:
        alpha = angle * np.pi / 180

        v = np.array([v0 * np.cos(alpha), v0 * np.sin(alpha)])
        F0 = drag_force(v[0], v[1], A)
        F0x, F0y = F0

        f_vector = [f_1, f_2, f_3, f_4]
        func = lambda t, p: np.array([f(t[i], p, m, A) for i, f in enumerate(f_vector)])
        initial_cond = [np.array([0, 0, 0, 0]), np.array([0, v[0], 0, v[1]])]

        dt = 0.01
        t_max = 3
        n = int(t_max / dt + 1)
        t_vals, p_vals = ode.runge_kutta_4th_order(func=func, point=initial_cond, h=dt, n=n)

        p_vals = list(filter(lambda vect: vect[2] >= 0, p_vals))
        x_vals = [vect[0] for vect in p_vals]
        y_vals = [vect[2] for vect in p_vals]


        plt.plot(x_vals, y_vals, label=fr'$m =$ {m}, $v_0 =$ {v0}, $\alpha =$ {angle} $\degree$, $A =$ {A}')
    plt.title("Trajektorie rzutu ukośnego piłki z oporami ruchu")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def main():
    first_trajectory()
    second_trajectory()

if __name__ == '__main__':
    main()
