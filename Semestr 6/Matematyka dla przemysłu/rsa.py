import numpy as np
import sympy as sp
import random


def gcd( a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_rsa_keys(p: int, q: int):
    n = p * q
    totient = (p - 1) * (q - 1)

    def choose_e(totient):
        while True:
            e = random.randrange(2, totient)
            if gcd(e, totient) == 1:
                return e

    e = choose_e(totient)



if __name__ == '__main__':
    print(sp.randprime(10, 20))