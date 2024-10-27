import random
import time
import math
import matplotlib.pyplot as plt

S = [random.randint(-100, 100) for _ in range(1000)]


def findMaximum(S):
    a = len(S)
    if a == 0:
        return -math.inf
    if a == 1:
        maximum = S[0]
        return maximum
    p = a // 2
    firstHalfMax = findMaximum(S[:p])
    secondHalfMax = findMaximum(S[p:])
    if firstHalfMax >= secondHalfMax:
        return firstHalfMax
    return secondHalfMax


def executionTime(function, lenght):
    averageTime = 0
    for i in range(10):
        S = [random.randint(-1000, 1000) for _ in range(lenght)]
        start = time.time()
        function(S)
        averageTime += time.time() - start
    return averageTime / 10


timeList = []
numberOfIter = 10
for i in range(numberOfIter):
    timeList.append(executionTime(findMaximum, i * 10))
print(timeList)
plt.plot([_*10 for _ in range(numberOfIter)], timeList)
# plt.grid(True)
plt.show()

print(S)
print(findMaximum(S))
