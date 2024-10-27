import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    N = 10 ** 3
    a = [0.2, 0.3, 0.5, 0.7, 0.8]
    c = []
    for j in a:
        p = j
        G = nx.erdos_renyi_graph(N, p)
        # nx.draw(G)
        # plt.show()

        # x = []
        # for node in G.nodes():
        #     x.append(G.degree(node))

        # sns.distplot(x)
        # plt.title(f'Rozkład stopni wierzchołków w grafie dla p = {p}')
        # plt.show()

        y = []
        for node in G.nodes():
            y.append(nx.clustering(G, node))

        c.append(np.sum((y - np.sum(y) / N) ** 2))
        print(j)
        # sns.distplot(y)
        # plt.title(f'Rozkład współczynników gronowania dla p = {p}')
        # plt.show()

    plt.scatter(a, c)
    plt.show()


if __name__ == '__main__':
    # main()
    my_file = open("facebook_combined.txt", "r")
    x = []
    for line in my_file:
        x.append(my_file.readline().replace('\n', '').split(" "))
    print(x)
