import random
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def sredniCzasWykonaiaSorted(dlugosc):
    czasSredni = 0
    for i in range(100):
        lista = [random.randint(-1000, 1000) for _ in range(dlugosc)]
        start = time.time()
        sorted(lista)
        end = time.time()
        czasSredni += end - start
    czasSredni /= 100
    return czasSredni


def test(x, a):
    return a*x*np.log(x)


def main():
    timeList = []  # lista czasów wykonania sorted od coraz dłuższych list
    numberOfTests = 10  # liczba iteracji pętli; liczba list
    x = np.array([(i+1) * 5000 for i in range(numberOfTests)])
    for i in range(numberOfTests):
        timeList.append(sredniCzasWykonaiaSorted((i+1) * 5000))  # średni czas sortowania takiej listy
        # dodajemy do listy czasów

    print(curve_fit(test, x, timeList))
    param, param_cov = curve_fit(f=test, xdata=x, ydata=timeList)
    ans = (param[0]*x*np.log(x))
    print(ans)

    plt.plot(x, timeList)
    plt.plot(x, ans)
    plt.legend(["Wykres", "Dopasowanie"])
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
