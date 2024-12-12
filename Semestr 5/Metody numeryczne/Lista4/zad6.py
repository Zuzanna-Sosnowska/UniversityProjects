import numpy as np
import zad2


def newton2(coef, x0, acc=1e-9):
    n = len(coef) - 1
    roots = []
    coef_0 = coef
    for _ in range(n):
        x, _ = zad2.newton(polynomial(coef), polynomial(der_coef(coef)), x0, acc)
        x, _ = zad2.newton(polynomial(coef_0), polynomial(der_coef(coef_0)), x, acc)
        roots.append(x)
        # coef = np.flip(np.polydiv(np.flip(coef), np.array([1, -x]))[0])
        coef, _ = polynom_div(coef, np.array([-x, 1]))
    return roots


def polynom_div(coeffs1, coeffs2):
    quotient = np.zeros(len(coeffs1) - len(coeffs2) + 1, dtype=complex)
    reminder = coeffs1.copy()
    for i in range(len(coeffs1) - 2, len(coeffs2) - 3, -1):
        multiplier = reminder[i + 1] / coeffs2[-1]
        quotient[i - len(coeffs2) + 2] = multiplier
        reminder[i + 1] = 0
        for j in range(len(coeffs2) - 2, -1, -1):
            reminder[i + j - len(coeffs2) + 2] -= multiplier * coeffs2[j]
    reminder.resize(len(coeffs2) - 1)
    return quotient, reminder


def der_coef(coef): return [coef[i] * i for i in range(1, len(coef))]


def polynomial(coef): return lambda x : sum(coef[i] * x ** i for i in range(len(coef)))


def main():
    coef = np.array([-84, 30 - 14j, -8 + 5j, 5 + 1j, 1])

    roots = newton2(coef, 0)
    print(roots)
    print([np.linalg.norm(polynomial(coef)(root)) for root in roots])


if __name__ == '__main__':
    main()