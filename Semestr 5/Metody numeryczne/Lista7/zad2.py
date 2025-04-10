import numpy as np
import matplotlib.pyplot as plt
import differential_equations as ode


def main():

    def f(x, y):
        return np.sin(y)


    def analytical_solution(x):
        return 2 * np.arctan(np.exp(x) * np.tan(0.5))


    h = 0.1
    stop = 0.5
    n = int(stop // h + 1)
    initial_cond = (0, 1)

    euler = ode.euler_method(f, initial_cond, h, n)
    runge_kutta_4rd_order = ode.runge_kutta_4th_order(f, initial_cond, h, n)
    x = np.arange(0, stop + h, h)
    solution = analytical_solution(x)

    plt.plot(x, solution, label="rozwiązanie analityczne")
    plt.plot(*euler, label="euler")
    plt.plot(*runge_kutta_4rd_order, label="runge kutta 4rd")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
