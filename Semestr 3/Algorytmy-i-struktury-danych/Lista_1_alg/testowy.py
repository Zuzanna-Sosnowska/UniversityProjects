import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def czasWykonaniaSorted(lista):
    czas = 0
    for i in range(10):
        start = time.time()
        sorted(lista)
        end = time.time()
        czas += end - start
    return czas / 10


def main():
    lista_czasow = []
    for i in range(100):
        lista = [p * 5000 for p in range(i)]
        lista_czasow.append(czasWykonaniaSorted(lista))




