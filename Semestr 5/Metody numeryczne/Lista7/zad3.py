import numpy as np
import matplotlib.pyplot as plt
import differential_equations as ode


def main():

    def f1(x, y):
        return y[1]         # y_1'(x) = y_2(x)

    def f2(x, y, A_hat=0.5, omega_hat=2/3, Q=2):
        return A_hat * np.cos(omega_hat * x) - 1 / Q * y[1] - np.sin(y[0])      # y_2'(x) = A*cos(omega*x) - 1/Q *y_2(x) - sin(y_1(x))

    cases = [
        (2, 2 / 3, 0.5, 0.01, 0),
        (2, 2 / 3, 0, 0.3, 0),
        (2, 2 / 3, 1.35, 0.3, 0)
    ]

    plt.figure(figsize=(12, 8))
    for i, (Q, omega_hat, A_hat, theta0, omega0) in enumerate(cases):

        f_vector = [f1, lambda x, y: f2(x, y, A_hat=A_hat, omega_hat=omega_hat, Q=Q)]
        func = lambda x, y: np.array([f(x[i], y) for i, f in enumerate(f_vector)])

        initial_cond = [np.array([0, 0]), np.array([theta0, omega0])]
        t_max = 50
        dt = 0.01
        n = int(t_max / dt + 1)

        t_vals, y_vals = ode.runge_kutta_4th_order(func=func, point=initial_cond, h=dt, n=n)
        # t = list(map(t_vals, lambda vec: vec[0]))
        # theta = list(map(y_vals, lambda vec: vec[0]))

        tau = [vect[0] for vect in t_vals]
        theta = [vect[0] for vect in y_vals]

        dtheta_dtau = [vect[1] for vect in y_vals]

        plt.subplot(3, 2, 2 * i + 1)
        plt.plot(tau, theta)
        plt.xlabel(r"Czas $\tau$")
        plt.ylabel(r"$\Theta(\tau)$")
        plt.title(fr"Przypadek {i + 1}: $Q={Q}$," + r" $\hat{\omega}$=" +
                  f"{omega_hat:.3f}, " + r"$\hat{A}$" + f"={A_hat}, " +
                  r"$\hat{\Theta_0}$" + fr"={theta0}, $\omega_0$={omega0}")

        plt.subplot(3, 2, 2 * i + 2)
        plt.plot(theta, dtheta_dtau)
        plt.xlabel(r"$\Theta$")
        plt.ylabel(r"$\frac{d\Theta}{d\tau}$")
        plt.title(f"Wykresy fazowe dla przypadku {i + 1}")

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
