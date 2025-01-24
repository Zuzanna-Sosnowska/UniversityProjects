import numpy as np


def bisection(f, a, b, accuracy=1.0e-9)->tuple:
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja nie zmienia znaku na podanym przedziale.")
    counter = 0
    while np.abs(b - a) / 2 > accuracy:
        c = a + 0.5 * (b - a)
        if f(c) == 0:
            print(counter)
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        counter += 1
    print(counter)
    return (a + b) / 2


def bisection2(f,x1,x2,tol=1.0e-9):
    f1 = f(x1)
    f2 = f(x2)
    if f1 == 0.0: return x1
    if f2 == 0.0: return x2
    if np.sign(f1) == np.sign(f2):
        raise ValueError('Wrong x1 and x2')
    # Obliczanie liczby iteracji potrzebnej do uzyskania żądanej dokładności
    n = int(np.ceil(np.log(abs(x2 - x1)/tol)/np.log(2.0)))
    for i in range(n):
        x3 = 0.5*(x1 + x2)
        f3 = f(x3)
        if abs(f3) > abs(f1) and abs(f3) > abs(f2):
            return None
        if f3 == 0.0:
            return x3
        if np.sign(f2)!= np.sign(f3):
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3
    return (x1 + x2) / 2.0, n


def brent(f, a, b, tol=1.0e-9, max_iter=2000):
    """
    Metoda Brenta do znajdowania pierwiastków funkcji f na przedziale [a, b].
    :param f: Funkcja, której pierwiastek szukamy
    :param a: Początek przedziału
    :param b: Koniec przedziału
    :param tol: Dokładność rozwiązania
    :param max_iter: Maksymalna liczba iteracji
    :return: Przybliżony pierwiastek
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja nie zmienia znaku na podanym przedziale.")

    fa = f(a)
    fb = f(b)
    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c = a
    fc = fa
    s = b
    fs = fb
    d = b - a
    e = b - a

    counter = 0

    for iteration in range(max_iter):
        if fb != fc and fa != fc:
            s = (a * fb * fc / ((fa - fb) * (fa - fc)) +
                 b * fa * fc / ((fb - fa) * (fb - fc)) +
                 c * fa * fb / ((fc - fa) * (fc - fb)))
        else:
            s = b - fb * (b - a) / (fb - fa)

        if not ((3 * a + b) / 4 < s < b or (b < s < (3 * a + b) / 4)):
            s = (a + b) / 2
        if abs(s - b) < tol:
            print(counter)
            return s

        fs = f(s)
        d, e = e, d

        if fs * fb < 0:
            a = b
            fa = fb
        else:
            fa /= 2

        b = s
        fb = fs

        if abs(fb) < tol:
            print(counter)
            return b
        counter += 1
    raise RuntimeError("Metoda Brenta nie zbiega w zadanej liczbie iteracji.")


def newton(f, df, x0, tol=1.0e-9):
    if f(x0) == 0.0:
        return x0
    counter = 0
    while abs(f(x0)) > tol:
        x0 = x0 - f(x0)/df(x0)
        counter += 1
    print(counter)
    return x0


def secant_method(f, x0, x1, tol=1.0e-9, max_iter=2000):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            raise ZeroDivisionError("Function values at x0 and x1 resulted in division by zero.")
        x_new = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        x0 = x1
        x1 = x_new
        if np.abs(f(x_new)) < tol:
            return float(x_new), i
    raise ValueError("Secant method did not converge within the maximum number of iterations.")


def main():
    def f(x): return np.tan(np.pi - x) - x
    def df(x): return - 1 / np.power(np.cos(np.pi - x), 2) - 1

    print(bisection(f, 2, 2.5))
    print(bisection2(f, 2, 2.5))
    print(brent(f, 2, 2.1))
    print(secant_method(f, 3, 3.5))
    # print(newton(f, df, 2))



if __name__ == '__main__':
    main()
