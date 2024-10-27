

def szybki_fibbonaci(n: int) -> [int]:
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    wynik = szybki_fibbonaci(n - 1)
    wynik += [wynik[n-2] + wynik[n-1]]
    return wynik