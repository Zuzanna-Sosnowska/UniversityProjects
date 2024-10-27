import numpy as np
import math


class Vector:
    """
    Metoda __init__ zwróci nam obiekt składający się z k zer
    """
    def __init__(self, k=3):
        self.size = k
        self.arr = np.zeros(k)


    def from_list(self, ls):
        '''Metoda from_list zamieni nam listę podaną jako argument na obiekt klasy Vector'''
        if self.size != len(ls):
            raise ValueError
        self.arr = np.array(ls)


    def random_vector(self, a=0, b=100):
        '''
        Metoda random_vector umożliwia stworzenie wektora o losowych współrzędnych
        '''
        self.arr = np.random.uniform(a, b, self.size)

    def __add__(self, other):
        '''
        Metoda __add__ sumuje dwa wektory.
        Metoda zwróci ValueError jeśli długości wektorów nie będą sobie równe.
        '''
        if self.size != other.size:
            raise ValueError
        else:
            result = Vector(self.size)
            result.arr = self.arr + other.arr
            return result.arr

    def __sub__(self, other):
        '''
        Metoda __sub__ (subtract) odejmuje wektory.
        Metoda zwróci ValueError jeśli długości wektorów nie będą sobie równe.
        '''
        if self.size != other.size:
            raise ValueError
        else:
            result = Vector(self.size)
            result.arr = self.arr - other.arr
            return result.arr

    def multiply(self, p):
        '''
        Metoda multiply umożliwia pomnożenie wektora przez skalar p
        '''
        self.arr = self.arr*p
        return self.arr

    def length(self):
        '''
        Metoda lenght umożliwia obliczenie długości wektora, zgodnie ze wzorem:
        długość wektora = pierwiastek z sumy kwadratów współrzędnych wektora
        '''
        k = 0.0
        for i in range(self.size):
            k += (self.arr[i]) ** 2
        return math.sqrt(k)

    def sum(self):
        '''
        Metoda sum zwraca sumę wszystkich elementów wektora (sumuje w pętli kolejne elemety z tablicy)
        '''
        p = 0.0
        for i in range(self.size):
            p += self.arr[i]
        return p

    def scalar_product(self, other):
        '''
        Metoda scalar_product zwraca wynik iloczynu skalarnego dwóch wektorów (obiektów klasy Vector) zadanych jako argument.
        Metoda zwróci ValueError jeśli długości wektorów nie będą sobie równe.
        '''
        if self.size != other.size:
            raise ValueError
        else:
            r = 0.0
            for i in range(self.size):
                r += self.arr[i] * other.arr[i]
            return r

    def __str__(self):
        '''
        Metoda __str__ zwróci nam obiekt jako "vector: [tablica, składająca się z k elementów]"
        '''
        return "vector: " + str(self.arr)

    def __getitem__(self, index:int):
        '''
        Metoda __getitem__ zwraca element z tablicy o indeksie zadanym jako parametr "index" w funkcji
        '''
        return self.arr[index]

    def __contains__(self, item):
        '''
        Metoda __contains__ sprawdza, czy dany element (zadany jeko parametr "item") znajduje się w tablicy
        '''
        return item in self.arr


if __name__ == '__main__':
    v = Vector(5)
    print("Metoda __init__: ", v)
    u = Vector(5)
    u.from_list([1, 2, 3, 4, 5])
    print("Metoda from_list: ", u)
    v.random_vector(-5, 5)
    print("Metoda random_vector zamieni nasz wektor v na : ", v)
    print("Metoda __add__ zsumuje nam wektor u i wektor v : ", u + v)
    print("Metoda __sub__ odejmie od wektora u wektor v : ", u - v)
    print("Metoda multiply pomnoży wektor v przez skalar (np.4) ", v.multiply(4))
    print("Metoda scalar_product zwróci nam produkt skalarny iloczynu wektorów u i v: ", u.scalar_product(v))
    print("Metoda lenght zmierzy nam długość wektora u : ", u.length())
    print("Metoda sum zsumuje nam elementy wektora u: ", u.sum())
    print("Metoda get_item zwróci nam element wektora u na 3 pozycji: ", u.__getitem__(3))
    print("Metoda __contains__ sprawdzi, czy liczba 4 znajduje się w wektorze u: ", u.__contains__(4))

