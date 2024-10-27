import time


def fibbonaci(n: int) -> int:
    if n < 0:
        raise Exception("error")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonaci(n-1) + fibbonaci(n-2)


def wolny_fibbonaci(n: int) -> [int]:
    wynik = []
    for i in range(n + 1):
        wynik += [fibbonaci(i)]
    return wynik


if __name__ == '__main__':
    dane = int(input("Wprowadź n: "))

    t0 = time.monotonic()
    result = wolny_fibbonaci(dane)
    finish_time = time.monotonic() - t0

    print("Execution time: ", finish_time)
    print(result)
