import networkx as nx
import matplotlib.pyplot as plt
import random
import os
import imageio


images = []

if not os.path.exists("C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_4\\Graph_picture"):
    os.makedirs("C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_4\\Graph_picture")


def create_random_graph(n=10, m=0.5):
    global pos
    g = nx.gnp_random_graph(n, m)
    color_map = []
    for node in g:
        if node < 1:
            color_map.append('red')
        else:
            color_map.append('blue')
    pos = nx.spring_layout(g)
    nx.draw(g, node_color=color_map, with_labels=True, pos=pos)
    path = f"./Graph_picture\\{0}.png"
    plt.savefig(path)
    plt.clf()
    images.append(imageio.v2.imread(path))
    return g


def walking_agent(graph, moves=10):
    agent_location = 0
    for i in range(moves):
        possible_path = []
        for edge in nx.edges(graph):
            if edge[0] == agent_location:
                possible_path.append(edge[1])
            elif edge[1] == agent_location:
                possible_path.append(edge[0])
        if len(possible_path) == 0:
            break
        random.shuffle(possible_path)
        agent_location = possible_path[0]
        color_map = []
        for node in graph:
            if node == agent_location:
                color_map.append('red')
            else:
                color_map.append('blue')
        nx.draw(graph, node_color=color_map, with_labels=True, pos=pos)
        path = f"./Graph_picture\\{i + 1}.png"
        plt.savefig(path)
        plt.clf()
        images.append(imageio.v2.imread(path))
    imageio.mimsave("./walking_agent.gif", images, duration=500)


g2 = create_random_graph()
walking_agent(g2)
