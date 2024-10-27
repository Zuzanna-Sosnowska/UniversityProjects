class Vertes:
    def __init__(self):
        self.neighbours = []


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edges = {}

    def add_vertex(self, vert_key):
        if vert_key not in self.adj_list:
            self.adj_list[vert_key] = []

    def add_edge(self, from_key, to_key, weight):
        if (from_key in self.adj_list) and (to_key in self.adj_list):
            self.adj_list[from_key].append(to_key)
            self.edges[(from_key, to_key)] = weight

    def get_vertex(self, vert_key):
        pass

    def get_neighbors(self, vert_key):
        pass

    def get_vertices(self):
        pass

    def get_edges(self):
        pass

    def __contains__(self):
        pass


v = Graph()
v.add_vertex(1)
v.add_vertex(2)
v.add_edge(1, 2, 10)
