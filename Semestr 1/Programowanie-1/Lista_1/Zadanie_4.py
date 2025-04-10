import math

def obj_kuli():
    """
    Funkcja oblicza objętość kuli
    :return: Objętość kuli o zadanym promieniu
    """
    r = float(input("Podaj promien kuli:"))
    if r <= 0:
        print("Błąd, zły promień")
        return
    objetosc = 4/3 * math.pi * int(r)**3
    print("Objetosc kuli:", objetosc)


obj_kuli()