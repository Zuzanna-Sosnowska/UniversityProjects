import ctypes  # tablice niskopoziomowe
import time
import matplotlib.pyplot as plt


class DynamicArray:

    def __init__(self):
        self._n = 0  # liczba elementów
        self._capacity = 1  # rozmiar tablicy
        self._A = self._make_array(self._capacity)  # właściwa tablica

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


    def insert(self, k, value):
        if not 0 <= k <= self._n:
            raise IndexError('invalid index')
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i, self._n-1):
                    self._A[j] = self._A[j+1]
                self._n -= 1
                return

    def expand(self, seq):
        if self._n + len(seq) > self._capacity:
            self._resize(2 * (self._n + len(seq)))
        for i in range(0, len(seq)):
            self._A[self._n + i] = seq[i]
        self._n += len(seq)

    def __str__(self):
        result = "|"
        for i in range(self._n):
            result += self._A[i] + "|"
        for i in range(self._n, self._capacity):
            result += " |"
        return result


a = DynamicArray()
print(a)
a.expand(['a', 'd', 'b', 'c', 'd'])
a.remove('d')
a.expand(['f', 'g', 'h', 'i'])
print(a)
a.insert(4, 'e')
print(a)


def sumOfListOfList(list_of_list):
    result = 0
    for a in list_of_list:
        for b in a:
            result += b
    return result


# print(sumOfListOfList([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def testAppend(l1, l2, n):
    avg_time = 0
    for _ in range(n):
        start = time.time()
        for a in l2:
            l1.append(a)
        avg_time += time.time() - start
    return avg_time / n


def testExtend(l1, l2, n):
    avg_time = 0
    for _ in range(n):
        start = time.time()
        l1.extend(l2)
        avg_time += time.time() - start
    return avg_time / n


def experiment4():
    N = 1
    n = 1
    time_append = []
    time_extend = []
    for i in range(n):
        l2 = [0] * i
        time_append.append(testAppend(l2, l2, N))
        time_extend.append(testExtend(l2, l2, N))
    plt.plot([i for i in range(n)], time_append)
    plt.plot([i for i in range(n)], time_extend)
    plt.show()


experiment4()