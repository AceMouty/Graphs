
'''

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. 
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

How can we make a graph?
    put the ancestors into a graph
    need a vertex and edge
BFS - Search for the earliest possible ancestor

'''


class Graph:
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        if vertex not in self.verticies:
            self.verticies[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)

        elif v1 not in self.verticies and v2 not in self.verticies:
            raise IndexError(f"ERR: Vertex's do not exist: {v1} & {v2}")
        elif v1 not in self.verticies:
            raise IndexError(f"ERR: That Vertex does not exist: {v1}")
        elif v2 not in self.verticies:
            raise IndexError(f"ERR: That Vertex does not exist: {v2}")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[0], i[1])
    print(graph.verticies)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)