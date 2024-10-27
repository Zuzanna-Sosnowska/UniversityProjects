import random
import time

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def example1(S):
    """Return the sum of the elements in sequence S."""
    number_of_operations = 0
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
        number_of_operations += 1
    return number_of_operations


def example2(S):
    """Return the sum of the elements with even index in sequence S.
    """
    number_of_operations = 0
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
        number_of_operations += 1
    return number_of_operations


def example3(S):
    """Return the sum of the prex sums of sequence S."""
    number_of_operations = 0
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            number_of_operations += 1
            total += S[k]
    return number_of_operations


def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex
    sums in A."""
    number_of_operations = 0
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
                number_of_operations += 1
        if B[i] == total:
            count += 1
            number_of_operations += 1
    return number_of_operations


def czasWykonania(function, S):
    czasSredni = 0
    for i in range(100):
        start = time.time()
        function(S)
        end = time.time()
        czasSredni += end - start
    return czasSredni / 100


def czasWykonania2(function, A, B):
    czasSredni = 0
    for i in range(10):
        start = time.time()
        function(A, B)
        end = time.time()
        czasSredni += end - start
    return czasSredni / 10


def main():

    number_of_tests = 10
    time_of_operations_1 = []
    time_of_operations_2 = []
    time_of_operations_3 = []
    time_of_operations_4 = []

    for i in range(number_of_tests):
        S = [random.randint(-10, 10) for _ in range(i * 10**4)]
        time_of_operations_1.append(czasWykonania(example1, S))
        time_of_operations_2.append(czasWykonania(example2, S))
        print(i)

    plt.plot([_*10**4 for _ in range(number_of_tests)], time_of_operations_1, marker='o')
    plt.grid(True)
    plt.show()
    plt.plot([_*10**4 for _ in range(number_of_tests)], time_of_operations_2, marker='o')
    plt.grid(True)
    plt.show()

    plt.loglog([_ * 10 ** 4 for _ in range(number_of_tests)], time_of_operations_1, marker='o')
    plt.grid(True)
    plt.show()
    plt.loglog([_ * 10 ** 4 for _ in range(number_of_tests)], time_of_operations_2, marker='o')
    plt.grid(True)
    plt.show()

    for i in range(number_of_tests):
        S = [random.randint(-10, 10) for _ in range(i * 100)]
        time_of_operations_3.append(czasWykonania(example3, S))
        print(i)
    plt.plot([_*1000 for _ in range(number_of_tests)], time_of_operations_3, marker='o')
    plt.grid(True)
    plt.show()

    plt.loglog([_ * 1000 for _ in range(number_of_tests)], time_of_operations_3, marker='o')
    plt.grid(True)
    plt.show()

    for i in range(number_of_tests):
        A = [random.randint(-10, 10) for _ in range(i * 50)]
        B = [random.randint(-10, 10) for _ in range(i * 50)]
        time_of_operations_4.append(czasWykonania2(example4, A, B))
        print(i)
    plt.plot([_ * 50 for _ in range(number_of_tests)], time_of_operations_4, marker='o')
    plt.grid(True)
    plt.show()

    plt.loglog([_ * 50 for _ in range(number_of_tests)], time_of_operations_4, marker='o')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
