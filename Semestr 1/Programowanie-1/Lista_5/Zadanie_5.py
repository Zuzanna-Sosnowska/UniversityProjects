
def czy_palindrom(slowo: str) -> bool:
    slowo = slowo.lower().replace(" ", "")
    odwrocone = slowo[::-1]
    for i in range(len(slowo)):
        if slowo[i] != odwrocone[i]:
            return False
    return True


if __name__ == '__main__':
    data = input("Podaj słowo: ")
    print(czy_palindrom(data))
