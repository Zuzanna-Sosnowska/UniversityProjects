import cmath as mt


def rownanie_kwadratowe(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta == 0:
        return ((-b / 2 * a), (-b / 2 * a))
    else:
        p_z_delty = mt.sqrt(delta)
        return ((-b - p_z_delty) / 2 * a), ((-b + p_z_delty) / 2 * a)


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

rozw1, rozw2 = rownanie_kwadratowe(a, b, c)

print(f"rozwiazanie 1: {rozw1} \nrozwiazanie 2: {rozw2}")




