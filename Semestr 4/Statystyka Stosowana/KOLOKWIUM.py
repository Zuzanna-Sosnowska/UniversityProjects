import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def rozklad_f(theta, n=1000):
    """
    Funkcja zwraca n realizacji zmiennej losowej o rozkładzie zadanym gęstością f
    :param theta: parametr funkcji f
    :param n: liczba realizacji
    :return: tablica w wartościami zmiennych losowych o rozkładzie zadanym gęstością f
    """
    u = np.random.uniform(0, 1, n)
    return np.power(u, 1/(2*theta+1))


def theor_distr(theta, n=1000):
    '''
    Funkcja zwraca listy x, y potrzebne do generowania wykresu dystrybuanty
    :param theta: parametr funkcji F
    :param n: liczba punktów w których obliczana jest wartość dystrybuanty. Możemy interpretować jako dokładność
    :return: lista x i odpowiadająca jej lista wartości funkcji F(x)
    '''
    x = np.linspace(0, 1, n)
    y = np.power(x, 2*theta + 1)
    return x, y


def theor_density(theta, n=1000):
    '''
    Funkcja zwraca listy x, y potrzebne do generowania wykresu gęstości
    :param theta: parametr funkcji f
    :param n: liczba punktów na które podzielimy odcinek [0, 1]. Możemy interpretować jako dokładność
    :return:  lista x i odpowiadająca jej lista wartości funkcji f(x)
    '''
    x = np.linspace(0, 1, n)
    y = (2*theta + 1) * np.power(x, 2*theta)
    return x, y


def theta_estimation(x):
    '''
    Funkcja zwraca estymator parametru theta, wyznaczony metodą momentów, w zależności od danych x z próby
    :param x: dane z próby losowej
    :return: wartość estymatora dla próby x
    '''
    return 1/(2 * (1 - (np.sum(x)/len(x)))) - 1


def theor_max_distr(theta, n=1000):
    '''
    Funkcja zwraca listę x i odpowiadającą jej listę wartości dystrybuanty F(x) w odpowiednich punktach
    :param theta: parametr funkcji F
    :param n: podział odcinka na n części - im większe n, tym bardziej dokładny będzie wykres
    :return: listę x i listę odpowiadających jej wartości F(x)
    '''
    x = np.linspace(0.99, 1, n)
    y = np.power(np.power(x, 2*theta + 1), n)
    return x, y


def theor_max_density(theta, n=1000):
    x = np.linspace(0.99, 1, n)
    y = n * np.power(np.power(x, 2*theta + 1), n-1) * (2*theta + 1) * np.power(x, 2*theta)
    return x, y


def main():
    theta = 2
    n = 1000

    u = rozklad_f(theta, n)
    x1, y1 = theor_distr(theta, n)
    x2, y2 = theor_density(theta, n)

    # Porównanie dystrybuant

    sns.ecdfplot(u, label="Empiryczna")
    plt.plot(x1, y1, label="Teoretyczna")
    plt.title("Porównanie dystrybuant")
    plt.legend()
    plt.show()

    # Porównanie gęstości

    plt.hist(u, density=True, label="Empiryczna")
    plt.plot(x2, y2, 'r', label="Teoretyczna")
    plt.title("Porównanie gęstości")
    plt.legend()
    plt.show()

    # Podpunkt c)

    theta_list = np.zeros(n)
    for i in range(1, n):
        u = rozklad_f(theta, n)
        theta_list[i-1] = theta_estimation(u)

    plt.scatter(np.linspace(0, n, n), theta_list, label='Wartość estymatora dla n-tej próby długości 1000')
    plt.axhline(y=theta, color='r', linestyle='--', label=r'Rzeczywista wartość parametru $\theta$')
    plt.title('Testowanie poprawności estymatora \n wyznaczonego metodą momentów')
    plt.legend()
    plt.xlabel('Numer próby')
    plt.ylabel('Wartość estymatora')
    plt.show()

    # Testowanie skuteczności estymatora

    theta_list = np.zeros(n - 1)
    for i in range(1, n):
        u = rozklad_f(theta, i * 50)
        theta_list[i - 1] = theta_estimation(u)

    plt.scatter(np.linspace(1, 50 * n, n - 1), theta_list, label='Wartość estymatora dla próby długości n')
    plt.axhline(y=theta, color='r', linestyle='--', label=r'Rzeczywista wartość parametru $\theta$')
    plt.title('Testowanie poprawności estymatora \n wyznaczonego metodą momentów')
    plt.legend()
    plt.xlabel('Długość próby')
    plt.ylabel('Wartość estymatora')
    plt.show()

    # Podpunkt e)

    m = 1000

    u_max = np.zeros(m)
    for i in range(m):
        u = rozklad_f(theta, n)
        u_max[i] = np.max(u)

    x, y = theor_max_distr(theta, n)
    a, b = theor_max_density(theta, n)

    sns.ecdfplot(u_max, label="Empiryczna")
    plt.plot(x, y, label="Teoretyczna")
    plt.title(r"Porównanie dystrybuant statystyki $U_{max}$")
    plt.legend()
    plt.show()

    plt.hist(u_max, label="Empiryczna")
    plt.plot(a, b, label="Teoretyczna")
    plt.title(r"Porównanie gęstości statystyki $U_{max}$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
