import matplotlib.pyplot as plt
import numpy as np


# poddaje sie

def psy_pchly(n=100, k=100, p=0.5):
    x = np.zeros(n)
    dog_1 = [n]
    dog_2 = [0]
    for j in range(k):
        for i in range(n):
            if np.random.random() < p:
                x[i] = 1 - x[i]
