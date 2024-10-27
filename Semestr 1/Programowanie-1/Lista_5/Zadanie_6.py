
def czy_posortowana(ls: [int]) -> bool:
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


if __name__ == '__main__':
    data = list(map(int, input("Wprowadź listę: ").split(" ")))
    print(czy_posortowana(data))
