import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


def main():
    n = 1000
    b0 = 5
    b1 = 2
    M = 5000
    v = 5

    x = np.arange(0, 10, 1/(n-1))
    t_student = t(5)
    e = t_student.rvs(size=5)
    e = t.rvs(size=n, )
    print(e)





if __name__ == '__main__':
    main()
