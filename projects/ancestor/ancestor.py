
'''

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. 
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

How can we make a graph?
    put the ancestors into a graph
    need a vertex and edge
BFS - Search for the earliest possible ancestor

'''
from stack import Stack


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

    def get_neighbors(self, vertex):
        return self.verticies[vertex]
    
    def dfs(self, starting_vertex):

        s = Stack()
        visited = set()
        s.push(starting_vertex)

        while s.size() > 0:
            vert = s.pop()

            if vert not in visited:
                visited.add(vert)
                for neighbor in self.get_neighbors(vert):
                    s.push(neighbor)
            if s.size() == 0:
                return vert


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])
    print(graph.dfs(starting_node))


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 8)
