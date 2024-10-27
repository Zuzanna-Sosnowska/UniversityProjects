import math

def obj_kuli():
    r = int(input("Podaj promien kuli:"))
    if r <= 0:
        print("Błąd, zły promień")
        return
    objetosc = 4/3 * math.pi * int(r)**3
    print("Objetosc kuli:", objetosc)


obj_kuli()