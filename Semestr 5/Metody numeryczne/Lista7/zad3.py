import numpy as np
import matplotlib.pyplot as plt
import differential_equations as ode


def main():
    def runge_kutta(f, theta, omega, h, c):
        k1_theta = h * omega
        k1_omega = h * f(theta, omega, c)

        k2_theta = h * (omega + k1_omega / 2)
        k2_omega = h * f(theta + k1_theta / 2, omega + k1_omega / 2, c)

        k3_theta = h * (omega + k2_omega / 2)
        k3_omega = h * f(theta + k2_theta / 2, omega + k2_omega / 2, c)

        k4_theta = h * (omega + k3_omega)
        k4_omega = h * f(theta + k3_theta, omega + k3_omega, c)

        theta += (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
        omega += (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega) / 6

        return theta, omega