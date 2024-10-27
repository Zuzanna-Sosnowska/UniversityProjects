import numpy as np
import matplotlib.pyplot as plt


def z1(x):
    return (6-2*x) / (6 + 4 * x + np.power(x, 2))


def z2(x):
    return (6 - 4 * x + np.power(x, 2)) / (6+2*x)


def plot1(x, z, z1, z2):
    plt.figure()
    plt.plot(x, z, 'b', label='rzeczywista wartość')
    plt.plot(x, z1, 'r', label='przybliżenie z1')
    plt.plot(x, z2, 'g', label='przybliżenie z2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'Porównanie przybliżenia Padego funkcji $e^{-x}$')
    plt.legend(loc='best')
    plt.savefig('przyblizenie_padego_1.png')
    plt.show()


def plot2(x, z, z1, z2):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    ax[0].plot(x, z1, c='g', label=r'$z_1$')
    ax[0].plot(x, z, c='cyan', label='rzeczywista wartość', linestyle='--')
    ax[0].legend(loc='best')
    ax[0].set_xlabel(r'x')
    ax[0].set_ylabel(r'y')
    ax[1].plot(x, z2, c='blue', label=r'$z_2$')
    ax[1].plot(x, z, c='cyan', label='rzeczywista wartość', linestyle='--')
    ax[1].legend(loc='best')
    ax[1].set_xlabel(r'x')
    ax[1].set_ylabel(r'y')

    # plot 2 subplots
    ax[0].set_title(r'Przybliżenie $z_1$')
    ax[1].set_title('Przybliżenie $z_2$')

    fig.suptitle(r'Porównanie przybliżeń Padego funkcji $e^{-x}$', size=20)
    fig.savefig('przyblizenia_padego_2.png')
    plt.show()


def plot3(x, z, z1, z2):
    z1 = np.abs(z-z1)
    z2 = np.abs(z-z2)
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 12))
    ax[0, 0].plot(x, z1, c='g')
    ax[0, 0].set_xlabel(r'x')
    ax[0, 0].set_ylabel(r'y')
    ax[1, 0].plot(x, z2, c='blue')
    ax[1, 0].set_xlabel(r'x')
    ax[1, 0].set_ylabel(r'y')

    z1 = z1 / z
    z2 = z2 / z

    ax[0, 1].plot(x, z1, c='cyan')
    ax[0, 1].set_xlabel(r'x')
    ax[0, 1].set_ylabel(r'y')
    ax[1, 1].plot(x, z2, c='blue')
    ax[1, 1].set_xlabel(r'x')
    ax[1, 1].set_ylabel(r'y')


    # plot 2 subplots
    ax[0, 0].set_title(r'Błąd bezwzględny $|z-z_1|$')
    ax[1, 0].set_title(r'Błąd bezwzględny $|z-z_2|$')
    ax[0, 1].set_title(r'Błąd względny $\frac{{{|z-z_1|}}}{{z}}$')
    ax[1, 1].set_title(r'Błąd względny $\frac{{{|z-z_2|}}}{{z}}$')

    fig.suptitle(r'Porównanie przybliżeń Padego funkcji $e^{-x}$', size=20)
    fig.savefig('przyblizenia_padego_3.png')
    plt.show()



if __name__ == '__main__':
    x = np.linspace(-1, 5, 10**4)
    z1 = z1(x)
    z2 = z2(x)
    z = np.exp(-x)

    # plot1(x, z, z1, z2)
    # plot2(x, z, z1, z2)
    plot3(x, z, z1, z2)
