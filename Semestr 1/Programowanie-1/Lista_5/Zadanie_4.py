import time


def ciag_fibonacciego(n: int) -> [int]:
    if n < 0:
        return []
    wynik = [0, 1]
    for i in range(2, n):
        wynik += [wynik[i-2] + wynik[i-1]]
    return wynik


if __name__ == '__main__':
    data = int(input("Wprowadź n: "))

    t0 = time.monotonic()
    result = ciag_fibonacciego(data)
    time = time.monotonic() - t0

    print("Execution time: ", time)
    print(result)
