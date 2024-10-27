import random
import os
import matplotlib.pyplot as plt
import time

S = [random.randint(-100, 100) for _ in range(101)]


def findMaximum(S):
    if len(S) == 1:
        maximum = S[0]
        return maximum
    firstHalfMax = findMaximum(S[:len(S)//2])
    secondHalfMax = findMaximum(S[len(S)//2:])
    if firstHalfMax >= secondHalfMax:
        return firstHalfMax
    return secondHalfMax


def maxAndMin(S):
    if len(S) == 1:
        max = min = S[0]
        return max, min
    firstHalf = maxAndMin(S[:len(S)//2])
    secondHalf = maxAndMin(S[len(S)//2:])
    if firstHalf[0] >= secondHalf[0]:
        if firstHalf[1] <= secondHalf[1]:
            return firstHalf
        return firstHalf[0], secondHalf[1]
    if firstHalf[1] <= secondHalf[1]:
        return secondHalf[0], firstHalf[1]
    return secondHalf


def prodOfMultipl(m, n, acc: int=0):
    if m == 0:
        return acc
    return prodOfMultipl(m-1, n, acc+n)


def palindrom(word):
    return len(word) <= 1 or word[0] == word[len(word)-1] and palindrom(word[1:len(word)-1])
    # if len(word) <= 1:
    #     return True
    # if word[0] == word[len(word)-1]:
    #     if palindrom(word[1:len(word)-1]):
    #         return True
    #     return False
    # return False


def find(path, filename, depth):
    if depth == 0:
        return []
    files = []
    for fileOrDir in os.listdir(path):
        fileOrDirPath = os.path.join(path, fileOrDir)
        if os.path.isdir(fileOrDirPath):
            files += find(fileOrDirPath, filename, depth - 1)
        elif fileOrDir == filename:
            files.append(fileOrDirPath)
    return files


def find2(path, filename):
    result = []
    for root, dirs, files in os.walk(path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


def executionTime(function, lenght):
    averageTime = 0
    for i in range(100):
        S = [random.randint(-1000, 1000) for _ in range(lenght)]
        start = time.time()
        function(S)
        end = time.time()
        averageTime += end - start
    return averageTime / 100


def main():

    # print(find("C:\\Users\\Zuzia\\PycharmProjects", "zad1.py", 3))
    # print(find2("C:\\Users\\Zuzia\\PycharmProjects", "zad1.py"))
    print(S)
    print(findMaximum(S))
    print(maxAndMin(S))

    timeList = []
    numberOfIter = 50
    for i in range(50):
        timeList.append(executionTime(findMaximum, i* 1000))

    plt.plot([_*1000 for _ in range(numberOfIter)], timeList)
    plt.grid(True)
    plt.show()

    #
    # print(palindrom("kobyłamamałybok"))
    # print(palindrom("akacja"))

