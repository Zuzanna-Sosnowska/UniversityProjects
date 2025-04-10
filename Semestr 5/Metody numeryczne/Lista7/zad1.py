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
    euler_sol1 = ode.euler_method(f, point, h1, 1)
    euler_sol2 = ode.euler_method(f, point, h2, 2)
    euler_sol4 = ode.euler_method(f, point, h4, 4)

    runge_kutta_2nd_order_sol1 = ode.runge_kutta_2nd_order(f, point, h1, 1)
    runge_kutta_2nd_order_sol2 = ode.runge_kutta_2nd_order(f, point, h2, 2)
    runge_kutta_2nd_order_sol4 = ode.runge_kutta_2nd_order(f, point, h4, 4)

    runge_kutta_4rd_order_sol1 = ode.runge_kutta_4th_order(f, point, h1, 1)
    runge_kutta_4rd_order_sol2 = ode.runge_kutta_4th_order(f, point, h2, 2)
    runge_kutta_4rd_order_sol4 = ode.runge_kutta_4th_order(f, point, h4, 4)

    sol = analytical_solution(stop)

    print(euler_sol1[1][-1] - sol , euler_sol2[1][-1] - sol , euler_sol4[1][-1] - sol , sep='\n')
    print('\n')
    print(runge_kutta_2nd_order_sol1[1][-1] - sol, runge_kutta_2nd_order_sol2[1][-1] - sol, runge_kutta_2nd_order_sol4[1][-1] - sol, sep='\n')
    print('\n')
    print(runge_kutta_4rd_order_sol1[1][-1] - sol, runge_kutta_4rd_order_sol2[1][-1] - sol,
          runge_kutta_4rd_order_sol4[1][-1] - sol, sep='\n')
    print('\n')
    print(sol)

    h_values = [0.03, 0.015, 0.0075]  # 1 step, 2 steps, 4 steps to x=0.03

    for h in h_values:
        steps = int(0.03 / h)
        x_euler, y_euler = ode.euler_method(f, point, h, steps)
        x_rk2, y_rk2 = ode.runge_kutta_2nd_order(f, point, h, steps)
        x_rk4, y_rk4 = ode.runge_kutta_4th_order(f, point, h, steps)

        # Solve using each method and plot results
        plt.figure(figsize=(10, 6))
        x_analytical = np.linspace(0, 0.03, 100)
        y_analytical = analytical_solution(x_analytical)
        plt.plot(x_analytical, y_analytical, 'k-', label='Analytical Solution')

        plt.plot(x_euler, y_euler, 'o-', label=f'Euler (h={h})')
        plt.plot(x_rk2, y_rk2, 's-', label=f'RK2 (h={h})')
        plt.plot(x_rk4, y_rk4, 'd-', label=f'RK4 (h={h})')
        plt.xlabel('x')
        plt.ylabel('y(x)')
        plt.legend()
        plt.title("Comparison of Numerical Methods")
        plt.show()


if __name__ == '__main__':
    main()
