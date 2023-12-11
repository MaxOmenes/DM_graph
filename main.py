import sys


class Graph:

    class Edge:
        def __init__(self, node1, node2, weight):
            self.node1 = node1
            self.node2 = node2
            self.weight = weight

        def get_weight(self, node):
            if node != self.node1 or node != self.node2:
                return -1
            return self.weight

        def get_neighbour(self, node):
            if (node != self.node1) and (node != self.node2):
                return -1

            if node == self.node1:
                return self.node2
            return self.node1

    def __init__(self):
        self.graph = []
        self.vertex = []

    def add_edge(self, node1, node2, value):
        self.graph.append(self.Edge(node1, node2, value))
        if node1 not in self.vertex:
            self.vertex.append(node1)
        if node2 not in self.vertex:
            self.vertex.append(node2)

    def get_edge(self, index):
        return self.graph[index]

    def get_neighbours(self, node):
        ans = []
        for edge in self.graph:
            tmp = edge.get_neighbour(node)
            if tmp != -1:
                ans.append(tmp)
        return ans

    def sort(self):
        self.graph = sorted(self.graph, key=lambda x: x.weight)

    def print(self):
        for i in self.graph:
            print(str(i.node1) + " " + str(i.node2) + " " + str(i.weight))

    def vertex_count(self):
        return len(self.vertex)

    def edge_count(self):
        return len(self.graph)


# graph = {'A': ['B', 'D'],
#          'B': ['A', 'C', 'E'],
#          'C': ['B'],
#          'D': ['A'],
#          'E': ['B']}

q = []
v = []
g = Graph()
g.add_edge("A", "B", 1)
g.add_edge("A", "D",  2)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 3)
g.add_edge("B", "E", 4)


def bfs(graph, node, visited, queue):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph.get_neighbours(m):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def find_min_edge(graph, vertex):
    min = sys.maxsize
    for edge in graph.graph:
        if (edge.node1 in vertex and edge.node2 not in vertex) or (edge.node1 not in vertex and edge.node2 in vertex):
            if edge.weight < min:
                min = edge.weight
                tmp_edge = edge
    return tmp_edge

def prim_mst(graph):
    vertex = []
    edges = []

    vertex.append(graph.vertex[0])

    while len(vertex) != graph.vertex_count():
        edge = find_min_edge(graph, vertex)
        edges.append(edge)
        if edge.node1 not in vertex:
            vertex.append(edge.node1)
        elif edge.node2 not in vertex:
            vertex.append(edge.node2)

    return edges


print("BFS")
bfs(g, 'A', v, q)

print()

edges = prim_mst(g)
for e in edges:
    print(e.node1 + " " + e.node2 + " " + str(e.weight))


