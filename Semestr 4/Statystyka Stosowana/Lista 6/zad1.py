import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np


def main():
    alpha = 0.05
    n = 12
    x_sr = 231.33
    s2 = 31.44
    q1 = stats.t.ppf(1 - alpha/2, 11)
    print(q1)


if __name__ == '__main__':
    main()
