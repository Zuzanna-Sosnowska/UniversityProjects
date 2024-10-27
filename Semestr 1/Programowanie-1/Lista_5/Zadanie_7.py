
def czy_anagramy(slowo1: str, slowo2: str) -> bool:
    wszystkie_litery = slowo1 + slowo2
    slownik1: dict = {litera: 0 for litera in wszystkie_litery}
    slownik2: dict = {litera: 0 for litera in wszystkie_litery}

    for litera in slowo1:
        slownik1[litera] += 1
    for litera in slowo2:
        slownik2[litera] += 1

    for litera in wszystkie_litery:
        if slownik1[litera] != slownik2[litera]:
            return False
    return True


if __name__ == '__main__':
    s1 = input("Podaj słowo 1: ")
    s2 = input("Podaj słowo 2: ")
    print(czy_anagramy(s1, s2))
