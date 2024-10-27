import sys
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def SEIR_model(x, t, beta, sigma, gamma):
    s, e, i, r = x
    n = s + e + i + r
    dSdt = -(beta*s*i)/n
    dEdt = (beta*s*i)/n - sigma*e
    dIdt = sigma*e - gamma*i
    dRdt = gamma*i
    return [dSdt, dEdt, dIdt, dRdt]


def SEIR_plot(t_pocz, t_kon, step, x_pocz, arguments):
    t = np.linspace(t_pocz, t_kon, step)
    wynik = odeint(SEIR_model, x_pocz, t, args=arguments)
    plt.plot(t, wynik[:, 0])
    plt.plot(t, wynik[:, 1])
    plt.plot(t, wynik[:, 2])
    plt.plot(t, wynik[:, 3])
    plt.legend(["Suspectible", "Exposed", "Infected", "Recovered"], loc="lower right")
    plt.title("Rozwój epidemii wg modelu SEIR")
    plt.xlabel("Czas")
    plt.ylabel("Liczność populacji")
    plt.show()


if __name__ == '__main__':
    x_p = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    argumenty = float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8])
    SEIR_plot(0, 160, 161, x_p, argumenty)
