from queue import Queue, PriorityQueue


class Edge:
    def __init__(self, fromVtx, toVtx, weight):
        self.fromVtx = fromVtx
        self.toVtx = toVtx
        self.weight = weight

    def __str__(self):
        if self.weight != 0:
            return f"{self.fromVtx} -> {self.toVtx} [ label = \"{self.weight}\" ];"
        else:
            return f"\"{self.fromVtx}\" -> \"{self.toVtx}\";"


class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}

    def __str__(self):
        return str(self.id)

    def __lt__(self, other):
        return self.id < other.id

    def hasNeighbor(self, nbr):
        return nbr in self.getNeighbors()

    def getNeighbors(self):
        return self.connectedTo.keys()

    def addNeighbour(self, nbr):
        self.addEdge(nbr, 0)

    def addEdge(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def getEdge(self, nbr):
        if self.hasNeighbor(nbr):
            return Edge(self, nbr, self.getWeight(nbr))

    def getEdges(self):
        return [self.getEdge(nbr) for nbr in self.getNeighbors()]

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def __getitem__(self, vertId):
        return self.getVertex(vertId)

    def __str__(self):
        graphStr = "digraph G {\n"
        for vert in self.getVertexes():
            for edge in vert.getEdges():
                graphStr += str(edge) + "\n"
        graphStr += "}"
        return graphStr

    def addVertex(self, vertId):
        if vertId not in self:
            newVertex = Vertex(vertId)
            self.vertList[vertId] = newVertex
            return newVertex
        else:
            return self.getVertex(vertId)

    def getVertex(self, vertId):
        if vertId in self.vertList:
            return self.vertList[vertId]
        else:
            return None

    def getNumberOfVertexes(self):
        return len(self.vertList)

    def addEdge(self, fromVertId, toVertId, weight=0, bidirectional=False):
        if (fromVertId in self.vertList) and (toVertId in self.vertList):
            self.vertList[fromVertId].addEdge(self.vertList[toVertId], weight)
            if bidirectional:
                self.vertList[toVertId].addEdge(self.vertList[fromVertId], weight)

    def getNeighbors(self, vertId):
        if vertId in self.vertList:
            return self.vertList[vertId].getNeighbors()
        return []

    def getVertIds(self):
        return self.vertList.keys()

    def getVertexes(self):
        return self.vertList.values()

    def getEdges(self):
        return [e for sub in [v.getEdges() for v in self.getVertexes()] for e in sub]

    def traverseDFS(self, startVertId):
        traversalOrder = []
        visited = set()

        def recDFS(vertex: Vertex):
            visited.add(vertex.id)
            traversalOrder.append(vertex.id)

            for vertNeighbour in vertex.getNeighbors():
                if vertNeighbour.id not in visited:
                    recDFS(vertNeighbour)

        recDFS(self.getVertex(startVertId))
        return traversalOrder

    def topologicalOrdering(self):
        topologicalOrder = []
        visited = set()

        def recTopologicalOrd(vertex: Vertex):
            visited.add(vertex.id)

            for vertNeighbour in vertex.getNeighbors():
                if vertNeighbour.id not in visited:
                    recTopologicalOrd(vertNeighbour)
                elif vertNeighbour.id not in topologicalOrder:
                    raise Exception('Graf zawiera cykl!')

            topologicalOrder.append(vertex.id)

        for vertex in self.vertList:
            if vertex not in visited:
                recTopologicalOrd(self.getVertex(vertex))

        return list(reversed(topologicalOrder))

    def traverseBFS(self, startVertId):
        traversalOrder = []
        visited = set()

        queue = Queue()
        queue.put(self.getVertex(startVertId))

        while not queue.empty():
            vertex = queue.get()
            if vertex.id not in visited:
                traversalOrder.append(vertex.id)
                visited.add(vertex.id)

                for vertNeighbour in vertex.getNeighbors():
                    queue.put(vertNeighbour)
        return traversalOrder

    def dijkstraSP(self, startVertId):
        shortestPaths = {}
        visited = set()

        queue = PriorityQueue()
        queue.put((0, self.getVertex(startVertId)))

        while not queue.empty():
            (path, vertex) = queue.get()
            if vertex.id not in visited:
                shortestPaths[vertex.id] = path
                visited.add(vertex.id)

                for vertEdge in vertex.getEdges():
                    vertNeighbour = vertEdge.toVtx
                    pathToNeighbour = path + vertEdge.weight
                    queue.put((pathToNeighbour, vertNeighbour))
        return shortestPaths


def getTestCaseGraph(bidirectional=True):
    g = Graph()
    for v in "SABCDEFGHI":
        g.addVertex(v)
    g.addEdge('S', 'A', 1, bidirectional)
    g.addEdge('S', 'D', 3, bidirectional)
    g.addEdge('S', 'E', 2, bidirectional)
    g.addEdge('S', 'F', 4, bidirectional)
    g.addEdge('A', 'B', 2, bidirectional)
    g.addEdge('A', 'C', 3, bidirectional)
    g.addEdge('B', 'G', 6, bidirectional)
    g.addEdge('G', 'I', 1, bidirectional)
    g.addEdge('C', 'G', 2, bidirectional)
    g.addEdge('C', 'D', 2, bidirectional)
    g.addEdge('D', 'H', 5, bidirectional)
    g.addEdge('E', 'F', 1, bidirectional)
    return g


def graph1():
    g = Graph()
    for v in "ABCDEFH":
        g.addVertex(v)
    g.addEdge('A', 'B')
    g.addEdge('C', 'B')
    g.addEdge('A', 'D')
    g.addEdge('B', 'D')
    g.addEdge('D', 'E')
    g.addEdge('D', 'H')
    g.addEdge('E', 'F')
    g.addEdge('F', 'H')
    return g


def graph2():
    g = Graph()
    for v in "ABCDEFG":
        g.addVertex(v)
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('B', 'C')
    g.addEdge('C', 'D')
    g.addEdge('B', 'F')
    g.addEdge('G', 'B')
    g.addEdge('G', 'F')
    g.addEdge('F', 'D')
    g.addEdge('F', 'E')

    return g


def graph3():
    g = Graph()
    for v in "ABCDEF":
        g.addVertex(v)
    g.addEdge('A', 'B')
    g.addEdge('B', 'D')
    g.addEdge('A', 'D')
    g.addEdge('D', 'E')
    g.addEdge('E', 'B')
    g.addEdge('B', 'C')
    g.addEdge('E', 'F')
    g.addEdge('F', 'C')

    return g


# graph = graph2()
# print(graph)
# print(graph.topologicalOrdering())


def cannibalAndMissionaries(cannibals=3, missionaries=3, boat=2):
    g = Graph()
    for i in range(cannibals + 1):
        for j in range(i, missionaries + 1):
            for k in range(0, cannibals - i + 1):
                for l in range(0, missionaries - j + 1):
                    if 1 <= k + l <= boat and missionaries-l-j >= cannibals-k-i:
                        g.addVertex(((i, j), (cannibals-k-i, missionaries-l-j), 'r'))
                        g.addVertex(((i, j), (cannibals-k-i, missionaries-l-j), 'l'))
    g.addVertex(((cannibals, missionaries), (0, 0), 'l'))

    for vertex in g.getVertexes():
        id = vertex.getId()
        if id[2] == 'r':
            i = id[0][0]
            j = id[0][1]
            for k in range(0, cannibals - i + 1):
                for l in range(0, missionaries - j + 1):
                    if 1 <= k+l <= boat and missionaries-l-j >= cannibals-k-i:
                        vertex.addNeighbour(g.getVertex(((i,j), (cannibals-k-i, missionaries-l-j), 'l')))
        else:
            i = id[1][0]
            j = id[1][1]
            for k in range(0, cannibals - i + 1):
                for l in range(0, missionaries - j + 1):
                    if 1 <= k+l <= boat and missionaries - l - j >= cannibals - k - i:
                        vertex.addNeighbour(g.getVertex(((cannibals - k - i, missionaries - l - j), (i, j), 'r')))

    traversalOrder = []
    visited = set()
    previous = {}

    starting_vertex = g.getVertex(((cannibals, missionaries), (0, 0), 'l'))
    queue = Queue()
    queue.put((starting_vertex, None))

    while not queue.empty():
        vertex, p = queue.get()
        if vertex.id not in visited:
            previous[vertex.id] = p
            if vertex.id[0] == (0, 0):
                path = [vertex.id]
                v = previous[vertex.id]
                while v is not None:
                    path.append(v.id)
                    v = previous[v.id]
                return list(reversed(path))

            traversalOrder.append(vertex.id)
            visited.add(vertex.id)

            for vertNeighbour in vertex.getNeighbors():
                queue.put((vertNeighbour, vertex))


def canisterProblem(canister1, canister2, liters):
    g = Graph()
    for i in range(canister1+1):
        for j in range(canister2+1):
            g.addVertex((i, j))

    for vertex in g.getVertexes():
        Id = vertex.getId()
        vertex.addNeighbour(g.getVertex((0, Id[1])))
        vertex.addNeighbour(g.getVertex((Id[0], 0)))
        vertex.addNeighbour(g.getVertex((canister1, Id[1])))
        vertex.addNeighbour(g.getVertex((Id[0], canister2)))
        if canister1 - Id[0] >= Id[1]:
            vertex.addNeighbour(g.getVertex((Id[0]+Id[1], 0)))
        else:
            vertex.addNeighbour(g.getVertex((canister1, Id[1] - (canister1 - Id[0]))))
        if canister2 - Id[1] >= Id[0]:
            vertex.addNeighbour(g.getVertex((0, Id[0]+Id[1])))
        else:
            vertex.addNeighbour(g.getVertex((Id[0] - (canister2 - Id[1]), canister2)))

    traversalOrder = []
    visited = set()
    previous = {}

    queue = Queue()
    queue.put((g.getVertex((0, 0)), None))

    while not queue.empty():
        vertex, p = queue.get()
        if vertex.id not in visited:
            previous[vertex.id] = p
            if vertex.id[0] == liters or vertex.id[1] == liters:
                path = [vertex.id]
                v = previous[vertex.id]
                while v is not None:
                    path.append(v.id)
                    v = previous[v.id]
                return list(reversed(path))

            traversalOrder.append(vertex.id)
            visited.add(vertex.id)

            for vertNeighbour in vertex.getNeighbors():
                queue.put((vertNeighbour, vertex))


print(canisterProblem(9, 6, 1))
#print(cannibalAndMissionaries())
