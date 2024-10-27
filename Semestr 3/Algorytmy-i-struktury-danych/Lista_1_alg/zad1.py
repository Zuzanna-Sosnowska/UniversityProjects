import random

polynom = [random.randint(-10, 10) for _ in range(5000)]


def polynomialValue1(polynomial, x):
    value = 0
    for i in range(len(polynomial)):
        y = 1
        for j in range(i):
            y *= x
        value += polynomial[i] * y
    return value


print(polynomialValue1([1, 1, 1, 1, 1, 1, 1], 2))
print(polynom)
print(polynomialValue1(polynom, 0.1))


def fastExponentianation(x, power):
    y = x
    potega = 1
    while power > 0:                    # operację wykonujemy do czasu aż x będzie potęgowany do 0
        if power % 2 == 1:              # jeśli potęga jest nieparzysta to wymnażamy przez y
                potega *= y
        power //= 2                     # dzielimy całkowicie potęgę przez 2
        y *= y                          # podnosimy y do kwadratu
    return potega


def polynomialValue2(polynomial, x):
    wynik = 0
    for i in range(len(polynomial)):
        wynik += polynomial[i] * fastExponentianation(x, i)
    return wynik


print(polynomialValue2([1, 1, 1, 1, 1, 1, 1], 2))
print(polynomialValue2(polynom, 0.1))


def polynomialValue3(polynomial, x):
    wynik = 0
    for i in range(len(polynomial)):
        wynik *= x
        wynik += polynomial[len(polynomial) - i - 1]    # dodajemy współczynniki od końca tablicy
    return wynik


print(polynomialValue3([1, 1, 1, 1, 1, 1, 1], 2))
print(polynomialValue3(polynom, 0.1))
