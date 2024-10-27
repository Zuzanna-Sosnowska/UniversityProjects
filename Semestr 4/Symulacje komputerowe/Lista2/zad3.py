import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def discrete_distribution(x_list, prob_list, n=1):
    if sum(prob_list) != 1:
        raise ValueError("Lista prawdopodobieństw nie sumuje się do 1!")
    if len(x_list) != len(prob_list):
        raise ValueError("Listy różnych długości")
    u = np.random.uniform(0, 1, n)
    x = np.zeros(n)
    for i in range(n):
        a = 0
        c = 0
        while u[i] >= a:
            a += prob_list[c]
            c += 1
            print(c)
        x[i] = x_list[c-1]
    return x


def discrete_dist(x_list, prob_list):
    if sum(prob_list) != 1:
        raise ValueError("Lista prawdopodobieństw nie sumuje się do 1!")
    if len(x_list) != len(prob_list):
        raise ValueError("Listy różnych długości")
    y = np.zeros(len(prob_list))
    x_to_prob_list = list(zip(x_list, prob_list))
    x_to_prob_list_sorted = sorted(x_to_prob_list, key=lambda q: q[0])
    val = 0
    for i in range(len(prob_list)):
        val += x_to_prob_list_sorted[i][1]
        y[i] = val
    return np.sort(x_list), y


def main():
    x_list = [2, -1, 3, 7]
    prob_list = [0.01, 0.7, 0.1, 0.19]

    a = discrete_distribution(x_list, prob_list, 1000)
    x, y = discrete_dist(x_list, prob_list)

    sns.ecdfplot(a)
    for i in range(len(prob_list) - 1):
        plt.scatter(x[i], y[i], color='g')
        plt.plot([x[i], x[i + 1]], [y[i], y[i]], color='g')
        plt.scatter(x[i + 1], y[i], facecolors='none', color='g')
    plt.show()


if __name__ == '__main__':
    main()


