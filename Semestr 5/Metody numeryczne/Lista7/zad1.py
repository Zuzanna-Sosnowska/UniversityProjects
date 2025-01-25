import numpy as np
import matplotlib.pyplot as plt
import differential_equations as ode


def main():
    def analytical_solution(x):
        return (31 / 32) * np.exp(-4 * x) + 0.25 * np.power(x, 2) - 0.125 * x + (1 / 32)

    def f(x, y):
        return np.power(x, 2) - 4 * y

    stop = 0.03
    h1 = stop
    h2 = stop / 2
    h4 = stop / 4
    h300 = stop / 300
    point = 0, 1
    euler_sol1 = ode.euler_method(f, point, h1, stop)
    euler_sol2 = ode.euler_method(f, point, h2, stop)
    euler_sol4 = ode.euler_method(f, point, h4, stop)

    runge_kutta_2nd_order_sol1 = ode.runge_kutta_2nd_order(f, point, h1, stop)
    runge_kutta_2nd_order_sol2 = ode.runge_kutta_2nd_order(f, point, h2, stop)
    runge_kutta_2nd_order_sol4 = ode.runge_kutta_2nd_order(f, point, h4, stop)

    runge_kutta_4rd_order_sol1 = ode.runge_kutta_4rd_order(f, point, h1, stop)
    runge_kutta_4rd_order_sol2 = ode.runge_kutta_4rd_order(f, point, h2, stop)
    runge_kutta_4rd_order_sol4 = ode.runge_kutta_4rd_order(f, point, h4, stop)

    sol = analytical_solution(stop)

    print(euler_sol1[1][-1] - sol , euler_sol2[1][-1] - sol , euler_sol4[1][-1] - sol , sep='\n')
    print('\n')
    print(runge_kutta_2nd_order_sol1[1][-1] - sol, runge_kutta_2nd_order_sol2[1][-1] - sol, runge_kutta_2nd_order_sol4[1][-1] - sol, sep='\n')
    print('\n')
    print(runge_kutta_4rd_order_sol1[1][-1] - sol, runge_kutta_4rd_order_sol2[1][-1] - sol,
          runge_kutta_4rd_order_sol4[1][-1] - sol, sep='\n')
    print('\n')
    print(sol)


if __name__ == '__main__':
    main()
