import sympy as sp
import random


def extended_euclidean(a, b):
    """
    Zwraca (gcd, x, y) takie, że: a*x + b*y = gcd
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


def mod_inverse(e, phi):
    """
    Zwraca d takie, że (e * d) % phi == 1
    """
    gcd, x, _ = extended_euclidean(e, phi)
    if gcd != 1:
        raise Exception("Odwrotność nie istnieje")
    else:
        return x % phi


def generate_rsa_keys(p: int, q: int):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def choose_e(totient):
        while True:
            e = random.randrange(2, totient)
            if gcd(e, totient) == 1:
                return e

    n = p * q
    totient = (p - 1) * (q - 1)
    e = choose_e(totient)
    d = mod_inverse(e, totient)
    return n, e, d


def encrypt(n, e, m):
    return pow(m, e, n)


def decrypt(n, d, c):
    return pow(c, d, n)

if __name__ == '__main__':
    p = sp.randprime(10 ** 40, 2 * 10 ** 40)
    q = sp.randprime(10 ** 40, 2 * 10 ** 40)
    n, e, d = generate_rsa_keys(p, q)
    message = "Ala ma kota"
    print("Nadana wiadomość:", message)

    m = int(message.encode("utf-8").hex(), 16)

    c = encrypt(n, e, m)
    print("Szyfrogram w postaci liczby:", c)
    m = decrypt(n, d, c)
    print("Odszyfrowana wiadomość w postaci liczby:", m)

    tmp = hex(m)[2:]
    if len(tmp) % 2 == 1:
        tmp = "0" + tmp
    message = bytes.fromhex(tmp).decode("utf-8")
    print("Odszyfrowana wiadomość:", message)
